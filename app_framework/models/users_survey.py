
import pandas as pd
from psycopg2 import connect, sql
import os

conn = os.environ["TABLE_CONN"]

class UsersSurvey:
    def __init__(self):
        return

    def make_query(self):
        
        query_preferences = sql.SQL('''SELECT * 
                                     FROM user_preferences''')
        
        sql_query = pd.read_sql(query_preferences, conn)

        print(sql_query)
        # with self.async_engine.connect() as con:
        #     query = "SELECT * FROM user_preferences;"
        #     result = con.execute(text(query))

        return sql_query


