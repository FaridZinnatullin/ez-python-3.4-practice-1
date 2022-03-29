import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.mapper import metadata

# user = os.getenv('USER', 'postgres')
# password = os.getenv('PASSWORD', 'wwanrltw')
host = os.getenv('POSTGRES_DB_HOST', 'localhost')
# port = os.getenv('PORT', '5432')
# database = os.getenv('DATABASE', 'evraz_lab')

engine = create_engine(f"postgresql+psycopg2://barash:123456@{host}/evraz_db")

Session = sessionmaker(engine)
metadata.create_all(engine)
