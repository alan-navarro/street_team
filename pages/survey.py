import dash
from dash import Dash, dcc, html, Input, Output, callback
from datetime import datetime as dt 
import datetime
import plotly.express as px
from app_framework.commit_db.write_user import WriteUser
from app_framework.models.users_survey import UsersSurvey


dash.register_page(__name__)

layout = html.Div([
html.Div(
    [
        html.I("Type your user name and press Enter, then vote!"),
        html.Br(),
        dcc.Input(id="input_1", type="text", placeholder=None, debounce=True, persistence=False),
        html.Br(),
        html.I("So far, what do you think is the factor that affects the most the climate?"),
        html.Br(),
        dcc.Dropdown(id="factor-dropdown",
           options=[
               {'label': '-', 'value': 0},
               {'label': 'Population', 'value': 1},
               {'label': 'GHG emissions', 'value': 2},
               {'label': 'Power production', 'value': 3},
               {'label': 'Increase of agricultural land', 'value': 4},
               {'label': 'Decrease of forest land', 'value': 5},
           ],
           placeholder="Choose a factor...",
           persistence=False
),
        html.Br(),
    ]
),
    
    html.Div([html.H1('', style={"textAlign": "center", "color": "#007F94", 'fontWeight': 'bold'}),
    html.Div([dcc.Loading(children=[dcc.Graph(id="pie_chart")])],)
    ]),
    ]) 


@callback(
    Output("pie_chart", "figure"),
    Output("input_1", "value"),
    Input('input_1', 'value'),
    Input('factor-dropdown', 'value'))

def create_chart(input_value, dropdown_value):
    WriteUser().committing_data(input_value, dropdown_value)

    pie_df = UsersSurvey().make_query()
    print(pie_df)

    users_preferences = px.pie(pie_df, values='selection', names='legend')
    input_value = None
    
    return users_preferences, input_value