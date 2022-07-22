import pandas as pd
import numpy as np
import dash
from dash import Dash, dcc, html, Input, Output, callback
from datetime import datetime as dt 
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go
import plotly.express as px
from pages.write_user import WriteUser
from pages.pie_df import MakeDF
# from write_user import WriteUser
# from pie_df import MakeDF

dash.register_page(__name__)

bp = "\n"*3

# app = dash.Dash(suppress_callback_exceptions=True)

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
    
    html.Div([html.H1("Breakdown of survey users' response", style={"textAlign": "center", "color": "#007F94", 'fontWeight': 'bold'}),
    html.Div([dcc.Loading(children=[dcc.Graph(id="pie_chart")])],)
    ]),
    ]) 


@callback(Output("pie_chart", "figure"), 
Input('input_1', 'value'),
Input('factor-dropdown', 'value'))

def create_chart(input_value, dropdown_value):
    WriteUser().committing_data(input_value, dropdown_value)

    pie_df = MakeDF().making_df()

    users_preferences = px.pie(pie_df, values='selection', names='legend')

    return users_preferences

# if __name__ == '__main__':
#     app.run_server(debug=True)