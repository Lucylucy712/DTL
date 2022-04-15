from imports import * 
from style import * 
abstract = "With the development of the whole-genome bacterial sequences technology, \
    it becomes possible to predict antibiotic resistance using sample’s gene orthology and deep neural networks. \
    However, it is difficult to collect adequate samples for model training due to the expense of data acquisition for each task. \
    To overcome this limitation, we proposed a double-sided network-based deep transfer learning from source task to target task. \
    This approach is capable of learning from target domain, as well as transferring the pre-trained neural network from the source domain to the target domain.\
    Compared to other commonly used machine learning models, we demonstrated that this approach outperforms in terms of XX (metric name), which could achieve XX%.\
    We anticipate that this approach could be helpful for antibiotic resistance prediction modeling."

siteguide = "We develop this website to summarize our DTL model and show the results interactively with structure below."


homepage = html.Div([
    html.H1('DTL: A Double-sided Transfer Learning Network for Antibiotic Resistance Prediction'),
    html.H2("Welcome to our DTL project!",style={"color":"rgb(12, 117, 49)"}),
    html.Br(),
    html.Div([
        html.P("Abstract",style={"font-size":"120%"}),
        html.P(abstract),
        html.P(children = [
            html.P(siteguide,style={"font-size":"120%"}),
            html.Ul(id='my-list',children=[
                html.Li(children=[html.B("Project:",style={"display":"inline-block"}),
                                    html.P("The overall project introduction, research motivation, and model description",style={"display":"inline-block"})]),
                html.Li(children = [html.B("Results:",style={"display":"inline-block"}),
                                    html.P("The result evaluation table and interactively plots",style={"display":"inline-block"})]),
                html.Li(children = [html.B("Download:",style={"display":"inline-block"}),
                                    html.P("The downloadbale data and sources",style={"display":"inline-block"})])])
            ])
        ])
],style=CONTENT_STYLE)