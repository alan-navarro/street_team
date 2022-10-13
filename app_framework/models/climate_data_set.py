from app_framework.db_connection.db_conn import DbConn
import pandas as pd
import numpy as np
from psycopg2 import connect, sql

bp = "\n"*3

class ClimateDataSet:
    def __init__(self):
        print("initializing ClimateDataSet class")

    def get_data(self, start_date, end_date):
        connections = DbConn().get_connection()
        conn = connections["conn"]
          
        query_db = sql.SQL('''SELECT country, temperature, year, name, population, co2, electricprod, agriculture, forest, TO_CHAR(date, 'yyyy-mm-dd') as date
                              FROM preprocessed_data
                              WHERE TO_CHAR(date, 'yyyy-mm-dd') 
                              BETWEEN '{start_date}' and '{end_date}'
                                      ''').format(start_date=sql.Identifier(start_date),end_date=sql.Identifier(end_date))
  
        df_climate = pd.read_sql(query_db,conn)
        pd.set_option('display.float_format', '{:,.1f}'.format)
        correlations_df = df_climate.copy()
        correlations_df.drop(columns="year", inplace = True) 
        correlations_top10 = correlations_df.corr()
        first_20_T = df_climate.groupby(['name', "country"])['temperature'].median().sort_values(ascending=False).head(20)
     
        class_outcome = {"correlations_top10": correlations_top10,
                          "first_20_T": first_20_T}
  
        print(class_outcome)
      
        return class_outcome

         # CO2 producers
        # grouped_co2 = df_climate.groupby('country')['co2'].median().sort_values(ascending=False)
     
            # # List of top 10 pollutant countries
        # first_10_CO2 = df_climate.groupby('country')['co2'].median().sort_values(ascending=False).head(11)
     
  
        # df_globe = df_climate.groupby(['date', 'country']).median()
            
     
        # sample_electric_prod = df_climate.groupby(['country'])
        # electric_prod_top10 = sample_electric_prod[['electricprod', 'co2']].aggregate(np.median).sort_values(ascending=False, by=['co2']).head(11)