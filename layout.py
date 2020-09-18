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
                                    config.DASHBOARD_TITLE,
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
