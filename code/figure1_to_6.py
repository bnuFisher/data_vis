#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly.plotly as py
py.sign_in('your name', 'your api-key')
import plotly.graph_objs as go

trace1 = go.Bar(
    x = [1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,
         1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,
         1990,1991,1992,1994,1995,1996,1997,1998,1999,
         2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
         2010,2011,2012,2013,2014,2015,],
    y = [651,470,494,473,580,740,923,1319,1526,2661,2663,
         2585,2545,2870,3494,2915,2860,3184,3721,4322,3887,
         4683,5073,3458,3081,3056,3200,933,1396,1813,1908,
         1332,1262,1161,2011,2751,3241,4787,4721,4821,5067,
         8498,11990,16840,14806,156898,],
    name = 'terrorist attack',
    marker =dict(color='rgb(55,88,109')
)

data1 = [trace1]

layout1 = go.Layout(
    title = 'Figure 1 - Distribution of Terrorist Attacks (1970-2015)',
    xaxis = dict(
            autotick=False,
            tick0=1970,
            dtick=1,
            tickangle=-45,
            tickwidth=2,
            tickfont=dict(
                size=14,
                color='rgb(107,107,107)',
        )
    ),

    yaxis = dict(
        title = 'Times per Year',
        titlefont =dict(
            size = 16,
            color = 'rgb(107,107,107)'
        ),
        tickfont = dict(
            size = 14,
            color = 'rgb(107,107,107)'
        )
    ),
    legend = dict(
        x = 0,
        y = 1.0,
        bgcolor = 'rgba(255,255,255,0)',
        bordercolor = 'rgba(255,255,255,0)'
    ),

    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)

# fig = go.Figure(data=data1,layout = layout1)
# py.plot(fig,filename='years')

trace2 = go.Bar(
	x = ['Jan.','Feb.','Mar','Apr.','May','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.'],

	y = [12878,11824,13138,13090,14423,13107,
		14117,13644,12200,13591,12968,11769,],

	name = 'terrorist attack: months',
	marker =dict(color='rgb(128,128,128')
)

data2 = [trace2]

layout2 = go.Layout(
	title = 'Figure 2 - Distribution of Terrorist Attacks ( Jan.-Dec. )',
    xaxis = dict(
        autotick=False,
        tick0=1,
        dtick=1,
        # tickangle=-45,
        tickwidth=2,
        tickfont=dict(
            size=14,
            color='rgb(107,107,107)',
    )
),

    yaxis = dict(
        title = 'Times per Month',
        titlefont =dict(
            size = 16,
            color = 'rgb(107,107,107)'
        ),
        tickfont = dict(
            size = 14,
            color = 'rgb(107,107,107)'
        )
    ),
    legend = dict(
        x = 0,
        y = 1.0,
        bgcolor = 'rgba(255,255,255,0)',
        bordercolor = 'rgba(255,255,255,0)'
    ),
)

# fig = go.Figure(data=data2,layout = layout2)
# py.plot(fig,filename='months')

trace3 = go.Scatter(
	x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],

	y = [5540,5193,5202,5334,5005,4956,5150,5043,5247,5294,5155,5171,5246,5251,5571,5319,5107,5036,5133,5132,4894,5037,4981,4944,5021,5021,5109,5164,4700,4308,2614],

	name = 'terrorist attack: days',
	marker =dict(color='rgb(192,37,37')
)

data3 = [trace3]

layout3 = go.Layout(
	title = 'Figure 3 - Distribution of Terrorist Attacks ( 1st - 31st )',
    xaxis = dict(
        autotick=False,
        tick0=1,
        dtick=1,
        tickangle=-30,
        tickwidth=4,
        tickfont=dict(
            size=14,
            color='rgb(107,107,107)',
    )
),

    yaxis = dict(
        title = 'Times per Day',
        titlefont =dict(
            size = 16,
            color = 'rgb(107,107,107)'
        ),
        tickfont = dict(
            size = 14,
            color = 'rgb(107,107,107)'
        )
    ),
    legend = dict(
        x = 0,
        y = 1.0,
        bgcolor = 'rgba(255,255,255,0)',
        bordercolor = 'rgba(255,255,255,0)'
    ),
)

# fig = go.Figure(data=data3,layout = layout3)
# py.plot(fig,filename='days')

regions=['North America',
'Central America & Caribbean',
'South America',
'East Asia',
'Southeast Asia',
'South Asia',
'Central Asia',
'Western Europe',
'Eastern Europe',
'Middle East & North Africa',
'Sub-Saharan Africa',
'Australasia & Oceania',
]

trace1 = go.Bar(
    x = regions,
    y = [8.88,8.97,7.51,6.14,7.07,8.70,5.58,9.31,8.22,7.88,7.91,9.35,],
    name = 'Jan',
)

trace2 = go.Bar(
    x = regions,
    y = [7.87,7.90,6.99,6.91,7.83,7.37,9.11,7.99,6.15,7.62,7.95,6.50,],
    name = 'Feb',
)

trace3 = go.Bar(
    x = regions,
    y = [9.52,8.32,8.35,9.97,9.05,7.50,9.67,8.98,6.89,8.78,8.70,6.10,],
    name = 'Mar',
)

trace4 = go.Bar(
    x = regions,
    y = [9.58,7.63,7.47,7.16,8.53,9.01,5.95,8.22,7.71,8.27,8.69,4.47,],
    name = 'Apr',
)

trace5 = go.Bar(
    x = regions,
    y = [10.47,10.39,9.30,8.82,10.13,9.66,8.55,8.99,7.97,8.34,9.18,7.72,],
    name = 'May',
)

trace6 = go.Bar(
    x = regions,
    y = [7.69,6.75,8.44,7.67,8.63,8.87,8.36,8.25,8.87,8.26,8.31,8.54,],
    name = 'Jun',
)

trace7 = go.Bar(
    x = regions,
    y = [8.02,8.00,9.26,15.60,8.04,8.67,11.52,8.52,12.39,9.19,9.74,5.69,],
    name = 'Jul',
)

trace8 = go.Bar(
    x= regions,
    y = [7.75,8.26,8.85,6.78,9.17,8.69,9.29,7.95,11.20,9.13,7.53,8.94,],
    name = 'Aug',
)

trace9 = go.Bar(
    x = regions,
    y = [7.04,7.65,8.88,7.29,7.55,7.94,9.48,7.22,7.03,7.66,7.50,10.98,],
    name = 'Sep',
)

trace10 = go.Bar(
    x = regions,
    y = [8.79,9.82,9.52,7.29,9.00,7.93,7.81,8.55,8.89,8.80,8.17,10.98,],
    name = 'Oct',
)

trace11 =go.Bar(
    x = regions,
    y = [6.89,8.62,8.30,9.72,8.01,8.29,8.18,7.52,8.79,8.46,8.51,9.35,],
    name = 'Nov',
)

trace12 = go.Bar(
    x = regions,
    y = [7.50,7.67,7.12,6.65,6.99,7.38,6.51,8.50,5.89,7.60,7.83,11.38,],
    name = 'Dec',
)

data = [trace12,trace11,trace10,trace9,trace8,trace7,trace6,trace5,trace4,trace3,trace2,trace1]

layout = go.Layout(
    title = 'Figure 4 - Distribution of Terrorist Attacks ( Jan - Dec ) -- by Regions',
    xaxis = dict(tickangle = 15),
    yaxis = dict(title = 'Percents',ticksuffix = '%',),
    barmode ='stack',

)

# fig = go.Figure(data=data, layout=layout)
# py.plot(fig,filename='stack_chart')

days= ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

trace4 = go.Bar(
	x =days,
	y = [24114,23302,23429,22716,20703,20273,21529],
	name = 'Total',
    # mode = 'markers',
	marker =dict(color='rgb(192,137,37')
)

trace5 = go.Scatter(
	x = days,
	y = [6134,6064,6274,5858,4766,5248,5961],
	name = 'Middle East & North Africa',
    mode = 'lines+markers',
    # line = dict(dash = 'dash')
	)

trace6 = go.Scatter(
	x = days,
	y = [5792,5525,5474,5219,4880,5479,5435],
	name = 'South Asia',
    mode = 'lines+markers'
	)

trace7 = go.Scatter(
	x = days,
	y = [2808,2884,2983,2887,2758,1986,2202],
	name = 'South America',
    mode = 'lines',
    # line = dict(dash = 'dot')
	)

trace8 = go.Scatter(
	x = days,
	y = [2386,2142,2236,2407,2370,2316,1982],
	name = 'Western Europe',
    mode = 'lines'
	)

data_multi = [trace5,trace6,trace7,trace8]

data4 = [trace4]

layout4 = go.Layout(
	title = 'Figure 5 - Distribution of Terrorist Attacks ( Mon - Sun )',
    xaxis = dict(
        autotick=False,
        # tick0=1,
        # dtick=1,
        # tickangle=-45,
        tickwidth=5,
        tickfont=dict(
            size=14,
            color='rgb(107,107,107)',
    )
),

    yaxis = dict(
        title = 'Times per Day',
        titlefont =dict(
            size = 16,
            color = 'rgb(107,107,107)'
        ),
        tickfont = dict(
            size = 14,
            color = 'rgb(107,107,107)'
        )
    ),
    legend = dict(
        x = 0,
        y = 1.4,
        bgcolor = 'rgba(255,255,255,0)',
        bordercolor = 'rgba(255,255,255,0)'
    ),

    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)

layout5 = go.Layout(
	title = 'Figure 6 - Distribution of Terrorist Attacks ( Mon - Sun ) -- by Regions',
    xaxis = dict(
        autotick=False,
        # tick0=1,
        # dtick=1,
        # tickangle=-45,
        tickwidth=5,
        tickfont=dict(
            size=14,
            color='rgb(107,107,107)',
    )
),
    yaxis = dict(
        title = 'Times per Day',
        titlefont =dict(
            size = 16,
            color = 'rgb(107,107,107)'
        ),
        tickfont = dict(
            size = 14,
            color = 'rgb(107,107,107)'
        )
    ),
    legend = dict(
        x = 0,
        y = 1.2,
        bgcolor = 'rgba(255,255,255,0)',
        bordercolor = 'rgba(255,255,255,0)'
    ),
    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)

# fig = go.Figure(data=data4,layout = layout4)
# py.plot(fig,filename='Mon-Sun')

# fig = go.Figure(data=data_multi,layout = layout5)
# py.plot(fig,filename='Mon-Sun-by-regions')