from config import *
from sqlalchemy.orm import Session, sessionmaker
from models import *

def delObj(obj):
    session = Session(engine)
    obj = session.merge(obj)
    session.delete(obj)
    session.commit()
    session.close()
