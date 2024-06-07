import asyncio
from dotenv import load_dotenv
import warnings
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

warnings.simplefilter("always")

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    second_name = Column(String(100))
    patronymic = Column(String(100))
    birth_data = Column(String(50))
    death_data = Column(String(50))
    birth_place = Column(String(100))
    death_place = Column(String(100))
    partner = Column(String(100))
    kind = Column(String(100))
    workplace = Column(String(100))
    awards = Column(String(100))
    epitaph = Column(String(10000))
    biography_1 = Column(String(10000))
    biography_2 = Column(String(10000))
    biography_3 = Column(String(10000))
    biography_4 = Column(String(10000))
    word_familiar = Column(String(10000))

class TgUser(Base):
    __tablename__ = 'tg_users'
    id = Column(Integer, primary_key=True)
    id_tg = Column(String(100))

async def create_data():
    try:
        Base.metadata.create_all(engine)
        print("[INFO] Table created")
        return "ok"
    except SQLAlchemyError as e:
        warnings.warn(f"Error: {e}")
        return "error"

async def add_new_person(person_data):
    try:
        new_person = Person(**person_data)
        session.add(new_person)
        session.commit()
        print("[INFO] New person added")
        return "ok"
    except SQLAlchemyError as e:
        session.rollback()
        warnings.warn(f"Error: {e}")
        return "error"

async def check_person_email(email):
    try:
        person = session.query(Person).filter_by(email=email).first()
        if person:
            print("[INFO] Person found")
            return "ok"
        else:
            print("[INFO] Person not found")
            return "not found"
    except SQLAlchemyError as e:
        warnings.warn(f"Error: {e}")
        return "error"

async def add_tg_id(email, tg_id):
    try:
        person = session.query(Person).filter_by(email=email).first()
        if person:
            new_tg_user = TgUser(id=person.id, id_tg=tg_id)
            session.add(new_tg_user)
            session.commit()
            print("[INFO] Telegram ID added")
            return "ok"
        else:
            print("[INFO] Person not found")
            return "not found"
    except SQLAlchemyError as e:
        session.rollback()
        warnings.warn(f"Error: {e}")
        return "error"

async def get_table_people():
    try:
        people = session.query(Person).all()
        columns = Person.__table__.columns.keys()
        result = [columns] + [[getattr(person, column) for column in columns] for person in people]
        return result
    except SQLAlchemyError as e:
        warnings.warn(f"Error: {e}")
        return "error"

async def get_table_reception():
    try:
        reception_data = session.execute("SELECT * FROM reception").fetchall()
        print(reception_data)
        return reception_data
    except SQLAlchemyError as e:
        warnings.warn(f"Error: {e}")
        return "error"
