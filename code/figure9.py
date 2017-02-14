#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import plotly.plotly as py
py.sign_in('your name', 'your api-key')
from plotly.graph_objs import *
import pickle

rows = pickle.load(open('bubble_db.pkl','rb')) 
#数据见 https://github.com/bnuFisher/data_vis/blob/master/data/bubble_db.pkl

df = pd.DataFrame( [ij for ij in i] for i in rows)

df.rename(columns={0:'Country',1:'Continent',
	2:'Attacks',3:'LifeExpectancy',4:'GDP'},inplace=True)

df = df.sort_values(by=['LifeExpectancy'],ascending=[1])

df.head()

country_names = df['Country']

sizemode = 'area'

sizeref = df['Attacks'].max()/1e2**1.8

colors = {
	'Asia':'rgb(255,65,54)',
	'Europe':'rgb(133,20,75)',
	'Africa':'rgb(0,116,217)',
	'North America':'rgb(255,133,27)',
	'Central America':'rgb(61,153,112)',
	'South America':'rgb(23,190,207)',
	'Oceania':'rgb(255,255,0)',
}

def make_text(X):
	return "Country: %s \
	 <br> Attacks:%s times \
	 <br> Life Expectancy:%s years" % (X['Country'],X['Attacks'],X['LifeExpectancy'])

def make_trace(X,Continent,sizes,color):
	return Scatter(
		x = X['GDP'],
		y = X['LifeExpectancy'],
		name = continent,
		mode ='markers',
		text = X.apply(make_text,axis=1).tolist(),
		marker = Marker(
			color = color,
			size = sizes,
			sizeref = sizeref,
			sizemode = sizemode,
			opacity = 0.4,
			line = Line(width=3,color='white')
			)
		)

data = Data()

for continent,X in df.groupby('Continent'):

	sizes = X['Attacks']
	color = colors[continent]

	data.append(
		make_trace(X,continent,sizes,color)
		)

title = 'Figure 9 - Terrorist Attacks with Life Expectancy and GDP per capita  (2014) -- A Bubble Chart'

x_title = 'GDP per capita (current US$)'
y_title = 'Life Expectancy at Birth'

axis_style = dict(
	type = 'log',
	zeroline = False,
	gridcolor = '#FFFFFF',
	ticks = 'outside',
	ticklen = 8,
	tickwidth = 1.5
)

layout = Layout(
	title = title,
	plot_bgcolor = '#EFECEA',
	hovermode = 'closest',
	xaxis = XAxis(
		axis_style,
		title = x_title,
		range = [2,5],
		),
	yaxis = YAxis(
		axis_style,
		title = y_title,
		)
	)

fig = Figure(data = data, layout=layout)
py.plot(fig,filename='bubble_chart')