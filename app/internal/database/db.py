import psycopg2
import asyncio
from dotenv import load_dotenv
import warnings
import os
import random

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

warnings.simplefilter("always")


async def create_data():
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                F"""CREATE TABLE {DB_NAME}(
                        id INT,
                        name varchar(100),
                        second_name varchar(100),
                        patronymic varchar(100),
                        birth_data varchar(50),
                        death_data varchar(50),
                        birth_place varchar(100),
                        death_place varchar(100),
                        partner varchar(100),
                        kind varchar(100),
                        workplace varchar(100),
                        awards varchar(100),
                        epitaph varchar(10000),
                        biography_1 varchar(10000),
                        biography_2 varchar(10000),
                        biography_3 varchar(10000),
                        biography_4 varchar(10000),
                        word_familiar varchar(10000)
                        );
                        """
            )
        print("[INFO] Table created")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"



async def add_new_person(patient_data):
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            query = """
            INSERT INTO people 
            (id, full_name, age, parents_name, address, date_of_visit, specialists_name, meeting_format, personal_factors, neurosurgery, 
            sensitivity, neurourology, mobility, self_service, TCP, neuroorthopedics, coloproctology, productive_activity, leisure, communication, 
            ophthalmology, height_and_weight, smart_functions, pain, tasks, other)
            VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                patient_data.id, patient_data.full_name, patient_data.age, patient_data.parents_name,
                patient_data.address, patient_data.date_of_visit, patient_data.specialists_name,
                patient_data.meeting_format, patient_data.personal_factors, patient_data.neurosurgery,
                patient_data.sensitivity, patient_data.neurourology, patient_data.mobility,
                patient_data.self_service, patient_data.TCP, patient_data.neuroorthopedics,
                patient_data.coloproctology, patient_data.productive_activity, patient_data.leisure,
                patient_data.communication, patient_data.ophthalmology, patient_data.height_and_weight,
                patient_data.smart_functions, patient_data.pain, patient_data.tasks, patient_data.other
            )

            cursor.execute(query, values)

        print("[INFO] Table created")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def return_person(full_name):
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM people WHERE full_name = %s", (full_name,))
            person_data = cursor.fetchone()


    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return person_data



async def add_new_reception(person):
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            query = """
                INSERT INTO reception (
                    id, full_name, full_name_doctor, date, age, gestational_age, premature, CLAMS, CAT, GM
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            values = (
                person.id, person.full_name, person.full_name_doctor, person.date,
                person.age, person.gestational_age, person.premature,
                person.CLAMS, person.CAT, person.GM
            )
            cursor.execute(query, values)


            print("[INFO] Table add")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def return_reception(id):
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM reception WHERE id = %s", (id,))
            reception_data = cursor.fetchall()

        print(reception_data)

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return reception_data