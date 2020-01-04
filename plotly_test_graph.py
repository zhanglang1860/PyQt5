import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_excel(r'C:\Users\Administrator\Desktop\test.xlsx')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=0,
        max=8,
        value=2,
        marks={list(df['人员'].unique()).index(year): str(year) for year in df['人员'].unique()},
        step=None

    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):

    traces = []
    # for selected_year in range(0, len(df['人员'].unique())):

    filtered_df = df[ df['人员']== df['人员'].unique()[selected_year]]
    print(filtered_df.shape[0])
    traces.append(dict(
        y=filtered_df['项目名'],
        # x=filtered_df['装机容量'],
        x=filtered_df['完成比例']*100,
        text=filtered_df['项目名'],
        mode='markers',
        opacity=0.7,
        marker={
            'size': 15,
            'line': {'width': 0.5, 'color': 'white'},
            'color' : filtered_df['完成比例'],
            'colorscale':'Greens',
            'reversescale':True
        },
        type='bar',
        orientation = 'h',


        name=selected_year
    ))
    print(traces)
    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'Linear', 'title': 'Progress',
                   'range':[0, 100]},
            yaxis={'range': [0, filtered_df.shape[0]]},
            margin={'l': 300, 'b': 80, 't': 20, 'r': 20},
            # legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)