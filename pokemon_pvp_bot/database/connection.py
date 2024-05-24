from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine('sqlite:///pokemon.db')
Session = sessionmaker(bind=engine)
session = Session()