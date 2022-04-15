from imports import * 
## load data 
datapath = "Epochs_100_Batch_128_total.csv"
DATA = pd.read_csv(datapath,dtype={"config_epochs":int,"config_batch":int})
DATA.rename(columns={"method":"config_method"},inplace=True)

## metric name fic 
METRIC_NAME_DIC={
    "f1score":"F1 score",
    "precision_score":"precision",
    "accuracy_score":"accuracy",
    "balanced_accuracy_score":"balanced accuracy score",
    "recall_score":"recall",
    "roc_auc_score":"AUC"}

##
method_option = [{"label":"Transfer Learning(TL)","value":"TL"},
{"label":"DTL","value":"DTL"},{"label":"Scratch","value":"Scratch"}]
## input layer
temp_list = DATA[["config_input_weights"]].dropna().iloc[:,0].unique()
input_weights_option =[{"label":ele,"value":ele} for ele in sorted(temp_list)]

## pred layer
temp_list = DATA[["config_pred_weights"]].dropna().iloc[:,0].unique()
pred_weights_option = [{"label":ele,"value":ele} for ele in sorted(temp_list)]

batch_option = [{"label":ele,"value":ele} for ele in sorted(DATA.config_batch.unique())]
epoch_option = [{"label":ele,"value":ele} for ele in sorted(DATA.config_epochs.unique())]

metric_option = [{"label":"F1 score","value":"f1score"},{"label":"precision","value":"precision_score"},
{"label":"accuracy","value":"accuracy_score"},
{"label":"balanced accuracy score","value":"balanced_accuracy_score"},
{"label":"recall","value":"recall_score"},
{"label":"AUC","value":"roc_auc_score"}]

load_checklist= html.Div(
    [
        # method 
        html.Label('Choose method:',id="method_label",style={"font-size":'28px'}),
        dbc.Checklist(id="method_option",options=method_option,value=["LRPT","TL"],
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True),
        # inputs wights
        html.Label('Choose input weights class:', style={"font-size":'28px',"margin-top":"15px"}),
        dbc.Checklist(id="input_weights_option",options=input_weights_option,value=["DefaultWeights"],
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True),
        # pred weight 
        html.Label('Choose predication weights class:', style={"font-size":'28px',"margin-top":"15px"}),
        dbc.Checklist(id="pred_weights_option",options=pred_weights_option,value=["DefaultWeights"],
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True),
        # batch
        html.Label('Choose fitting batch:', style={"font-size":'28px',"margin-top":"15px"}),
        dbc.Checklist(id="batch_option",options=batch_option,value=[128],
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True),
        # epochs
        html.Label('Choose fitting epochs:',style={"font-size":'28px',"margin-top":"15px"}),
        dbc.Checklist(id="epoch_option",options=epoch_option,value=[10],
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True),
        # metric
        html.Label('Choose the metric:',style={"font-size":'28px',"margin-top":"15px"}),
        dbc.RadioItems(id="metric_option",options=metric_option,
        inputStyle={"margin-left": "20px"},value="accuracy_score",
        input_checked_style={"borderColor":"#0c72ad","backgroundColor":"#1776ad"},
        label_checked_style={"color":"#1776ad"},inline=True)]
)


