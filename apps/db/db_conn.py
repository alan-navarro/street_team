import psycopg2
import os


host = os.environ["HOST"]
dbname = os.environ["DB"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]


class DbConn:

    def __init__(self):
        print("initializing Connection class")

    def get_connection(self):
        conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, "5432", dbname, user, password))
        
        return conn

