# External libraries
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_table
import io
import flask
import json
import requests

# Internal modules
from config import config
from processing.data_management import load_dataset, fetch_data_from_api



app = dash.Dash(
	__name__, meta_tags=[
		{
			'name': 'viewport', 
			'content': 'width=device-width'
		}
	]
)

server = app.server


def serve_layout():
	df = load_dataset(file_name=config.DATA_FILE)

	return html.Div(
		[
			dcc.Store(id="json_storage")
			html.Div(id='output-clientside') # Empty div to trigger clientside javascript
			create_header(app, df)
		]
	)


if __name__ == "__main__":
	app.run_server(host='0.0.0.0', port=8050, debug=False)
