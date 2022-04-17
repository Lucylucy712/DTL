from general.imports import * 
from models.LRPT.LRPT_legos import * 

def build_LRPT_model(shelconfig,new_model,Train_X,trained_model,trained_model_Train_X):
    """
    Step 1: Build a new model 
    Step 2: copied weights 
    
    for all layers in LRPT.NONTRAIN_LAYERS, we make it nontrainable and copied weights from trained_model
    
    If the LRPT.VARIANT_DENSE_VERSION is CopiedWeights, we copied it (partially) from trained model 
    If the LRPT.FINAL_DENSE_VERSION is CopiedWeights, we copied it from trained model 
    
    If the LRPT.VARIANT_DENSE_VERSION is DefaultWeights, we don't modify 
    If the LRPT.FINAL_DENSE_VERSION is DefaultWeights, we don't modify 
    """
    
    ## check version are specified 
    assert shelconfig.LRPT.VARIANT_DENSE_VERSION in ["DefaultWeights","CopiedWeights"],"The LRPT variants dense layer version is not available. Please double check"
    assert shelconfig.LRPT.FINAL_DENSE_VERSION in ["DefaultWeights","CopiedWeights"],"The LRPT final dense layer version is not available. Please double check"    
    
    # step 1: change layers in LRPT.NONTRAIN_LAYERS
    new_model_layers = [layer.name for layer in new_model.layers]
    trained_model_layers = [layer.name for layer in trained_model.layers]
    
    for layer_name in shelconfig.LRPT.NONTRAIN_LAYERS:
        new_model = assign_weights_and_trainable_one_layer(new_model,trained_model,layer_name,trainbale=False)
        
    # step 3: change layers "single_block_1_dense"
    if shelconfig.LRPT.VARIANT_DENSE_VERSION == "CopiedWeights": 
        assert Train_X is not None, "Train_X is empty. Please Add it"
        assert trained_model_Train_X is not None, "Train_X is empty. Please Add it"
        new_model = assign_paritial_weights_and_trainable_one_layer(new_model=new_model,trained_model=trained_model,
                                                                    new_model_Train_X = Train_X,
                                                                    trained_model_Train_X = trained_model_Train_X,
                                                                    layer_name = "single_block_1_dense",
                                                                    trainbale=True)
    # step 4: change layers "final_block_dense"
    if shelconfig.LRPT.FINAL_DENSE_VERSION == "CopiedWeights": 
        new_model = assign_weights_and_trainable_one_layer(new_model,trained_model,"final_block_dense",trainbale=True)
    
    return (new_model)


def compile_LRPT_model(model,base_config):
    # ## step 4: model compile 
    loss_key = base_config.PARPTrain.LOSS
    loss = [ele for ele in base_config.PARPTrain.LOSSDIC if ele[0]==loss_key][0][1]

    optimizer_key = base_config.PARPTrain.OPTIMIZER
    optimizer_rate = base_config.PARPTrain.OPTIMIZERATE
    optimizer = [ele for ele in base_config.PARPTrain.OPTIMIZERDIC if ele[0]==optimizer_key][0][1]

    metrics_threshold_list = base_config.PARPTrain.METRICSTHRESHOLDLIST
    metrics = [tf.keras.metrics.BinaryAccuracy(threshold = threshold,name='binary_accuracy_'+str(threshold)) for threshold in metrics_threshold_list]

    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    backend.set_value(model.optimizer.learning_rate, optimizer_rate)
    return model 










