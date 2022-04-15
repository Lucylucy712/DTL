from imports import * 
from style import * 
##### data table 
data_table_header = [
    html.Thead(html.Tr([html.Th(""),html.Th("Antibiogram"), html.Th("Shelburne")]))
]
row1 = html.Tr([html.Td("Sample Size"),html.Td("3,393"), html.Td("198")])
row2 = html.Tr([html.Td("Unique Bacteria Class"),html.Td("9"), html.Td("5")])
row3 = html.Tr([html.Td("Unique Antibiotic Class"),html.Td("29"), html.Td("10")])
row4 = html.Tr([html.Td("Unique Bacteria-Antibiotic Pair"), html.Td("93"),html.Td("30")])
row5 = html.Tr([html.Td("Training Data"), html.Td("29,187"),html.Td("1,224")])
row6 = html.Tr([html.Td("Unqiue Variants"), html.Td("14,615"),html.Td("5,785")])
data_table_body = [html.Tbody([row1, row2, row3, row4, row5, row6])]
data_table = dbc.Table(data_table_header + data_table_body,bordered=True,hover=True,responsive=True,striped=True)
########## Paragraph 1

data1 = "The PARP model keeps fixed in terms of model weights and input structure after the training process. \
    It indicates that we need to keep the input structure identical to the training data if we want to evalute\
    the model's performance on another dataset. "
data2 = "Considering the characteristics of different bacteria samples, the genetic variant domians may be much different \
    between the training dataset and the test one. "
data3 = "The table below compares the difference between the Antibiogram Data, \
    which is the training dataset of PARP model, and the Shelburne Data."

data4 = "Based on the table description, we could get the following conclusions: "

data51 = "The bacteria and antibiotic classes of Shelburne Data exist in those of the Antibiogram Data."
data52 = "The genetic variants are much different between the two datasets."

data5 = html.Ul(id='my-list',children=[
    html.Li(html.P(data51)),
    html.Li(html.P(data52)),
])

######## Paragraph 2 
data6 = "The venn plot of the unique variants from the Antibiogram and Shelburne Datasets are shown blow. We notice if we feed\
    the Shelburne Dataset directly to the PARP model, we need to discard 3,461 variants, around 59.8% of the whole set. Therefore,\
    it's reasonable to expect the performance would be not pretty good.\
    In other words, we meet a shit domain problem.\
    The target doamin (the Shelburne data) is much different from the source domain (the Antibiogram data).\
    One approach to solve the shift domain problem is to re-train the model from scratch using part of the new dataset and evaluate it \
    on the rest. However, due to the sample size limit, it would lead to over-fitting problem in the trianing process."

plot_venn = base64.b64encode(open("assets/Venn_Shel_Anti.png", 'rb').read())
data7 = html.Figure(id="plot_venn",children = [
    html.Img(src='data:image/png;base64,{}'.format(plot_venn.decode()),style={"width":"60%","height":"60%"}),
    html.Figcaption("Figure 4: The Venn diagram of variants",style={"text-align":"center"})],
    style={"text-align":"center","display":"block"})

###########

motivation = html.Div([
    html.H2("Problems of Interest"),
    html.P(children=[data1,data2,data3]),
    data_table,
    html.P(data4),
    data5,html.P(data6),data7],
    style=CONTENT_STYLE)


