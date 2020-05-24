#!/usr/bin/env python3

import pandas
import plotly.express as px
import plotly

df = pandas.read_csv('kw-test-data.csv')

fig = px.line(df, x = 'timestamp', y = 'pagespeed', title='Kwiat.com Homepage Page Speed Over Time')
# fig.show()

plotly.offline.plot(fig, filename='test-kwplot.html')