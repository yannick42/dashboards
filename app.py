from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import uuid
import kagglehub
from scipy.stats import shapiro

# Download latest version
path = kagglehub.dataset_download("hellbuoy/car-price-prediction")
#print("Path to dataset files:", path) # ~/.cache/kagglehub/datasets/hellbuoy/car-price-prediction/versions/1
df = pd.read_csv(path + '/CarPrice_Assignment.csv')

app = Dash()

def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div([
        html.H1(children='Multiple Linear Regression', style={'textAlign':'center'}),
        dcc.Dropdown(df.columns, 'CarName', id='dropdown-selection'),
        dcc.Dropdown(df.columns, 'price', id='dropdown-selection-2'),
        dcc.Graph(id='graph-content'),
        html.H2(children='Normality test', style={'textAlign':'left'}),
        dcc.Dropdown(df.select_dtypes(exclude=['object']).columns, 'price', id='dropdown-selection-for-normality'),
        dcc.Markdown(
            children='''
            ### Shapiro-Wilk's test of normality

            It's a statistical test proposed in ***<green>1965</green>***.

            $W=\dfrac{(\sum\limits_{i=1}^n a_i x_{(i)})^2}{\sum\limits_{i=1}^n (x_i - \overline{x})^2}$

            see [Wikipedia](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test) for more details
            ''',
            mathjax=True,
            dangerously_allow_html=True, # to make <u></u> work ?
            link_target="_blank"
        ),
        html.Br(),
        html.Div(children=[
            html.Span(id='shapiro-wilk-stat', style={'color': 'red', 'fontWeight': 'bold'}),
            html.Span(', '),
            html.Span(id='shapiro-wilk-p-value', style={'color': 'red', 'fontWeight': 'bold'}),
        ]),
    ])

app.layout = serve_layout()


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('dropdown-selection-2', 'value')
)
def update_graph(value, value2):
    dff = df.sort_values(by=['price'])
    return px.scatter(dff, x=value, y=value2)

@callback(
    Output('shapiro-wilk-stat', 'children'),
    Output('shapiro-wilk-p-value', 'children'),
    Input('dropdown-selection-for-normality', 'value')
)
def update_shapiro_wilk(value):
    sample = df[[value]]
    statistics, p_value = shapiro(sample)

    return f"W={statistics:.3f}", f"p-value={p_value:.4f}"

if __name__ == '__main__':
    app.run(debug=True)
