from config import *
from sqlalchemy.orm import Session, sessionmaker
from model import *

def delObj(obj):
    session = Session(engine)
    session.delete(obj)
    session.commit()
    session.close()