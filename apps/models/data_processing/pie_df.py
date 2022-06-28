
import pandas as pd
from psycopg2 import connect, sql
from apps.db.db_conn import DbConn

conn = DbConn().get_connection()

class MakeDF:
    def __init__(self):
        print("make dataframe")

    def making_df(self):
        
        query_preferences = sql.SQL('''SELECT * 
                                     FROM user_preferences''')
        
        sql_query = pd.read_sql(query_preferences,conn)
        

        return sql_query