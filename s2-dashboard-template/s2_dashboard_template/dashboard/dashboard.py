from dash import Dash, dcc, html
import os
from graph.graph import getFigure

'''
Provide your Dashboard app using this function
'''
def getDashboardApp():
	fig = getFigure()
	dash_base_path = os.environ['SINGLESTOREDB_APP_BASE_PATH']
	app = Dash(requests_pathname_prefix=dash_base_path)
	app.layout = html.Div([
		dcc.Graph(figure=fig)
	])
	return app
