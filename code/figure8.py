#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly.plotly as py
py.sign_in('your name', 'your api-key')
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/bnuFisher/data_vis/master/data/maps.csv')

data =[dict(
     type = 'choropleth',
     locations = df['CODE'],
     z = df['DEATH'],
     text = df['COUNTRY'],
     colorscale = [[0,"rgb(5,48,97)"],
        [0.15265666689933938,"rgb(35,48,97)"],
        [0.20531333379867875,"rgb(33,102,172)"],
        [0.30531333379867875,"rgb(33,80,162)"],
        [0.4079700006980182,"rgb(97,137,195)"],
        [0.4579700006980182,"rgb(67,147,195)"],
        [0.5279700006980182,"rgb(67,127,225)"],
        [0.6006266675973575,"rgb(146,197,222)"],
        [0.7032833344966969,"rgb(209,229,240)"],
        [0.7577361120805807,"rgb(247,247,247)"],
        [0.8021888896644646,"rgb(244,165,130)"],
        [0.85066416672483484,"rgb(244,145,130)"],
        [0.9010944448322323,"rgb(214,96,77)"],
        [0.9555472224161161,"rgb(103,0,56)"],
        [1,"rgb(103,0,31)"]],
    autocolorscale = False,
    # reversecale = True,
    marker = dict(
        line = dict(
            color = 'rgb(180,180,180)',
            width = 0.5,
        )),
    colorbar = dict(
        title = 'Death Toll'),
)]

layout = dict(
    title = 'Figure 8 - Death Toll in Terrorist Attacks (1970-2015)',
    geo = dict(
        showframe=False,
        showcoastlines =True,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig =dict(data = data,layout=layout)
py.plot(fig,validata=False,filename='world_map')