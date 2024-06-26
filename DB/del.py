from config import *
from sqlalchemy.orm import Session, sessionmaker
from model import *

def delObj(obj):
    session = Session(engine)
    obj = session.merge(obj)
    session.delete(obj)
    session.commit()
    session.close()

session = Session(engine)
delet = session.query(User).first()

delObj(delet)