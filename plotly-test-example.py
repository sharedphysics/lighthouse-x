#!/usr/bin/env python3

import pandas
import plotly.express as px
import plotly

df = pandas.read_csv('metrics-test.csv')

fig = px.line(df, x = 'timestamp', y = 'firstContentfulPaint', title='First Contentful Paint Over Time')
# fig.show()

plotly.offline.plot(fig, filename='test-plot.html')