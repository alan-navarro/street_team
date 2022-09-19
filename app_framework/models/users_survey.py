
import pandas as pd
from psycopg2 import connect, sql
from sqlalchemy import text
import os

conn = os.environ["TABLE_CONN"]

class UsersSurvey:
    def __init__(self):
        return

    def make_query(self):
        
        query_preferences = sql.SQL('''SELECT * 
                                     FROM user_preferences''')
        
        # sql_query = pd.read_sql(query_preferences, conn)
        result = await conn.execute(text(query_preferences))

        print(result)

        return result


