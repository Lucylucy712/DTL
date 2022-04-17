from yacs.config import CfgNode as CN 
import tensorflow as tf 

_C = CN()

## conetnts of tables
### ~ 20 lines: system
### 20 ~ 90 lines: PARP
### 90~ 150 lines: PARPCumulative
### 150 ~220 lines: Transfer Learning
### 220~  lines: LRPT


# for the model we want to use#####################################
_C.SYSTEM = CN()
_C.SYSTEM.SAVEFOLDER = None # full path
_C.SYSTEM.LOGGERNAME = "ProcessRecords.logs" 
_C.SYSTEM.LOGGERREWRITE = True

######################################################### for PARP##############################################
# for PARP Data ##############################################
_C.PARPData = CN()
_C.PARPData.TrainPath = None
#_C.PARPData.TrainVariants = None 
#_C.PARPData.TrainAntibiotics = None 
#_C.PARPData.TrainResults = None 
#_C.PARPData.TrainX = None 
#_C.PARPData.Trainy = None

_C.PARPData.TestPath = None


# for the PARP Model #####################################
_C.PARP = CN()
## for the input size
_C.PARP.VARIANTS_INPUT_DIM = None
_C.PARP.ANTI_INPUT_DIM = None 
_C.PARP.DENSE_SIZE = 1024 

## for the multi_add_block
_C.PARP.MUL_ADD_BLOCK_NUM = 2
_C.PARP.MUL_DROP_RATE = 0.5
_C.PARP.ADD_DROP_RATE = 0.5
_C.PARP.MUL_ACTIVATION_NAME = "relu"
_C.PARP.ADD_ACTIVATION_NAME = "relu"
_C.PARP.MUL_ADD_BLOCK_1_MUL_SEED = 111
_C.PARP.MUL_ADD_BLOCK_1_ADD_SEED = 111

## for single dense block
_C.PARP.SINGLE_DROP_RATE = 0.5
_C.PARP.SINGLE_ACTIVATION_NAME = "relu"
_C.PARP.SINGLE_BLOCK_NUM = 1 
_C.PARP.SINGLE_BLOCK_1_SEED = 111
_C.PARP.SINGLE_BLOCK_2_SEED = 111

## for the final dense block
_C.PARP.FINAL_DROP_RATE = 0.5
_C.PARP.FINAL_ACTIVATION_NAME = "relu"
_C.PARP.FINAL_BLOCK_SEED = 111
## for the connect block
_C.PARP.CONNECT_DROP_RATE = 0.5
_C.PARP.CONNECT_ACTIVATION_NAME = "relu"
_C.PARP.CONNECT_SEED = 111

# for the PARP TRAIN #####################################

_C.PARPTrain = CN()

##### PARP Compose 
_C.PARPTrain.LOSSDIC = [("binary_crossentropy",tf.keras.losses.BinaryCrossentropy(from_logits=False))]
_C.PARPTrain.LOSS = "binary_crossentropy"

_C.PARPTrain.OPTIMIZERDIC = [
    ["adam",tf.keras.optimizers.Adam(learning_rate=0.001)],
    ["rmsprop",tf.keras.optimizers.RMSprop(learning_rate=0.001)],
    ["sgd",tf.keras.optimizers.SGD(learning_rate=0.001)]]
_C.PARPTrain.OPTIMIZER = 'adam'
_C.PARPTrain.OPTIMIZERATE= 0.001

_C.PARPTrain.METRICS = 'accuracy'
_C.PARPTrain.METRICSTHRESHOLDLIST= [0.1,0.3,0.5,0.7,0.9]

## for outer split

_C.PARPTrain.VALSIZE = 0.2
_C.PARPTrain.VALSEED = 123
_C.PARPTrain.VALSHUFFLE = True

_C.PARPTrain.EarlyStoppingpatience = 10 
_C.PARPTrain.EarlyStoppingdelta = 1e-4

_C.PARPTrain.BATCHSIZE = 32
_C.PARPTrain.EPOCHS = 50
_C.PARPTrain.VERBOSE = 0

_C.PARPTrain.MODEL_WEIGHTS_PATH = "modelweights.h5"
_C.PARPTrain.MODEL_HISTORY_PATH = "fithistory.pkl"

## for logs save 


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()



