import psycopg2
import os

class DbConn:

    def __init__(self):
        print("initializing Connection class")

    def get_connection(self):
        host = os.environ["HOST"]
        db_name = os.environ["DB_NAME"]
        user = os.environ["USER"]
        password = os.environ["PASSWORD"]
        
        conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, "5432", db_name, user, password))

        table_conn = os.environ["TABLE_CONN"]
        
        dict_conn = {"conn": conn, "table_conn": table_conn}
        
        return dict_conn

