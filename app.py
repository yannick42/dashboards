from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import uuid
import kagglehub

# Download latest version
path = kagglehub.dataset_download("hellbuoy/car-price-prediction")
#print("Path to dataset files:", path) # ~/.cache/kagglehub/datasets/hellbuoy/car-price-prediction/versions/1
df = pd.read_csv(path + '/CarPrice_Assignment.csv')

app = Dash()

def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div([
        html.H1(children='Multiple Linear Regression', style={'textAlign':'center'}),
        dcc.Dropdown(['gas', 'diesel'], 'gas', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        
    ])

app.layout = serve_layout()

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.fueltype==value]
    return px.line(dff, x='CarName', y='price')

if __name__ == '__main__':
    app.run(debug=True)
