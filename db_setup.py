from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main1 import * 





engine = create_engine('sqlite:///mymusic.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


    

def current_prices():
    db_session.execute(dictionary.insert()), [ 
        {'id':'12','name':'a','lang':'eng'},
        {'id':'13','name':'b','lang':'eng'},
        {'id':'14','name':'c','lang':'eng'},
    ]
)
    db_session.commit()
        




def init_db():
    import models
    Base.metadata.create_all(bind=engine)