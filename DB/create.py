from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
#from model import *

engine = create_engine('sqlite:///DB/dbMain.db')
Session = sessionmaker(bind=engine)

def addObject(obj):
    with Session() as session:
        session.add(obj)
        session.commit()
        print(f"{obj.__class__.__name__} object committed")