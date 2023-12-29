import subprocess
import sys
import json
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


sqlite_filepath = "./contacts.db"
Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"
    contact_id = Column(Integer, primary_key=True)
    name = Column(String)
    risk = Column(Float)
    raw_response = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

def main():
    if len(sys.argv) != 2:
        print("Usage main.py <phone_number>")
        sys.exit(1)
    phone = sys.argv[1]
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    truecaller_resp = subprocess.check_output(['/data/data/com.termux/files/usr/bin/truecallerjs', '--json','-s',phone])
    truecaller_data = json.loads(truecaller_resp)
    contact = Contact(name=truecaller_data["data"][0]["name"], risk=truecaller_data["data"][0]["score"], raw_response=truecaller_resp)
    session.add(contact)
    session.commit()
    print(truecaller_resp.decode())
    
    


if __name__ == "__main__":
    main()