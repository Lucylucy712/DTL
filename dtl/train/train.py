from general.imports import * 
from general.logs import generate_log
from general.commonfuns import *


from models.PARP.PARP import *
from models.PARPCumulative.PARPCumulative import *
from models.TransferLearning.TransferLearning import *
from models.LRPT.LRPT import *

class Get_Model(object):
    """
    To wrapper all information about the data/model/config and have the function to train model
    The order should be :
    Step 1: build class
    Step 2: wrap_data() get train data and test dat (and validation data)
    Step 3: get_model(）construct model
    Step 4: train() train model
    """
    
    ########################################
    ###   Construct Class Given Config   ###
    ########################################
    def __init__(self,baseconfig,shelconfig):
        # import config and generate logger 
        self.baseconfig = baseconfig
        self.shelconfig = shelconfig
        # check the system model name 
        # check the system model name 
        if self.shelconfig.SYSTEM.SAVEFOLDER is None:
            raise ValueError("Please specify the folder path to save results")
        # construct the major savedic 
        os.makedirs(self.shelconfig.SYSTEM.SAVEFOLDER)
            
            
    ########################################
    ###        Construct Model           ###
    ########################################     
    
    def _get_model_PARP(self):
        my_model = build_parp_model(self.baseconfig)
        my_model.compile(loss=self.baseconfig.PARPTrain.LOSS,
                         optimizer=self.baseconfig.PARPTrain.OPTIMIZER,
                         metrics=self.baseconfig.PARPTrain.METRICS)
        return(my_model)
    
    def _get_model_PARP_Cumulative(self):
        my_model = build_parp_cumulative_model(self.baseconfig)
        my_model.compile(loss=self.baseconfig.PARPCumulTrain.LOSS,
                         optimizer=self.baseconfig.PARPCumulTrain.OPTIMIZER,
                         metrics=self.baseconfig.PARPCumulTrain.METRICS)
        return(my_model)

        
       
    def get_model(self):
        if self.baseconfig.SYSTEM.MODELNAME == "PARPCumulative":
            my_model = self._get_model_PARP_Cumulative()
        else :
            my_model = self._get_model_PARP_Cumulative()
            
        return(my_model)