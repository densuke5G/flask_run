from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from orm.models import User

password = config.DATABASE_PASSWORD
engine = create_engine('mysql+pymysql://root:' + password + '@localhost:3306/flask_run?charset=utf8')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    
    Base.metadata.create_all(bind=engine)

def regist_user(username, password):
    new_user = User(username, password)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()
