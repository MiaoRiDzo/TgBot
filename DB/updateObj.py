from config import *
from model import *
from sqlalchemy.orm import Session

#Cabinet
def updateCabinetID(id, CabinetNum, CabinetName, zone):
    session = Session(engine)
    
    obj = session.query(Cabinet).get(id)
    
    obj.CabinetNum = CabinetNum
    obj.CabinetName = CabinetName
    obj.ZoneID = zone.ZoneID
    
    session.add(obj)
    session.commit()
    session.close()

#Equipment
def updateEqStatusID(id, eqType, eqStat, eqCab, EqName, SN):
    session = Session(engine)

    obj = session.query(Equipment).get(id)

    obj.EquipmentTypeID = eqType.EquipmentTypeID
    obj.EquipmentStatusID = eqStat.EquipmentStatusID
    obj.CabinetID = eqCab.CabinetID

    obj.EquipmentName = EqName
    obj.SN = SN

#EqStatus
def updateEqStatusID(id, StatusName):
    session = Session(engine)
    
    obj = session.query(EquipmentStatus).get(id)
    
    obj.EquipmentStatusName = StatusName

    session.add(obj)
    session.commit()
    session.close()

#EqType
def updateEqTypeID(id, TypeName):
    session = Session(engine)
    
    obj = session.query(EquipmentType).get(id)
    
    obj.EquipmentTypeName = TypeName

    session.add(obj)
    session.commit()
    session.close()

#Zone
def updateZoneID(id, zoneName, Floor):
    session = Session(engine)
    
    obj = session.query(Zone).get(id)
    
    obj.ZoneName = zoneName
    obj.Floor = Floor 
    
    session.add(obj)
    session.commit()
    session.close()

