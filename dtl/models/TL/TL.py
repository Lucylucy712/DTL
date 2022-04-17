from general.imports import * 

def reinitialize_one_layer(model,layer_name):
    assert layer_name in [layer.name for layer in model.layers],f"Layer {layer_name} doesn't exist in the model."
    
    weights_initializer = initializers.RandomNormal(mean=0., stddev=1.)
    my_initail_weight = weights_initializer(shape=model.get_layer(layer_name).get_weights()[0].shape)
    bias_initializer = initializers.Zeros()
    my_initail_bias = bias_initializer(shape=model.get_layer(layer_name).get_weights()[1].shape)
    
    model.get_layer(layer_name).set_weights([my_initail_weight,my_initail_bias])
    return (model)


def build_TL_model(config,trained_model):
    """
    copy weights 
    
    Based on the pre-trained model, we make all layers in config.TL.NONTRAIN_LAYERS non trainable. 
    layer "final_block_dense" is not in config.TL.NONTRAIN_LAYERS
    
    If the TL.VERSION is CopiedWeights, we don't do anything
    If the TL.VERSION is DefaultWeights, we reassign the iniital weights is default
    
    """
    assert config.TL.FINAL_DENSE_VERSION in ["DefaultWeights","CopiedWeights"],"The transfer learning version is not available. Please double check"
    
    trained_model_layers = [layer.name for layer in trained_model.layers]
    for layer_name in config.TL.NONTRAIN_LAYERS:
        assert layer_name in trained_model_layers, f"the non-trainable layer {layer_name} doesn't exist in trained model."
        trained_model.get_layer(layer_name).trainable = False
    if config.TL.FINAL_DENSE_VERSION == "DefaultWeights":
        trained_model = reinitialize_one_layer(trained_model,"final_block_dense")
    return (trained_model)
    
    
def compile_TL_model(model,base_config):
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
        