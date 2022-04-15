from imports import * 
from style import * 

intro1 = "As Antimicrobial resistance (AMR) is becoming a global health threat,\
    predicting bacteria samples’ resistance to antibiotics is becoming essential to conquer AMR\
    With the availability of bacteria samples’ whole genome sequencing (NGS), \
    we could build up label-supervised classification models using genomes with the paired phenotypes. "

intro2_1 = "Our group proposed a bioinformatcis tool,\
    variant mapping and prediction of antibiotic resistance ("
intro2_2 = html.A("VAMPr",href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007511")
intro2_3=") to derive gene ortholog-based sequence features for protein variants and performe analysis for AMR problem. "

intro3 = "We curated 3,393 bacterial genomes from 9 different bacteria species and the paired AMR phenotypes to 29 antibiotics,\
     covering 93 various pathology-antibiotic combinations"


parp1 = "To build up a general prediction model for all available combinations, \
    we proposed a pan-antibiotic resistance prediction model, PARP, with workflow shown below."

parp2_1= "We employeed the "
parp2_2 = html.A("FiLM structure",href="https://arxiv.org/abs/1709.07871")
parp2_3 = " in our PARP model, with sturcture shown below. \
    The model input consists of two inputs: 1) the protein-level orthology gene features denoted by KEGG orthology gene name and variants; \
    2) antibiotic class."

parp3 = "We utilized grid search approach for hyper-parameters. Then, we compared it with three other common-used machine learning models,\
    including Random Forest(RF), Logistic Regression with L2 constraints(L2), and Support Vector Machine(SVM) on an external test dataset."

parp4 = "The PARP model outperforms in terms of the weighted test prediction accuracy as shown below."


#### add plots 

plot_parp_workflow= base64.b64encode(open("assets/PARP_workflow.png", 'rb').read())
plot_parp_str = base64.b64encode(open("assets/PARP_structure.png", 'rb').read())
plot_parp_acc = base64.b64encode(open("assets/PARP_accbar.png", 'rb').read())


background = html.Div([
    html.H2('Background'),
    html.P(children=[intro1,intro2_1,intro2_2,intro2_3,intro3]),
    html.Br(),
    html.P(parp1),
    html.Figure(id="plot_parp_workflow",children = [
        html.Img(src='data:image/png;base64,{}'.format(plot_parp_workflow.decode()),style={"width":"80%","height":"80%"}),
        html.Figcaption("Figure 1: The PARP Project Workflow",style={"text-align":"center"})],
        style={"text-align":"center","display":"block"}),    
    html.P(children=[parp2_1,parp2_2,parp2_3]),
    html.Figure(id="plot_parp_str",children = [
        html.Img(src='data:image/png;base64,{}'.format(plot_parp_str.decode())),
        html.Figcaption("Figure 2: The PARP Model",style={"text-align":"center"})],
        style={"text-align":"center","display":"block"}),  
    html.P([parp3,parp4]),
    html.Figure(id="plot_parp_acc",children = [
        html.Img(src='data:image/png;base64,{}'.format(plot_parp_acc.decode())),
        html.Figcaption("Figure 3: The weighted test prediction accuracy of \
            PARP and other Machine Learning models",style={"text-align":"center"})],
        style={"text-align":"center","display":"block"})
    ],
    style=CONTENT_STYLE)

