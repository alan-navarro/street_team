import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
#app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server