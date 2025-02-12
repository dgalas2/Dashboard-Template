import random
from datetime import datetime, timedelta
import plotly.graph_objects as go

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
