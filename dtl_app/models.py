from imports import * 
from style import * 
########## Methods Paragph 

model1_1 = "We seek an approach for three targets: 1) keeping what the pre-trained PARP model learned; 2) solving the domian shift probleml;\
     3) protecting from the overfitting problem. "
model1_2 = "Transfer Learning(TL) is an appropriate tool in solving the domain shift and insufficient training dataset problems. \
    In terms of deep neural networks, there are four major classes of TL approachs described in the "
model1_3 = html.A("paper.",href="https://link.springer.com/chapter/10.1007/978-3-030-01424-7_27")

model2_title = "In this project, we propose a network-based deep Transfer Learning approach on the base PARP model, with the workflow shown below."
model2_step1 = "First, we would retrain the PARP model on the source domain (the Antibiogram data).\
    We would use the optimal hyperparameters chosen by the nested cross-validation method and retrain with 20 different initial seeds"
model2_step2 = "Then,we would apply three approachs on each of the pre-trained PARP models within 3-fold cross-validation for the target domain:"
model2_step2_1_1 = "The network-based transfer learning (TL) from this "
model2_step2_1_2 = html.A("paper",href="https://openaccess.thecvf.com/content_cvpr_2014/html/Oquab_Learning_and_Transferring_2014_CVPR_paper.html")  
model2_step2_2 = "Our proposed DTL model"
model2_step2_3 = "Training the PARP model from scratch"
model2_step3 = "Finally, we compare the models' performance on the test folds of the 3-fold corss-validation.  "


model2_list = html.Ul(id='model2_list',children=[
    html.Li(html.P(model2_step1)),
    html.Li(children = [html.P(model2_step2),
                        html.Ul(children=[
                            html.Li(html.P([model2_step2_1_1,model2_step2_1_2])),
                            html.Li(html.P(model2_step2_2)),
                            html.Li(html.P(model2_step2_3))]
                        )]),
    html.Li(html.P(model2_step3))
])


plot_DTL_workflow= base64.b64encode(open("static/DTL_workflow.png", 'rb').read())
model2_4 = html.Figure(id="plot_venn",children = [
    html.Img(src='data:image/png;base64,{}'.format(plot_DTL_workflow.decode()),style={"width":"60%","height":"60%"}),
    html.Figcaption("Figure 5: The DTL Project Workflow",style={"text-align":"center"})],
    style={"text-align":"center","display":"block"})

method_total = dbc.AccordionItem([html.P([model1_1,model1_2,model1_3]),html.Br(),html.P(model2_title),model2_list,html.Br(),model2_4,],title="Methods")
method_list = dbc.Accordion([method_total],start_collapsed=False)

######## models paragraph 

#### tlm model 
tlm_1 = "We reuse all layers except for the final prediction dense layer from the pre-trained PARP model as shown below. "
tlm_2 = "During the training process on target doamin (the Shlburne data), we take 20% of the training fold randomly \
    as the validation dataset and set an early stopping with 10 steps patience on validation loss. We evaluate the performance\
        of different hyperparameter setting on the test fold within a 3-fold corss-validation. The hyperparaters contain: "
tlm_3 = html.Ul(children=[
                    html.Li(html.P("Batch size: 16, 32, 64, 128")),
                    html.Li(html.P("Training epochs: 10, 20, 50, 100")),
                    html.Li(html.P("The initial weights of prediction layer for fine-tune: the defaults OR the learnt weight from base PARP models."))])
tlm4_1 = "Check the "
tlm4_2= html.A("paper",href="https://openaccess.thecvf.com/content_cvpr_2014/html/Oquab_Learning_and_Transferring_2014_CVPR_paper.html")  
tlm4_3 = " for more details."
tlm_4 = html.P([tlm4_1,tlm4_2,tlm4_3])
plot_TL_model= base64.b64encode(open("static/tl_model.png", 'rb').read())
tlm_5 = html.Figure(id="plot_venn",children = [
    html.Img(src='data:image/png;base64,{}'.format(plot_TL_model.decode()),style={"width":"60%","height":"60%"}),
    html.Figcaption("Figure 6: The TL Model",style={"text-align":"center"})],
    style={"text-align":"center","display":"block"})

TLmodel = dbc.AccordionItem([html.P([tlm_1,tlm_2]),tlm_3,tlm_4,tlm_5],title = "TL Model")


#### dtl model 
dtl_1 = "The DTL model resues all layers from the pre-trained PARP model as shown below, except for "
dtl_2 = html.Ul(children=[
                    html.Li(html.P("The dense layer connected to the variants input")),
                    html.Li(html.P("The dense layer for prediction output"))])

plot_DTL_model= base64.b64encode(open("static/dtl_model.png", 'rb').read())
dtl_plot = html.Figure(id="plot_venn",children = [
    html.Img(src='data:image/png;base64,{}'.format(plot_DTL_model.decode()),style={"width":"60%","height":"60%"}),
    html.Figcaption("Figure 7: The DTL Model",style={"text-align":"center"})],
    style={"text-align":"center","display":"block"})        

dtl_3 = html.P("We design the transfer learning structure based on the assumptions that \
    the front dense layer can be taken as a feature extractor and the final prediction \
    dense layer is task dependent. Since the domain distributions are different between \
    the source and the target ones, it’s natural to retrain the dense layer after variants \
    to learn the different domain information. Meanwhile, we need to retrain the final dense \
    layer for the new target task. ")
dtl_4 = "We take the same setting for training process as described above in TL Model. \
    In terms of the hyperparatemer settings, we have: "
dtl_5 = html.Ul(children=[
                    html.Li(html.P("Batch size: 16, 32, 64, 128")),
                    html.Li(html.P("Training epochs: 10, 20, 50, 100")),
                    html.Li(html.P("The initial weights of prediction layer for fine-tune: \
                        the defaults OR the learnt weight from base PARP models.")),
                    html.Li(html.P("The initial weights of variants dense layer for fine-tune: \
                        the defaults OR the learnt weight from base PARP models."))])

DTLmodel = dbc.AccordionItem([html.P([dtl_1,dtl_2,dtl_plot]),dtl_3,html.P([dtl_4,dtl_5])],title = "DTL Model")

#### Scratch Model 
scratch_1 = "We retrain the PARP model on the source domian (the Shelburne data) from scratch.\
    We take the same setting for training process as described above in TL Model. \
    In terms of the hyperparatemer settings, we have: "
scratch_2 = html.Ul(children=[
                    html.Li(html.P("Batch size: 16, 32, 64, 128")),
                    html.Li(html.P("Training epochs: 10, 20, 50, 100"))])
Scratch = dbc.AccordionItem([html.P([scratch_1,scratch_2])],title = "Train from scratch") 
#### combine the three models together
model_list = dbc.Accordion([TLmodel,DTLmodel,Scratch],start_collapsed=True)



models = html.Div([
    html.H2("Methods"),
    method_list,
    html.H2("Models"),
    model_list
    ],
    style=CONTENT_STYLE)


