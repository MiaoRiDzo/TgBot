
from config import *
from sqlalchemy.orm import Session, sessionmaker
from DB.models import *
from DB.DBconfig import *

def delObj(obj_id, model):
    session = Session(engine)
    delIns = session.query(model).get(obj_id)
    session.delete(delIns)
    session.commit()
    session.close()
