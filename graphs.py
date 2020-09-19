# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Internal modules
from config import config


def choropleth(geojson, location_id, variable, label):
    
    data = go.Choroplethmapbox(
        geojson = geojson,
        locations = location_id,
        z = variable,
        text = label,
        colorscale = 'reds',
        #colorbar = {'thickness':20, 'ticklen':3},
        showscale = False,
        marker_line_width=0.5, 
        marker_opacity=0.5
        
    )
    
    layout = go.Layout(
        title_text = '',
        autosize = True,
        #height = 250,
        #width = 350,
        margin = {'l': 0, 'r': 0, 'b': 0, 't': 0},
        mapbox = {'center': {'lat':33.677, 'lon':65.21600},
                 'accesstoken': config.MAPBOX_TOKEN,
                 'zoom':5,
                 'style': 'dark'}
    )
    
    fig = go.Figure(data=data, layout=layout)

    return fig

# choropleth(geojsdata, gdf['ID_1'], gdf['ID_1'])


def linechart(x):
    data = [
        go.Scatter(
            x = x.value_counts().sort_index().index,
            y = x.value_counts().sort_index().values,
            
            line = {'color': '#97151c'},
            mode = 'lines',
            #name = 'set a name for me'
        )
    ]
    
    layout = go.Layout(
        template = 'plotly_white',
        autosize = True,
        title = '',
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 350,
        #width = 340,
        hovermode = 'closest',
        legend = {
            'x': -0.0277108433735,
            'y': -0.142606516291,
            'orientation': 'h'
        },
        margin = {
            'r': 20,
            't': 20,
            'b': 20,
            'l': 50
        },
        showlegend = False,
    xaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        #'nticks': 4,
        'showgrid': True,
        'showline': True,
        #'ticklen': 5,
        'ticks': 'outside',
        #'title': 'Label me!',
        #'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    }
    )
    
    yaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        'nticks': 4,
        'showgrid': True,
        'showline': True,
        'ticklen': 5,
        'ticks': 'outside',
        'title': 'Label me!',
        #'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    }
    
    fig = go.Figure(data=data, layout=layout)
    

    return fig