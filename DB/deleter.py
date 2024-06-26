import sys
sys.path.append('C:/Users/Admin/Documents/sorce/equipBot/TgBot/')
from config import *
from sqlalchemy.orm import Session, sessionmaker
from DB.models import *

def delObj(obj):
    session = Session(engine)
    obj = session.merge(obj)
    session.delete(obj)
    session.commit()
    session.close()
