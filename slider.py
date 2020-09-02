import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import chart_studio.plotly as py
import chart_studio
chart_studio.tools.set_credentials_file(
    username='zhanglang86', # 这儿就不放我自己的账号和api了
    api_key='MxJLQuDBGkAVEZI7f2J0'
    )
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = pd.read_excel(r'D:\onedrive_data\OneDrive - Platinum\gapminder2007.xlsx')

fig = go.Figure(go.Scatter(x=df['gdpPercap'], y=df['lifeExp'], text=df.country, mode='markers', name='2007'))
fig.update_xaxes(title_text='GDP per Capita', type='log')
fig.update_yaxes(title_text='Life Expectancy')

# pio.write_html(fig, file='hello_world.html', auto_open=True)
py.plot(fig, filename='pandas-multiple-scatter')


# import chart_studio
# chart_studio.tools.set_credentials_file(
#     username='', # 这儿就不放我自己的账号和api了
#     api_key=''
#     )
# import chart_studio.plotly as py
# from plotly.graph_objects import Scatter
# trace0 = Scatter(
#     x = [1, 2, 3, 4],
#     y = [10, 15, 13, 17]
# )
# trace1 = Scatter(
#     x = [1, 2, 3, 4],
#     y = [16, 5, 11, 9]
# )
# data = ([trace0, trace1])
# py.plot(data, filename='first_start')