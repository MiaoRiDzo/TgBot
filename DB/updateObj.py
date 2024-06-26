from config import *
from DB.models import *
from sqlalchemy.orm import Session

def update_object(model_class, id, **kwargs):
    session = Session(engine)
    
    obj = session.query(model_class).get(id)
    
    for key, value in kwargs.items():
        setattr(obj, key, value)
    
    session.add(obj)
    session.commit()
    session.close()