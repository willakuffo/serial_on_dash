
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px
from plotly import graph_objs as go
from dash.dependencies import Output,Input
import pandas as pd
import numpy as np
from serialcom import serialstream


S = serialstream()

app = dash.Dash(__name__)

app.layout = html.Div( children = [

		html.H1('UAV data monitor',style  = dict(textAlign = 'center')),
		html.Div(children = [html.H1(id = 'orientation',style = dict(texAlign = 'center'))]),
		dcc.Interval(id ='orientation update',interval = 500,n_intervals = 0)
]

)

@app.callback(Output('orientation','children'),[Input('orientation update','n_intervals')])
def update_orientation_graph(n):
	data = S.serialread()
	if data is not None:
		return data.decode()

if __name__ == '__main__':
	app.run_server('192.168.43.136',debug = True,use_reloader = False)
