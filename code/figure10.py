#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly.plotly as py
from plotly.grid_objs import Grid,Column
from plotly.tools import FigureFactory as FF
py.sign_in('your name', 'your api-key')
import pandas as pd
import time

url='https://raw.githubusercontent.com/bnuFisher/data_vis/master/data/slide.csv'

dataset = pd.read_csv(url)

years_from_col = set(dataset['year'])
years_ints = sorted(list(years_from_col))
years = [str(year) for year in years_ints]

countrys = []

for country in dataset['country']:
    if country not in countrys:
        countrys.append(country)

columns = []
#make grids

for year in years:
    for country in countrys:
        dataset_by_year = dataset[dataset['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['country'] == country]
        for col_name in dataset_by_year_and_cont:
            column_name = '{year}_{country}_{header}_gapminder_grid'.format(
                year = year, country=country, header=col_name
            )
            a_column = Column(list(dataset_by_year_and_cont[col_name]),column_name)
            columns.append(a_column)

#upload

grid = Grid(columns)
url = py.grid_ops.upload(grid, 'gapminder_grid'+str(time.time()), auto_open=False)
# url

figure = {
    'data':[],
    'layout':{},
    'frames':[],
    'config':{'scrollzoom':True}
}

figure['layout']['xaxis'] = {'range':[55,85],'title':'Life Expectancy at Birth','gridcolor':'#FFFFFF'}
figure['layout']['yaxis'] = {'title':'GDP per Capita (current US$)','type':'log','gridcolor':'#FFFFFF'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['plot_bgcolor'] = '#EFECEA'
figure['layout']['title'] = 'Figure 10 - Terrorist attacks with GDP per Capita and Life-Exp in 10 Countries (2005-2014)'


#add slider

figure['layout']['slider'] = {
    'args':[
        'slider.value', {
            # 'duration':400,
            'ease':'cubic-in-out'
        }
    ],
    'initiaValue':'2005',
    'plotlycommand':'animate',
    'values':years,
    'visible':True
}


figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition':{'duration': 300,
                         'easing':'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': True,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

custom_colors = {
    'Afghanistan':'rgb(255,65,54)',
    'Algeria':'rgb(133,20,75)',
    'Colombia':'rgb(21,10,242)',
    'India':'rgb(75,21,243)',
    'Iraq':'rgb(110,116,217)',
    'Israel':'rgb(123,190,207)',
    'Nepal':'rgb(17,12,89)',
    'Nigeria':'rgb(23,89,122)',
    'Pakistan':'rgb(103,203,12)',
    'Philippines':'rgb(45,54,12)',
    'Thailand':'rgb(121,121,90)',
}

col_name_template = '{year}_{country}_{header}_gapminder_grid'

year = 2005

for country in countrys:
    data_dict = {
        'xsrc':grid.get_column_reference(col_name_template.format(
            year=year, country=country,header='life'
        )),
        'ysrc': grid.get_column_reference(col_name_template.format(
            year=year, country=country,header='gdp'
        )),
        'mode':'markers',
        'textsrc':grid.get_column_reference(col_name_template.format(
            year =year, country=country,header='country'
        )),
        'marker':{
            'sizemode':'area',
            # 'sizeref':200000,
            'sizesrc':grid.get_column_reference(col_name_template.format(
                year= year,country=country,header='attacks'
            )),
         'color':custom_colors[country]
        },
        'name':country
    }
    figure['data'].append(data_dict)


for year in years:
    frame = {'data':[], 'name':str(year)}
    for country in countrys:
        data_dict = {
            'xsrc':grid.get_column_reference(col_name_template.format(
                year=year, country=country,header='life'
            )),
            'ysrc': grid.get_column_reference(col_name_template.format(
                year=year,country=country,header='gdp'
            )),
            'mode':'markers',
            'textsrc':grid.get_column_reference(col_name_template.format(
                year=year, country=country,header='country'
            )),
            'marker':{
                'sizemode':'area',
                # 'sizeref':200000,
                'sizesrc':grid.get_column_reference(col_name_template.format(
                    year=year,country=country,header='attacks'
                )),
                'color':custom_colors[country]
            },
            'name':country
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = { 'args':[
        [year],
        {'frame':{'duration':300,'redraw':False},
         'mode':'immediate',
         'transtion': {'duration':300}}
     ],
     'label':year,
     'method':'animate'}
    sliders_dict['steps'].append(slider_step)

figure['layout']['sliders'] = [sliders_dict]
py.create_animations(figure,'attacks_gap_life'+str(time.time()))