from sqlalchemy import create_engine, MetaData
from .settings import Settings

settings = Settings() 
engine = create_engine(settings.url_database) # crear nueva conexion
metaData = MetaData()

conn = engine.connect()


 

