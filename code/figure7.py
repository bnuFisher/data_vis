#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly.plotly as py
py.sign_in('your name', 'your api-key')
import plotly.graph_objs as go

latitudes = ["S 40+","S 31-40","S 21-30","S 11-20","S 1-10","N 0-10","N 11-20","N 21-30","N 31-40","N 41-50","N 51-60","N 60+"]

regions = ["Western Europe","Sub-Saharan Africa","Middle East & North Africa","Eastern Europe",
			"South Asia","Central Asia","Southeast Asia","East Asia","Australasia & Oceania",
			"North America","Central America & Caribbean","South America"]

data = [
	go.Heatmap(
		colorscale='Viridis',
		x=regions,
		y = latitudes,
		z= [[0,0,0,0,0,0,0,0,16,0,0,29,],
		   [0,365,0,0,0,0,0,0,77,0,0,3033,],
		   [0,1752,0,0,0,0,0,0,37,0,0,373,],
		   [0,599,0,0,2,0,0,0,30,0,0,5395,],
		   [0,1469,0,0,0,0,469,0,83,0,0,884,],
		   [0,5662,0,0,2933,0,6519,0,0,0,191,7722,],
		   [0,3073,2637,0,1690,0,2700,1,0,609,9032,348,],
		   [41,11,1544,0,13663,11,119,157,0,301,34,0,],
		   [2125,0,34283,43,19079,227,1,519,0,1163,0,0,],
		   [7263,0,1110,4391,0,280,0,100,0,1169,0,0,],
		   [6418,0,0,424,0,6,0,0,0,17,0,0,],
		   [15,0,0,8,0,0,0,0,0,1,0,0,]]
		   	 )
		]

layout = go.Layout(
	title = 'Figure 7 - A Heatmap of Terrorist Attacks:  Latitudes & Regions',
	xaxis = dict(
		   tickangle=15,
		   tickwidth=3,
		   )
)

fig = go.Figure(data = data,layout=layout)
py.plot(fig,filename='heatmap')