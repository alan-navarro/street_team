
import pandas as pd
from psycopg2 import connect, sql
from sqlalchemy import create_engine
from sqlalchemy import text
import os

conn = os.environ["TABLE_CONN"]
engine = create_engine(conn)

class UsersSurvey:
    def __init__(self):
        return

    def make_query(self):   
        # query_preferences = sql.SQL('''SELECT * 
        #                              FROM user_preferences''')
        sql = "SELECT * FROM user_preferences"
        df = pd.read_sql_query(sql, engine)
        # sql_query = pd.read_sql(query_preferences, conn)
        # result = await conn.execute(text(query_preferences))

        return df

        # # print(result)
        # async with self.async_engine.connect() as con:
        #     query = "SELECT * FROM user_preferences"
        #     result = await con.execute(text(query))
        # return result


