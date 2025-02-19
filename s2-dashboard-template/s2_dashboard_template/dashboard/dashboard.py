from dash import Dash, dcc, html
import os
from s2_dashboard_template.graph.graph import getFigure
from dotenv import load_dotenv
load_dotenv(".env")
env = os.environ.get('ENV')
if env == None:
	env = ""

def getVariableName(env,name):
	if env=="":
		return name
	else:
		return f'{env}_{name}'
	


'''
Provide your Dashboard app using this function
'''
def getDashboardApp():
	fig = getFigure()
	dash_base_path = os.environ.get(getVariableName(env,'BASE_PATH'))
	app = Dash(requests_pathname_prefix=dash_base_path)
	app.layout = html.Div([
		dcc.Graph(figure=fig)
	])
	return app
