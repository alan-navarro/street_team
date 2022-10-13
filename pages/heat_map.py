import pandas as pd
import dash
from dash import html 
from dash import dcc 
from datetime import datetime as dt 
from datetime import date
from dash import Dash, dcc, html, Input, Output, callback
import datetime
from dateutil.relativedelta import relativedelta
import plotly.express as px
from app_framework.models.climate_data_set import ClimateDataSet


dash.register_page(__name__)

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

    climate_dataset = ClimateDataSet().get_data(start_date, end_date)

    correlations_top10 =climate_dataset["correlations_top10"]

    heatmap = px.imshow(correlations_top10, color_continuous_scale=px.colors.diverging.Tealrose,
    x=['Temperature', 'Population', 'CO2 (kt)', 'KWh use per capita', 'Agricultural land (km2)', 'Forest land (km2)'],
    y=['Temperature', 'Population', 'CO2 (kt)', 'KWh use per capita', 'Agricultural land (km2)', 'Forest land (km2)'],)

    return heatmap
