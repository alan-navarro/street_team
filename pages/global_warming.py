from db_conn import DbConn
# from pages.db_conn import DbConn
import pandas as pd
import numpy as np
from psycopg2 import connect, sql

bp = "\n"*3

class AnalizeFactors:
    def __init__(self):
        print("initializing AnalizeFactors class")

    def get_data(self, start_date, end_date):
      connections = DbConn().get_connection()
      conn = connections["conn"]
        
      query_db = sql.SQL('''SELECT country, temperature, year, name, population, co2, electricprod, agriculture, forest, TO_CHAR(date, 'yyyy-mm-dd') as date
                            FROM preprocessed_data
                            WHERE TO_CHAR(date, 'yyyy-mm-dd') 
                            BETWEEN '{start_date}' and '{end_date}'
                                    ''').format(start_date=sql.Identifier(start_date),end_date=sql.Identifier(end_date))

      df_climate = pd.read_sql(query_db,conn)

       # CO2 producers
      grouped_co2 = df_climate.groupby('country')['co2'].median().sort_values(ascending=False)
      pd.set_option('display.float_format', '{:,.1f}'.format)
   
          # # List of top 10 pollutant countries
      first_10_CO2 = df_climate.groupby('country')['co2'].median().sort_values(ascending=False).head(11)
   
      correlations_df = df_climate.copy()
      correlations_df.drop(columns="year", inplace = True) 
      correlations_top10 = correlations_df.corr()

      df_globe = df_climate.groupby(['date', 'country']).median()
          
      first_20_T = df_climate.groupby(['name', "country"])['temperature'].median().sort_values(ascending=False).head(20)
   
      sample_electric_prod = df_climate.groupby(['country'])
      electric_prod_top10 = sample_electric_prod[['electricprod', 'co2']].aggregate(np.median).sort_values(ascending=False, by=['co2']).head(11)
   
   
      class_outcome = {"df_climate": df_climate, "grouped_co2": grouped_co2,
                        "first_10": first_10_CO2, "correlations_top10": correlations_top10,
                        "df_globe": df_globe, "first_20_T": first_20_T, "electric_prod_top10": electric_prod_top10}
      
      return class_outcome