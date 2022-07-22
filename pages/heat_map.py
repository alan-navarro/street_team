import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output, callback
import datetime
from dateutil.relativedelta import relativedelta
from dash import dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from pages.global_warming import AnalizeFactors
# from global_warming import AnalizeFactors
from dash import dash_table
from dash.dash_table.Format import Format
from dash.dash_table.Format import Group
dash.register_page(__name__)

# from app import app
# import random
bp = "\n"*3

empty_data = {
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"],
              '-': ["-"]}
empty_df = pd.DataFrame(empty_data)

past_month = relativedelta(months=1)
current_date = datetime.date.today()
starting_date = current_date - past_month

# app = dash.Dash(suppress_callback_exceptions=True)


layout = html.Div([
    html.Div([html.H1('Factors correlation map', style={"textAlign": "center", "color": "#007F94", 'fontWeight': 'bold'}),

    dcc.Dropdown(id="year-dropdown",
   options=[
       {'label': '2010', 'value': 2010},
       {'label': '2011', 'value': 2011},
       {'label': '2012', 'value': 2012},
       {'label': '2013', 'value': 2013},
   ],
   value=2010,
   placeholder="Select a year...",
),
    html.Div([dcc.Loading(children=[dcc.Graph(id="heat_map")])]),

    ])
    ]) 


@callback(
       Output('heat_map', 'figure'), 
       Input('year-dropdown', 'value'))

def create_heatmap(selected_year):
    start_date = str(selected_year) + '-01-01'
    end_date = str(selected_year) + '-12-31'

    Analize_Factors = AnalizeFactors().get_data(start_date, end_date)

    correlations_top10 =Analize_Factors["correlations_top10"]

    heatmap = px.imshow(correlations_top10, color_continuous_scale=px.colors.diverging.Tealrose,
    x=['Temperature', 'Population', 'CO2 (kt)', 'KWh use per capita', 'Agricultural land (km2)', 'Forest land (km2)'],
    y=['Temperature', 'Population', 'CO2 (kt)', 'KWh use per capita', 'Agricultural land (km2)', 'Forest land (km2)'],)

    return heatmap

# if __name__ == '__main__':
#     app.run_server(debug=True)