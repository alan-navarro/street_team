import dash
from dash import html 
from dash import dcc 
from datetime import datetime as dt 
from dash.dependencies import Input, Output
import datetime
import plotly.express as px
from apps.models.save_data.write_user import WriteUser
from apps.models.data_processing.pie_df import MakeDF
from app import app

bp = "\n"*3

layout = html.Div([
html.Div(
    [
        html.I("Type your user name and press Enter, then vote!"),
        html.Br(),
        dcc.Input(id="input_1", type="text", placeholder=None, debounce=True),
        html.Br(),
        html.I("So far, what do you think is the factor that affects the most the climate?"),
        html.Br(),
        dcc.Dropdown(id="factor-dropdown",
           options=[
               {'label': 'Population', 'value': 1},
               {'label': 'GHG emissions', 'value': 2},
               {'label': 'Power production', 'value': 3},
               {'label': 'Increase of agricultural land', 'value': 4},
               {'label': 'Decrease of forest land', 'value': 5},
           ],
           placeholder="Choose a factor...",
),
        html.Br(),
    ]
),
    
    html.Div([html.H1('', style={"textAlign": "center", "color": "#007F94", 'fontWeight': 'bold'}),
    html.Div([dcc.Loading(children=[dcc.Graph(id="pie_chart")])],)
    ]),
    ]) 


@app.callback(
    dash.dependencies.Output("pie_chart", "figure"),
    [dash.dependencies.Input('input_1', 'value'),
    dash.dependencies.Input('factor-dropdown', 'value')])

def create_chart(input_value, dropdown_value):
    WriteUser().committing_data(input_value, dropdown_value)

    pie_df = MakeDF().making_df()

    users_preferences = px.pie(pie_df, values='selection', names='legend')

    return users_preferences