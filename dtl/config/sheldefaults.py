from yacs.config import CfgNode as CN 

_S = CN()

## conetnts of tables
### 10~  lines: SYSTEM

# for the model we want to use#####################################
_S.SYSTEM = CN()
_S.SYSTEM.MODELNAME = None
_S.SYSTEM.SAVEFOLDER = None # full path
_S.SYSTEM.LOGGERNAME = "ProcessRecords.logs" 
_S.SYSTEM.LOGGERREWRITE = True


######################################################### for LRPT##############################################
# for Model #####################################
_S.LRPT = CN()

_S.LRPT.VARIANT_DENSE_VERSION = None 
# version indicates the variants dense layer weights
# it can be DefaultWeights or CopiedWeights

_S.LRPT.FINAL_DENSE_VERSION = None
# version indicates the final block layer weights
# it can be DefaultWeights or CopiedWeights


_S.LRPT.NONTRAIN_LAYERS = ["single_block_1_BN",
                           "single_block_2_dense","single_block_2_BN",
                           "mul_add_block_1_mul_dense","mul_add_block_1_add_dense",
                           "mul_add_block_2_mul_dense","mul_add_block_2_add_dense",
                           "mul_add_block_1_mul_BN","mul_add_block_1_add_BN",
                           "mul_add_block_2_mul_BN","mul_add_block_2_add_BN",
                           "single_block_1_activation","single_block_1_dropout",
                           "mul_add_block_1_mul_activation",
                           "mul_add_block_1_mul_dropout",
                           "mul_add_block_1_add_activation",
                           "mul_add_block_1_add_dropout",
                           "mul_add_block_2_mul_activation",
                           "mul_add_block_2_mul_dropout",
                           "mul_add_block_2_add_activation",
                           "mul_add_block_2_add_dropout",
                           "final_block_activation",
                           "final_block_dropout",
                           "connect_block_2_BN","connect_block_2_activation",
                           "connect_block_2_dense","connect_block_2_dropout"]



######################################################### for TL##############################################
# for Model #####################################
_S.TL = CN()

_S.TL.FINAL_DENSE_VERSION = None
# version indicates the final block layer weights
# it can be DefaultWeights or CopiedWeights


_S.TL.NONTRAIN_LAYERS = ["single_block_1_dense","single_block_1_BN",
                         "single_block_2_dense","single_block_2_BN",
                           "mul_add_block_1_mul_dense","mul_add_block_1_add_dense",
                           "mul_add_block_2_mul_dense","mul_add_block_2_add_dense",
                           "mul_add_block_1_mul_BN","mul_add_block_1_add_BN",
                           "mul_add_block_2_mul_BN","mul_add_block_2_add_BN",
                           "single_block_1_activation","single_block_1_dropout",
                           "mul_add_block_1_mul_activation",
                           "mul_add_block_1_mul_dropout",
                           "mul_add_block_1_add_activation",
                           "mul_add_block_1_add_dropout",
                           "mul_add_block_2_mul_activation",
                           "mul_add_block_2_mul_dropout",
                           "mul_add_block_2_add_activation",
                           "mul_add_block_2_add_dropout",
                           "final_block_activation",
                           "final_block_dropout",
                           "connect_block_2_BN","connect_block_2_activation",
                           "connect_block_2_dense","connect_block_2_dropout"]




######################################################### for Shel Data ##############################################
# for Model #####################################

_S.SHELDATA = CN()
_S.SHELDATA.ThreeSets = None 
_S.SHELDATA.Info = None 

######################################################### for LRPT Train ##############################################
### for sheldata evaluate ####################
_S.LRPTTrain = CN()
_S.LRPTTrain.CVSPLIT = 3
_S.LRPTTrain.CVSEED = 111
_S.LRPTTrain.CVSHUFFLE = True

_S.LRPTTrain.VALSPLIT = True
_S.LRPTTrain.VALSIZE = 0.2 
_S.LRPTTrain.VALSPLITSHUFFLE = True
_S.LRPTTrain.VALSEED = 123


_S.LRPTTrain.BATCH_SIZE = 32
_S.LRPTTrain.EPOCHS = 100
_S.LRPTTrain.VERBOSE = 0 
_S.LRPTTrain.EarlyStoppingpatience = 10 
_S.LRPTTrain.EarlyStoppingdelta = 1e-4


_S.LRPTTrain.MODEL_WEIGHTS_PATH = "Model_WEIGHTS.h5"
_S.LRPTTrain.MODEL_STRUCTURE_PATH = "Model_STRUCTURE.json"
_S.LRPTTrain.MODEL_PATH = "Model.h5"
_S.LRPTTrain.MODEL_HISTORY_PATH = "Model_Fit_History.pkl"


######################################################### for TL Train ##############################################
### for sheldata evaluate ####################
_S.TLTrain = CN()
_S.TLTrain.CVSPLIT = 3
_S.TLTrain.CVSEED = 111
_S.TLTrain.CVSHUFFLE = True

_S.TLTrain.VALSPLIT = True
_S.TLTrain.VALSIZE = 0.2 
_S.TLTrain.VALSPLITSHUFFLE = True
_S.TLTrain.VALSEED = 123


_S.TLTrain.BATCH_SIZE = 32
_S.TLTrain.EPOCHS = 100
_S.TLTrain.VERBOSE = 0 
_S.TLTrain.EarlyStoppingpatience = 10 
_S.TLTrain.EarlyStoppingdelta = 1e-4


_S.TLTrain.MODEL_WEIGHTS_PATH = "Model_WEIGHTS.h5"
_S.TLTrain.MODEL_STRUCTURE_PATH = "Model_STRUCTURE.json"
_S.TLTrain.MODEL_PATH = "Model.h5"
_S.TLTrain.MODEL_HISTORY_PATH = "Model_Fit_History.pkl"


######################################################### for TL Train ##############################################
### for sheldata evaluate ####################
_S.ScratchTrain = CN()
_S.ScratchTrain.CVSPLIT = 3
_S.ScratchTrain.CVSEED = 111
_S.ScratchTrain.CVSHUFFLE = True

_S.ScratchTrain.VALSPLIT = True
_S.ScratchTrain.VALSIZE = 0.2 
_S.ScratchTrain.VALSPLITSHUFFLE = True
_S.ScratchTrain.VALSEED = 123


_S.ScratchTrain.BATCH_SIZE = 32
_S.ScratchTrain.EPOCHS = 100
_S.ScratchTrain.VERBOSE = 0 
_S.ScratchTrain.EarlyStoppingpatience = 10 
_S.ScratchTrain.EarlyStoppingdelta = 1e-4


_S.ScratchTrain.MODEL_WEIGHTS_PATH = "Model_WEIGHTS.h5"
_S.ScratchTrain.MODEL_STRUCTURE_PATH = "Model_STRUCTURE.json"
_S.ScratchTrain.MODEL_PATH = "Model.h5"
_S.ScratchTrain.MODEL_HISTORY_PATH = "Model_Fit_History.pkl"



def get_shelburne_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _S.clone()



