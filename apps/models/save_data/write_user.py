from apps.models.table.user_preferences import UserPreferences
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import datetime
from sqlalchemy import create_engine
import psycopg2
# from apps.db.db_conn import DbConn
import os

conn = os.environ["MANCHESTER"]


class WriteUser:
    def __init__(self):
        return print("Writting on DB...")

    def committing_data(self, user_name_, selection_):

        engine = create_engine(conn, echo = True, pool_size=500, max_overflow=-1, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
    
        if selection_ == 1:
            legend_ = "Population"
        elif selection_ == 2:
            legend_ = "GHG emissions"
        elif selection_ == 3:
            legend_ = "Power production"
        elif selection_ == 4:
            legend_ = "Increase of agricultural land"
        elif selection_ == 5:
            legend_ = "Decrease of forest land"
        else:
            pass
        try:
            if user_name_ == '':
                user_name_= None
            else:
                pass
            commit_preferences = UserPreferences(user_name = user_name_, selection = 1, legend = legend_,
            created_at = datetime.datetime.now())
    
            session.add(commit_preferences)
            session.commit()
        except:
            pass

        print("Data commited!")
        session.close()
        
        return