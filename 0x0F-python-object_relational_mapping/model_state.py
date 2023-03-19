
#!/usr/bin/python3
"""
    create class: State
    using the database hbtn_0e_4_usa
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine



Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+pymysql://localhost:3306/mydatabase')

Base.metadata.create_all(engine)

