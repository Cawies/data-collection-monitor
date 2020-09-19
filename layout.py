# External libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_table

# Internal modules
from config import config
from processing.data_management import load_dataset, fetch_data_from_api
import graphs as graphs


def create_header(app):
    return html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("logo.png"),
                            id="plotly-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
                    ],
                    className="one-third column",
               ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    'Title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Overview", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Download data", id="learn-more-button"),
                            href="link/to/data",

                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        )


def map_and_four_boxes(app):
        return html.Div(
            [
                html.Div(
                        dcc.Graph(id = 'map',figure = None, className="dcc_control"),

                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="tot_interviews"), html.P("Total interviews"), html.H4('1')],
                                    id="box-1",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="duplicated_id"), html.P("Duplicated ID"), html.H4('2')],
                                    id="box-2",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="end_before_start"), html.P("Total flags"), html.H4('3')],
                                    id="box-3",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="avg_interview_duration"), html.P("Avg. interview duration (min)"), html.H4('4')],
                                    id="water",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            children = [

                            dcc.Graph(id="interview-count", figure=None)],
                            className="pretty_container"
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        )