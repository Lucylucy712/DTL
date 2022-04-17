from general.imports import * 

# separate a dataset into varints/antibiotocs/results
def Separate_Data(dataset,num_classes = 33,variants_start_index=5):
    #num_classes = dataset.Antibiotics_Index.nunique()

    result_set=1*(dataset["Results"]=="resistant")
    variants_set=dataset.iloc[:,variants_start_index:].fillna(0)
    antibiotics_set=tf.keras.utils.to_categorical(dataset["Antibiotics_Index"],num_classes = num_classes)
    antibiotics_set=pd.DataFrame(antibiotics_set)
    results_set=pd.DataFrame(result_set)
    return(variants_set,antibiotics_set,results_set)

# separate a dataset into varints/antibiotocs/results and organize them 
def Organize_Separate_Data(dataset,num_classes = 33,variants_start_index=5):
    x,y,z = Separate_Data(dataset,num_classes=num_classes,variants_start_index=variants_start_index)
    x.index = range(x.shape[0])
    y.index = range(y.shape[0])
    z.index = range(z.shape[0])
    Input_X = pd.concat([x,y],axis=1)
    Input_y = copy.deepcopy(z) 
    Input_X.index = dataset.index
    Input_y.index = dataset.index
    data_info = dataset.iloc[:,:variants_start_index]
    return (Input_X,Input_y,data_info)

def Modify_Variants_Mute(variants_external,variants_original):

    appear_gene=[ele for ele in variants_external.columns if ele in variants_original.columns]
    if len(appear_gene)!=variants_external.shape[1]:
        variants_external=variants_external[appear_gene]
        #print ("New genes appear in external data and therefore we delete them")

    new_dataframe=pd.DataFrame({},columns=variants_original.columns.values,index=None)
    variants_external=pd.concat([new_dataframe,variants_external],axis=0,
                                ignore_index=False,sort=False).fillna(0)
    return (variants_external)