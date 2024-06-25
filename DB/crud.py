from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model import *

engine = create_engine('sqlite:///DB/dbMain.db')

def addObject(obj):
    session = Session(bind=engine)
    try:
        session.add(obj)
        session.commit()
        print(f"{obj.__class__.__name__} object committed")
    except Exception as e:
        session.rollback()
        print(f"Exception occurred: {e}")
    finally:
        session.close()

for z in range(100):
    ins = Zone(
        ZoneName = f"Zone_{z}",
        Floor = z
    )
    addObject(ins)
