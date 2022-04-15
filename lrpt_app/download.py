from imports import * 
from style import * 

### results data 
codebook_header = [
    html.Thead(html.Tr([html.Th("Column"),html.Th("Column Type"), 
    html.Th("Meaning"),html.Th("Class for discrete variable"),
    html.Th("Range for numeric variable ")]))
]
row1 = html.Tr([html.Td("model"),html.Td("Discrete"), html.Td("The applied model"),html.Td("PARP, DTL, TL, Scratch"),html.Td("")])
row2 = html.Tr([html.Td("threshold"),html.Td("Numeric"),html.Td("The classification threshold"),html.Td(""),html.Td("0.5")])
row3 = html.Tr([html.Td("f1score"),html.Td("Numeric"),html.Td("The F1 Score"),html.Td(""),html.Td("[0,1]")])
row4 = html.Tr([html.Td("precision_score"),html.Td("Numeric"),html.Td("The Precision Score"),html.Td(""),html.Td("[0,1]")])
row5 =  html.Tr([html.Td("accuracy_score"),html.Td("Numeric"),html.Td("The Accuracy Score"),html.Td(""),html.Td("[0,1]")])
row6 =  html.Tr([html.Td("balanced_accuracy_score"),html.Td("Numeric"),html.Td("The Balanced Accuracy Score"),html.Td(""),html.Td("[0,1]")])
row7 =  html.Tr([html.Td("recall_score"),html.Td("Numeric"),html.Td("The Recall Score"),html.Td(""),html.Td("[0,1]")])
row8 =  html.Tr([html.Td("roc_auc_score"),html.Td("Numeric"),html.Td("The AUROC"),html.Td(""),html.Td("[0,1]")])
row9 = html.Tr([html.Td("seed"),html.Td("Discrete"),html.Td("The PARP model seet"),html.Td("Seed_100-Seed_117, Seed_119, Seed_120"),html.Td("")])
row10 = html.Tr([html.Td("cv"),html.Td("Discrete"),html.Td("The 3-fold cross-valdiation cv"),html.Td("cv_0, cv_1, cv_2"),html.Td("")])
row11 = html.Tr([html.Td("config"),html.Td("Discrete"),html.Td("The different model's config summary"),html.Td(""),html.Td("")])
row12 = html.Tr([html.Td("config_method"),html.Td("Discrete"),html.Td("The model"),html.Td("DTL, TL, Scratch"),html.Td("")]) 
row13 = html.Tr([html.Td("config_epochs"),html.Td("Discrete"),html.Td("The training epochs"),html.Td("10, 20, 50, 100"),html.Td("")]) 
row14 = html.Tr([html.Td("config_batch"),html.Td("Discrete"),html.Td("The training batch"),html.Td("16, 32, 64, 128"),html.Td("")]) 
row15 = html.Tr([html.Td("config_pred_weights"),html.Td("Discrete"),html.Td("The default weights of prediction dense layer"),html.Td("CopiedWeights, DefaultWeights"),html.Td("")]) 
row16 = html.Tr([html.Td("config_input_weights"),html.Td("Discrete"),html.Td("The default weights of input dense layer"),html.Td("CopiedWeights, DefaultWeights"),html.Td("")]) 


codebook_body = [html.Tbody([row1, row2, row3, row4, row5, row6,row7,row8,
row9,row10,row11,row12,row13,row14,row15,row16])]
codebook_table = dbc.Table(codebook_header + codebook_body,bordered=True,hover=True,responsive=True,striped=True)

#####




download_button = html.Button("Click me",id="download_button",style={"border-radius":"8px","background-color":"#1776ad","font-size":"30px","color":"white"})
download =html.Div([
    html.H2("Download the interactive plot data"),
    download_button,
    dcc.Download(id="download_csv"),
    html.Br(),html.Br(),
    html.H3("Codebook Table: "),
    codebook_table,
    html.Br(),html.Hr(),
    html.H2("Models")
    ],
    style=CONTENT_STYLE)
