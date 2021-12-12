import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.user.model import Base

user = os.getenv('USER', 'postgres')
password = os.getenv('PASSWORD', 'mypwd')
host = os.getenv('HOST', 'my-postgres')
port = os.getenv('PORT', '5432')
database = os.getenv('DATABASE', 'postgres')

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
