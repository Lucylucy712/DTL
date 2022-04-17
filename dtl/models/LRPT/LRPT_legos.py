from general.imports import * 
########## Build a LRPT model
def reinitialize_one_layer(model,layer_name):
    assert layer_name in [layer.name for layer in model.layers],f"Layer {layer_name} doesn't exist in the model."
    
    weights_initializer = initializers.RandomNormal(mean=0., stddev=1.)
    my_initail_weight = weights_initializer(shape=model.get_layer(layer_name).get_weights()[0].shape)
    bias_initializer = initializers.Zeros()
    my_initail_bias = bias_initializer(shape=model.get_layer(layer_name).get_weights()[1].shape)
    
    model.get_layer(layer_name).set_weights([my_initail_weight,my_initail_bias])
    return (model)

def assign_weights_and_trainable_one_layer(new_model,trained_model,layer_name,trainbale=False):
    assert layer_name in [layer.name for layer in trained_model.layers],f"Layer {layer_name} doesn't exist in the trained model."
    assert layer_name in [layer.name for layer in new_model.layers],f"Layer {layer_name} doesn't exist in the new model."
    
    new_model.get_layer(layer_name).set_weights(trained_model.get_layer(layer_name).get_weights())
    new_model.get_layer(layer_name).trainable=trainbale
    
    return (new_model)


def assign_paritial_weights_and_trainable_one_layer(new_model,trained_model,
                                                    new_model_Train_X,trained_model_Train_X,
                                                    layer_name,trainbale=True):
    assert layer_name in [layer.name for layer in trained_model.layers],f"Layer {layer_name} doesn't exist in the trained model."
    assert layer_name in [layer.name for layer in new_model.layers],f"Layer {layer_name} doesn't exist in the new model."

    # get the new var
    new_train_var = [ele for ele in new_model_Train_X.columns if type(ele) is str]
    # get the original var
    original_train_var =  [ele for ele in trained_model_Train_X.columns if type(ele) is str]

    # get the subset of new var which exist in the original
    new_train_var_exist = [ele for ele in new_train_var if ele in original_train_var]

    # get location of those intersected variant in new dataset 
    new_pos = new_model_Train_X.columns.get_indexer(new_train_var_exist)

    # get location of those intersected variants in model 8 trianing dataset 
    original_pos = trained_model_Train_X.columns.get_indexer(new_train_var_exist) 

    # get weights of those intersected variants from original model 
    original_model_weights = trained_model.get_layer(layer_name).get_weights()[0][original_pos] 

    # get initial weights for the layer
    initial_weights = new_model.get_layer(layer_name).get_weights()[0]
    initial_bias = new_model.get_layer(layer_name).get_weights()[1]
    
    # get new initial weights by copying the original weights into the corssponding positions 
    new_weights = copy.deepcopy(initial_weights)
    new_weights[new_pos] = original_model_weights

    new_model.get_layer(layer_name).set_weights([new_weights,initial_bias])
    new_model.get_layer(layer_name).trainable = trainbale
    return(new_model)


