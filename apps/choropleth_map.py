import pandas as pd
import numpy as np
import dash
from dash import html 
from dash import dcc 
from datetime import datetime as dt 
from datetime import date
from dash.dependencies import Input, Output
import datetime
from dateutil.relativedelta import relativedelta
from dash import dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from apps.models.data_processing.global_warming import AnalizeFactors
from dash import dash_table
from dash.dash_table.Format import Format
from dash.dash_table.Format import Group
from app import app

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

layout = html.Div([
    dcc.DatePickerRange(
        id='global-date-picker',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="End Day",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True, # if false, the calendar will open up automatixally when values are deleted
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(1989, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2014, 1, 1),  # maximum date allowed on the DatePickerRange component
        start_date="1990-01-01", # buscar como poner el dia de hoy para mostrar
        end_date="1991-01-01",
        minimum_nights=0,  # minimum number of days between start and end date

        persistence=True,       # remember the date chosen
        persisted_props=['start_date',"end_date"],
        persistence_type='local',  # session, local, or memory. Default is 'local'

        updatemode='singledate'  # singledate or bothdates. Determines when callback is triggered
), # Closing date-Picker brackets
    
    html.Div([html.H1('Temperature increase over time', style={"textAlign": "center", "color": "#007F94", 'fontWeight': 'bold'}),
    html.Div([dcc.Loading(children=[dcc.Graph(id="choropleth_map")])],style={'width': '67%', 'display': 'inline-block', 'float': 'left'}), 
    ]),

    html.Div([
    dcc.Loading(children=[dash_table.DataTable(
    id='top20_table',
    columns =  [{"name": i, "id": i} for i in empty_df.columns],
    data = empty_df.to_dict('records'),
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    column_selectable="single",
    row_selectable="multi",
    page_action="native",
    page_size = 100,
    page_current = 0,
    ) # datatable
    ]) # loading datatable
    ], style={'width': '30%', 'display': 'inline-block',}),    
    ]) 


@app.callback(
    dash.dependencies.Output('choropleth_map', 'figure'),
    dash.dependencies.Output("top20_table", "data"),
    dash.dependencies.Output("top20_table", "columns"),
    [dash.dependencies.Input('global-date-picker', 'start_date'),
    dash.dependencies.Input('global-date-picker', 'end_date')])

def create_map(start_date, end_date):
    Analize_Factors = AnalizeFactors().get_data(start_date, end_date)

    first_20_T =Analize_Factors["first_20_T"].reset_index()
    first_20_T_mean = first_20_T["temperature"].mean()

    choropleth_map = px.choropleth(first_20_T, locations="name", color="temperature",
                        color_continuous_scale=px.colors.diverging.BrBG,
                        color_continuous_midpoint=first_20_T_mean,
                        hover_name="country", 
                        title="Data collected from 1990 to 2013" % first_20_T_mean)
        # ------------------------
    
    columns_table = [
    dict(id='country', name='country'),
    dict(id='temperature', name='temperature', type='numeric', format=Format()),
             ]
    
    data_table = first_20_T.to_dict('records')


    return choropleth_map, data_table, columns_table
