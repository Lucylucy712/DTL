from imports import * 
from style import * 
sidebar = html.Div(
    [
        html.H2(dbc.NavLink("DTL", href="/", active="exact",external_link=True), className="display-4",style={"test-align":"center"}),
        html.Hr(),
        html.P("A modified Transfer Learning Model", className="lead"),
        dbc.Nav(children=
            [dbc.NavItem(children=[
                dbc.Accordion( children = [
                    dbc.AccordionItem(
                            [
                              dbc.NavLink("Background", href="/project/background", active="exact",external_link=True),
                              dbc.NavLink("Motivation",href = "/project/motivation",active = "exact",external_link=True),
                              dbc.NavLink("Model",href = "/project/model",active = "exact",external_link=True), 
                            ],title="Project"),
                    dbc.AccordionItem(
                            [
                              dbc.NavLink("Evaluation", href="/results/evaluation", active="exact",external_link=True),
                              dbc.NavLink("Plot",href = "/results/plot",active = "exact",external_link=True)
                            ],title="Results"),
                    dbc.AccordionItem(
                            [
                            dbc.NavLink("download",href="/download",active="exact",external_link=True)
                            ],title = "Download")],start_collapsed=True)])],vertical=True,pills=True)
    ],
    style=SIDEBAR_STYLE,
)
