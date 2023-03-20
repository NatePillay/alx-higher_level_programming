#!/usr/bin/python3
""" prints the State object with the name passed as argument from the
 database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    new_record = State(name = "Louisiana")

    session.add(new_record)
    session.commit()
    print(new_record.id)
