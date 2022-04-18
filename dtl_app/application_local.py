from imports import * 
from style import * 
import sidebar,homepage,background,motivation,models,loaddata,download
pd.options.mode.chained_assignment = None
app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN],
suppress_callback_exceptions=True,assets_folder="assets",assets_url_path="assets")

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar.sidebar, content])


################# Page Callbacks ###################################

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return homepage.homepage
    elif pathname == "/project/background":
        return background.background
    elif pathname == "/project/motivation":
        return motivation.motivation
    elif pathname == "/project/model":
        return models.models
    elif pathname == "/results/evaluation":
        return html.H3('In Process....')
    elif pathname == "/results/plot":
        return html.Div([
            loaddata.load_checklist,
            html.Div(id='data_temp', style={'display': 'none'}, children = loaddata.DATA.to_json()),
            html.Div(id="metric_dic_temp",style={'display': 'none'}, children = loaddata.METRIC_NAME_DIC),
            dcc.Graph(id="box_plot")
            ])
    elif pathname == "/download":
        return html.Div([
            download.download
        ])
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )




@app.callback(
    Output(component_id="box_plot",component_property="figure"),
    Input(component_id="data_temp",component_property="children"),
    Input(component_id="method_option",component_property="value"),
    Input(component_id="epoch_option",component_property="value"),
    Input(component_id="batch_option",component_property="value"),
    Input(component_id="pred_weights_option",component_property="value"),
    Input(component_id="input_weights_option",component_property="value"),
    Input(component_id="metric_option",component_property="value")
)
def draw_graph(data,method,epochs_list,batch_list,pred_weights_list,input_weights_list,metric):
    if not metric:
        return {}
    ## get data separately 
    data = pd.read_json(data)
    tempdata = data.copy(deep=True)
    if epochs_list:
        tempdata = tempdata[tempdata.config_epochs.isin(epochs_list)]
    if batch_list:
        tempdata = tempdata[tempdata.config_batch.isin(batch_list)]
    ## 2. get parp data
    ### stratgey: For the same seed + cv, the PARP should be the same 
    temp_parp = tempdata[(tempdata.model=="PARP")]
    temp_cols = [ele for ele in temp_parp.columns if "config" not in ele] + ["config_epochs","config_batch"]
    temp_parp = temp_parp[temp_cols]
    temp_parp.drop_duplicates(inplace=True)
    temp_parp["config_method"] = "PARP"
    #temp_parp["config"] = temp_parp.apply(lambda x:"Epochs_"+str(x["config_epochs"])+"_Batch_"+str(x["config_batch"])+"_PARP",axis=1)
    def parp_config(epochs,batch):
        return "Model: PARP <br>" + "Epochs: "+str(epochs)+"<br>Batch: "+str(batch)
    temp_parp["config"] = temp_parp.apply(lambda x: parp_config(x["config_epochs"],x["config_batch"]),axis=1)
        

    ## 3. get DTL data 
    temp_DTL = tempdata[tempdata.model=="DTL"]
    if pred_weights_list:
        temp_DTL = temp_DTL[temp_DTL.config_pred_weights.isin(pred_weights_list)]
    if input_weights_list:
        temp_DTL = temp_DTL[temp_DTL.config_input_weights.isin(input_weights_list)]
    def dtl_config(epochs,batch,pred_weights,input_weights):
        return "Model: DTL <br>" + "Epochs: "+str(epochs)+"<br>Batch: "+str(batch)+"<br>Pred_weights: "+pred_weights + "<br>Input_weights: "+input_weights
    temp_DTL["config"]=temp_DTL.apply(lambda x: dtl_config(x["config_epochs"],x["config_batch"],x["config_pred_weights"],x["config_input_weights"]),axis=1) 


    ## 4. get TL data 
    temp_TL = tempdata[tempdata.model=="TL"]
    if pred_weights_list:
        temp_TL = temp_TL[temp_TL.config_pred_weights.isin(pred_weights_list)]
    def tl_config(epochs,batch,pred_weights):
        return "Model: TL <br>" + "Epochs: "+str(epochs)+"<br>Batch: "+str(batch)+"<br>Pred_weights: "+pred_weights
    temp_TL["config"]=temp_TL.apply(lambda x: tl_config(x["config_epochs"],x["config_batch"],x["config_pred_weights"]),axis=1) 
    ## 5. get Scratch data 
    temp_Scratch = tempdata[tempdata.model=="Scratch"]
    def scratch_config(epochs,batch):
        return "Model: Scratch <br>" + "Epochs: "+str(epochs)+"<br>Batch: "+str(batch)
    temp_Scratch["config"] = temp_Scratch.apply(lambda x: scratch_config(x["config_epochs"],x["config_batch"]),axis=1)

    ## final data 
    results = pd.concat([temp_parp,temp_TL,temp_DTL,temp_Scratch])
    if method:
        method_ture = ["PARP"] + method 
        results = results[results.model.isin(method_ture)]
   
    ## for px
    agg_func = {metric:["describe"]}
    temp_df = results.groupby(["config","model"]).agg(agg_func).reset_index()

    temp_df = temp_df.T.reset_index()
    temp_df.drop(columns=["level_0",'level_1'],inplace=True)
    temp_df.loc[0,"level_2"] = "config"
    temp_df.loc[1,"level_2"] = "model"
    temp_df = temp_df.T
    temp_df.columns = temp_df.iloc[0]
    temp_df.drop(temp_df.index[0],inplace=True)

    total_results = pd.merge(results,temp_df,how="left")
    total_results["input_w"] = total_results["config_input_weights"]
    total_results["pred_w"] = total_results["config_pred_weights"]
    total_results["epochs"] = total_results["config_epochs"]
    total_results["batch"] = total_results["config_batch"]
    
    total_results.sort_values(["model","input_w","pred_w","batch","epochs"],inplace=True)
    color_discrete_map = {'PARP': 'rgb(215,25,28)', 'Scratch': 'rgb(136,86,167)', 'TL': 'rgb(49,163,84)',"DTL":"rgb(8,81,156)"}
    ## 
    fig = px.box(total_results,x="config",y=metric,color="model",color_discrete_map=color_discrete_map,
    hover_name="model",points="all",
    hover_data={'config':False,"input_w":True,"pred_w":True,"epochs":True,"batch":True,"model":False,
    metric:":.2f","count":True,
    'mean':':.2f','std':":.2f",'25%':':.2f',
    '50%':':.2f', '75%':':.2f'})

    METRIC_NAME_DIC={
        "f1score":"F1 score",
        "precision_score":"precision",
        "accuracy_score":"accuracy",
        "balanced_accuracy_score":"balanced accuracy score",
        "recall_score":"recall",
        "roc_auc_score":"AUC"}

    fig.update_yaxes(title=METRIC_NAME_DIC[metric],title_font_size=20)
    fig.update_xaxes(title="",visible=True,showticklabels=True,ticklabelposition="outside")
    fig.update_traces(quartilemethod="exclusive")
    return fig 


@app.callback(
    Output("download_csv", "data"),
    Input("download_button", "n_clicks"),
    prevent_initial_call=True)# button is btn_csv 
def func(n_clicks):
    return dcc.send_data_frame(loaddata.DATA.to_csv, "Results.csv")





if __name__ == "__main__":
    app.run_server(port=8888)