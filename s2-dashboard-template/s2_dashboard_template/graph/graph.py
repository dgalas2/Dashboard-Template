import random
from datetime import datetime, timedelta
import plotly.graph_objects as go
from s2_dashboard_template.db import database
import os
from dotenv import load_dotenv
load_dotenv(".env")
env = os.environ.get('ENV')

connection_url = database.getConnectionString(env)
# db = database.DB(connection_url)	

def getFigure():
	start_date = datetime(2023, 1, 1)
	dates = [start_date + timedelta(days=i) for i in range(100)]
	values = [random.randint(2000, 3000) for _ in range(100)]
	fig = go.Figure(go.Scatter(x=dates, y=values, mode='lines+markers'))
	fig.update_layout(
		xaxis=dict(title='Dates'),
		yaxis=dict(title='Active Cases'),
		title='Active Covid Cases in 2023')
	return fig
