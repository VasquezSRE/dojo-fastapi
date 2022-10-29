from importlib.metadata import metadata
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import metaData, engine

users = Table("users", metaData,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("email", String(255)),
              Column("password", String(255))
             )

metaData.create_all(engine)
