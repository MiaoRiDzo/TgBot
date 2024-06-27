from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@178.161.150.241/DBEquip'
engine = create_engine(SQLALCHEMY_DATABASE_URI)