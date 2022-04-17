import os 
import sys
sys.path.append("/work/PCDC/s202005/Research/TransferLearning/Shelburne/Codes")
from config.sheldefaults import *
# config.basedeafults is copied from "/work/PCDC/s202005/Research/PARP/Codes/PARpforLRPT/config/defaults"
from config.basedefaults import *
from general.commonfuns import * 
from general.imports import *
from general.logs import * 
from data.data_legos import * 
from models.TL.TL import *
sys.path.append("/work/PCDC/s202005/Research/PARP/Codes/PARPforLRPT")
from model.PARPModel import * 
class ShelTL(object):
    def __init__(self):
        pass
    
    def _get_base_config(self,base_config_index,base_yaml_index,base_config_folder):
        config_folder_dic = sorted([ele for ele in os.listdir(base_config_folder) if ele.startswith("Epochs")])
        config_subfolder = os.path.join(base_config_folder,config_folder_dic[base_config_index])
        yaml_folder = sorted([ele for ele in os.listdir(config_subfolder) if ele.endswith(".yaml")])
        base_yaml_path = os.path.join(config_subfolder,yaml_folder[base_yaml_index])
        config = get_cfg_defaults()
        config.merge_from_file(base_yaml_path)
        
        ## return 
        self.base_config = config
        self.base_yaml_path = base_yaml_path
        self.parp_folder = config.SYSTEM.SAVEFOLDER.split("Single_1_Anti_2_Dense_1024/")[-1]
        
        
    def _get_shel_config(self,config_file_path):
        config = get_shelburne_defaults()
        config.merge_from_file(config_file_path)
        fin_ver = config.TL.FINAL_DENSE_VERSION
        batch = config.TLTrain.BATCH_SIZE
        epochs = config.TLTrain.EPOCHS
        tempname = fin_ver+"_Epochs_"+str(epochs)+"_Batch_"+str(batch)
        ## return
        self.shel_config = config
        self.save_folder = os.path.join(config.SYSTEM.SAVEFOLDER,self.parp_folder,tempname)
        os.makedirs(self.save_folder,exist_ok=True)
        
    def _get_cv_and_data(self):
        shel_config = self.shel_config
        ######## get data 
        Variants,Antibiotics,Results = open_pickle(shel_config.SHELDATA.ThreeSets)
        DataInfo = pd.read_csv(shel_config.SHELDATA.Info)
        Shel_X = pd.concat([Variants,Antibiotics],axis=1)
        shel_data = {"Variants":Variants,
                     "Antibiotics":Antibiotics,
                     "Results":Results,
                     "X":Shel_X,
                     "Info":DataInfo}

        ######### get cv 
        Totaly = Results
        cv_split = KFold(n_splits=shel_config.LRPTTrain.CVSPLIT,
                         shuffle=shel_config.LRPTTrain.CVSHUFFLE,
                         random_state=shel_config.LRPTTrain.CVSEED)
        for cv_index,(train_ix,test_ix) in enumerate(cv_split.split(Totaly)):
            cv_save_folder = os.path.join(self.save_folder,"cv_"+str(cv_index))
            os.makedirs(cv_save_folder,exist_ok=True) # make the dircitiony 
            split_index = {"train_ix":train_ix,"test_ix":test_ix}
            save_as_pickle(split_index,os.path.join(cv_save_folder,"train_test_ix.pkl"))
            
        ## return 
        self.shel_data = shel_data
    
    def _get_base_model_path(self,parp_folder):
        
        epochsname  = os.path.split(os.path.split(self.base_yaml_path)[0])[1]
        seedname = os.path.split(self.base_yaml_path)[1].replace(".yaml","")
        trained_model_weights_path = os.path.join(parp_folder,epochsname,seedname,"modelweights.h5")
        ## return 
        self.trained_model_weights_path = trained_model_weights_path
        
    def _wrap_PARP_data(self):
        # get train/test/or validation for training process
        Variants,Antibiotics,Results = open_pickle(self.base_config.PARPData.TrainPath)
        PARP_Train_X = pd.concat([Variants,Antibiotics],1)
        
        # return 
        self.PARP_Train_X = PARP_Train_X.iloc[:5,:]  
        
        opts = ["PARP.VARIANTS_INPUT_DIM", Variants.shape[1],
                "PARP.ANTI_INPUT_DIM", Antibiotics.shape[1]]
        self.base_config.merge_from_list(opts)
        
    def _get_base_model_PARP(self):

        model = build_parp_model(self.base_config)
        # ## step 4: model compile 
        loss_key = self.base_config.PARPTrain.LOSS
        loss = [ele for ele in self.base_config.PARPTrain.LOSSDIC if ele[0]==loss_key][0][1]

        optimizer_key = self.base_config.PARPTrain.OPTIMIZER
        optimizer_rate = self.base_config.PARPTrain.OPTIMIZERATE
        optimizer = [ele for ele in self.base_config.PARPTrain.OPTIMIZERDIC if ele[0]==optimizer_key][0][1]

        metrics_threshold_list = self.base_config.PARPTrain.METRICSTHRESHOLDLIST
        metrics = [tf.keras.metrics.BinaryAccuracy(threshold = threshold,
                                                   name='binary_accuracy_'+str(threshold)) for threshold in metrics_threshold_list]

        model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
        backend.set_value(model.optimizer.learning_rate, optimizer_rate)
        

        model.load_weights(self.trained_model_weights_path)
        self.PARP_base_model = model 
        
    def _get_TL_model(self):
        TL_base_config = copy.deepcopy(self.base_config)
        TL_base_model = build_parp_model(TL_base_config)
        TL_base_model.load_weights(self.trained_model_weights_path)
        
        TL_model = build_TL_model(self.shel_config,TL_base_model)
        TL_model = compile_TL_model(TL_model,TL_base_config)
        self.TL_model = TL_model
    
    def eval_on_basePARP(self,cv_folder):
        
        assert cv_folder in os.listdir(self.save_folder),"Cv folder doesn't exist"
        cv_ix = open_pickle(os.path.join(self.save_folder,cv_folder,"train_test_ix.pkl"))

        ## get save folder
        savefolder = os.path.join(self.save_folder,cv_folder)
        train_ix = cv_ix["train_ix"]
        test_ix = cv_ix["test_ix"]

        ## get 
        X = self.shel_data["X"]
        X = Modify_Variants_Mute(X,self.PARP_Train_X)

        Y = self.shel_data["Results"]

        ## get train and test 
        train_x = X.to_numpy()[train_ix]
        test_x = X.to_numpy()[test_ix]

        train_y = Y.to_numpy()[train_ix]
        test_y = Y.to_numpy()[test_ix]

        ## evaluate 
        train_score = self.PARP_base_model.evaluate(train_x,train_y,verbose=0)
        test_score = self.PARP_base_model.evaluate(test_x,test_y,verbose=0)

        train_pred = self.PARP_base_model.predict(train_x,verbose=0)
        test_pred =self.PARP_base_model.predict(test_x,verbose=0)

        score = {"train_score":train_score,"test_score":test_score}
        pred = {"train_pred":train_pred,"test_pred":test_pred}

        ## save 
        save_as_pickle(data=score,path = os.path.join(savefolder,"basePARP_score.pkl"))
        save_as_pickle(data=pred,path = os.path.join(savefolder,"basePARP_pred.pkl"))
    
        
    def train_and_eval_TL(self,cv_folder):
        assert cv_folder in os.listdir(self.save_folder),"Cv folder doesn't exist"
        cv_ix = open_pickle(os.path.join(self.save_folder,cv_folder,"train_test_ix.pkl"))

        ## get save folder
        savefolder = os.path.join(self.save_folder,cv_folder)
        X = Modify_Variants_Mute(self.shel_data["X"],self.PARP_Train_X)

        train_x = X.to_numpy()[cv_ix["train_ix"]]
        train_y = self.shel_data["Results"].to_numpy()[cv_ix["train_ix"]]

        test_x = X.to_numpy()[cv_ix["test_ix"]]
        test_y = self.shel_data["Results"].to_numpy()[cv_ix["test_ix"]]


        log_dir = os.path.join(savefolder,"tensorboard/logs")

        if self.shel_config.TLTrain.VALSPLIT is not None:
            callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                             patience=self.shel_config.TLTrain.EarlyStoppingpatience, 
                                             min_delta=self.shel_config.TLTrain.EarlyStoppingdelta),
                         tf.keras.callbacks.TensorBoard(log_dir=log_dir)]
            indices = range(len(train_x))
            train_x, val_x, train_y, val_y,train_idx,val_idx = train_test_split(train_x,train_y,indices,
                                                                                test_size=self.shel_config.TLTrain.VALSIZE,
                                                                                shuffle=self.shel_config.TLTrain.VALSPLITSHUFFLE,
                                                                                random_state=self.shel_config.TLTrain.VALSEED)

            history = self.TL_model.fit(x=train_x,y=train_y,
                                          batch_size=self.shel_config.TLTrain.BATCH_SIZE,
                                          epochs=self.shel_config.TLTrain.EPOCHS,
                                          verbose=self.shel_config.TLTrain.VERBOSE,
                                          validation_data=(val_x,val_y),
                                          callbacks=callbacks)
        else:
            callbacks = [tf.keras.callbacks.EarlyStopping(monitor='loss',
                                     patience=self.shel_config.TLTrain.EarlyStoppingpatience, 
                                     min_delta=self.shel_config.TLTrain.EarlyStoppingdelta),
                         tf.keras.callbacks.TensorBoard(log_dir=log_dir)]
            history = self.TL_model.fit(x=train_x,y=train_y,
                                          batch_size=self.shel_config.TLTrain.BATCH_SIZE,
                                          epochs=self.shel_config.TLTrain.EPOCHS,
                                          verbose=self.shel_config.TLTrain.VERBOSE,
                                          callbacks = callbacks)
        ## save history 
        temp_path = os.path.join(savefolder,self.shel_config.TLTrain.MODEL_HISTORY_PATH)
        save_as_pickle(data =history.history,path = temp_path)

        ## save model 
        h5_file = os.path.join(savefolder,self.shel_config.TLTrain.MODEL_WEIGHTS_PATH)
        self.TL_model.save_weights(h5_file)

        ## save train and val idx 
        if train_idx:
            split_index = {"train_ix":train_idx,"val_ix":val_idx}
            save_as_pickle(split_index,os.path.join(savefolder,"fit_train_val_ix.pkl"))

        ## evaluate and predict 
        train_score = self.TL_model.evaluate(train_x,train_y,verbose=0)
        train_pred = self.TL_model.predict(train_x,verbose=0)

        test_score = self.TL_model.evaluate(test_x,test_y,verbose=0)
        test_pred = self.TL_model.predict(test_x,verbose=0)

        score = {"train_score":train_score,"test_score":test_score}
        pred = {"train_pred":train_pred,"test_pred":test_pred}

        if train_idx:
            val_score = self.TL_model.evaluate(val_x,val_y,verbose=0)
            val_pred = self.TL_model.predict(val_x,verbose=0)
            score["val_score"] = val_score
            pred["val_pred"] = val_pred

        save_as_pickle(data=score,path = os.path.join(savefolder,"fit_score.pkl"))
        save_as_pickle(data=pred,path = os.path.join(savefolder,"fit_pred.pkl"))

        
        
    def build(self,base_config_index,base_yaml_index,config_file_path):
        base_config_folder = "/work/PCDC/s202005/Research/PARP/Codes/PARPforLRPT/config/Single_1_Anti_2_Dense_1024"
        parp_folder ="/work/PCDC/s202005/Research/PARP/Results/PARPforLRPT/Single_1_Anti_2_Dense_1024" 
        self._get_base_config(base_config_index=base_config_index,
                              base_config_folder=base_config_folder,
                              base_yaml_index=base_yaml_index)
        self._get_shel_config(config_file_path=config_file_path)
        self._get_cv_and_data()
        self._get_base_model_path(parp_folder=parp_folder)
        self._wrap_PARP_data()
        self._get_base_model_PARP()
        self._get_TL_model()

    def run(self,cv_folder):
        self.eval_on_basePARP(cv_folder=cv_folder)
        self.train_and_eval_TL(cv_folder=cv_folder)
        
if __name__=="__main__":
    base_config_folder = "/work/PCDC/s202005/Research/PARP/Codes/PARPforLRPT/config/Single_1_Anti_2_Dense_1024"
    parp_folder ="/work/PCDC/s202005/Research/PARP/Results/PARPforLRPT/Single_1_Anti_2_Dense_1024" 
    base_config_dic = sorted([ele for ele in os.listdir(base_config_folder) if ele.startswith("Epochs")])
    
    
    base_config_index = int(sys.argv[1]) # number inside base_config_folder: 0-5 (6 in total)
    config_subfolder = os.path.join(base_config_folder,base_config_dic[base_config_index])
    base_yaml_folder = sorted([ele for ele in os.listdir(config_subfolder) if ele.endswith(".yaml")])
    base_yaml_index = int(sys.argv[2])
    
    config_file_folder = "/work/PCDC/s202005/Research/TransferLearning/Shelburne/Codes/config/Single_1_Anti_2_Dense_1024_TL_Ensemble"
    config_file_dic = sorted([ele for ele in os.listdir(config_file_folder) if ele.endswith(".yaml")])
        
    
    for config_file_index in range(len(config_file_dic)): # base_yaml_index 0-31 (32 in total)
        config_file_path = os.path.join(config_file_folder,config_file_dic[config_file_index])
        for cv_name in ["cv_0","cv_1","cv_2"]:
            MyModel = ShelTL()
            MyModel.build(base_config_index=base_config_index,
                          base_yaml_index=base_yaml_index,
                          config_file_path=config_file_path)
            MyModel.run(cv_name)
