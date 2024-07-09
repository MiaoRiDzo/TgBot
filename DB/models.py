from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
#from DBconfig import engine 
# Create an engine

# Define the base class
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = 'user'
    TG_ID = Column(Integer, primary_key=True)
    UserName = Column(String(255), nullable=False)

    requests = relationship("Request", back_populates="user")

# Define the EquipmentType class
class EquipmentType(Base):
    __tablename__ = 'equipment_type'
    EquipTypeID = Column(Integer, primary_key=True)
    EquipTypeName = Column(String(255), nullable=False)

    equipment = relationship("Equipment", back_populates="equipment_type")

# Define the EquipmentStatus class
class EquipmentStatus(Base):
    __tablename__ = 'equipment_status'
    EquipmenStatusID = Column(Integer, primary_key=True)
    EquipmentStatusName = Column(String(255), nullable=False)

    equipment = relationship("Equipment", back_populates="equipment_status")

# Define the Zone class
class Zone(Base):
    __tablename__ = 'zone'
    ZoneID = Column(Integer, primary_key=True)
    ZoneName = Column(String(255), nullable=False)
    Floor = Column(Integer)

    cabinets = relationship("Cabinet", back_populates="zone")

# Define the Cabinet class
class Cabinet(Base):
    __tablename__ = 'cabinet'
    CabinetID = Column(Integer, primary_key=True)
    CabinetNum = Column(String(255), nullable=False)
    CabinetName = Column(String(255), nullable=False)
    ZoneID = Column(Integer, ForeignKey('zone.ZoneID'))

    zone = relationship("Zone", back_populates="cabinets")
    equipment = relationship("Equipment", back_populates="cabinet")

# Define the Equipment class
class Equipment(Base):
    __tablename__ = 'equipment'
    Equipment_ID = Column(Integer, primary_key=True)
    EquipmentTypeID = Column(Integer, ForeignKey('equipment_type.EquipTypeID'))
    EquipmentStatusID = Column(Integer, ForeignKey('equipment_status.EquipmenStatusID'))
    CabinetID = Column(Integer, ForeignKey('cabinet.CabinetID'))
    EquipmentName = Column(String(255), nullable=False)
    SN = Column(String(255), nullable=False)

    equipment_type = relationship("EquipmentType", back_populates="equipment")
    equipment_status = relationship("EquipmentStatus", back_populates="equipment")
    cabinet = relationship("Cabinet", back_populates="equipment")

# Define the RequestStatus class
class RequestStatus(Base):
    __tablename__ = 'request_status'
    RequestStatusID = Column(Integer, primary_key=True)
    RequestStatusName = Column(String(255), nullable=False)

    requests = relationship("Request", back_populates="request_status")

# Define the Request class
class Request(Base):
    __tablename__ = 'request'
    RequestID = Column(Integer, primary_key=True)
    TG_ID = Column(Integer, ForeignKey('user.TG_ID'))
    RequestStatusID = Column(Integer, ForeignKey('request_status.RequestStatusID'))
    Description = Column(String(255), nullable=False)

    user = relationship("User", back_populates="requests")
    request_status = relationship("RequestStatus", back_populates="requests")

#Base.metadata.create_all(engine)