
# from pages.db_conn import DbConn
from db_conn import DbConn
import pandas as pd
from psycopg2 import connect, sql

bp = "\n"*3

class MakeDF:
    def __init__(self):
        print("make dataframe")

    def making_df(self):
        
        connections = DbConn().get_connection()
        conn = connections["conn"]
        
        query_preferences = sql.SQL('''SELECT * 
                                     FROM user_preferences''')
        
        sql_query = pd.read_sql(query_preferences,conn)
        

        return sql_query