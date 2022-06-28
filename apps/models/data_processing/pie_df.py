
import pandas as pd
from psycopg2 import connect, sql
import os

conn = os.environ["DATABASE_URL"]


class MakeDF:
    def __init__(self):
        print("make dataframe")

    def making_df(self):
        
        query_preferences = sql.SQL('''SELECT * 
                                     FROM user_preferences''')
        
        sql_query = pd.read_sql(query_preferences,conn)
        

        return sql_query