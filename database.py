from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def init_db():
    engine = create_engine('sqlite:///weapon_stats.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
