import sqlite3
import asyncio
import warnings
from datetime import datetime

warnings.simplefilter("always")

DB_PATH = 'database.db'


def create_tables():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reception (
        id INTEGER PRIMARY KEY,
        full_name VARCHAR(100),
        age DATE,
        parents_name VARCHAR(100),
        address VARCHAR(100),
        date_of_visit DATE,
        specialists_name VARCHAR(100),
        meeting_format VARCHAR(50),
        personal_factors TEXT,
        neurosurgery TEXT,
        sensitivity TEXT,
        neurourology TEXT,
        mobility TEXT,
        self_service TEXT,
        TCP TEXT,
        neuroorthopedics TEXT,
        coloproctology TEXT,
        productive_activity VARCHAR(50),
        leisure TEXT,
        communication TEXT,
        ophthalmology TEXT,
        height_and_weight TEXT,
        smart_functions TEXT,
        pain TEXT,
        tasks TEXT,
        other TEXT,
        clams INT,
        cat INT,
        gm INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Fullname TEXT,
        Birthdate DATE,
        PhoneNumber VARCHAR(20),
        MotherFullname TEXT,
        City TEXT,
        Email VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tg_users (
        id INT,
        id_tg INT
    )
    """)

    connection.commit()
    connection.close()


try:
    create_tables()
except:
    print("Mabye bad")



async def add_new_person(person_data):
    connection = None

    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
                    INSERT INTO people
                    (Fullname, Birthdate, PhoneNumber, MotherFullname, City, Email) 
                    VALUES 
                    (?, ?, ?, ?, ?, ?)
                """

        values = (
            person_data.full_name,
            person_data.birthdate,
            person_data.phone_number,
            person_data.mother_full_name,
            person_data.city,
            person_data.email
        )

        cursor.execute(query, values)
        connection.commit()

        print("[INFO] Person added")

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
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM people WHERE fullname = ?", (full_name,))
        person_data = cursor.fetchone()

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return person_data


async def add_new_reception(patient_data):
    connection = None

    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            INSERT INTO reception 
            (id, full_name, age, parents_name, address, date_of_visit, specialists_name, meeting_format, personal_factors, neurosurgery, 
            sensitivity, neurourology, mobility, self_service, TCP, neuroorthopedics, coloproctology, productive_activity, leisure, communication, 
            ophthalmology, height_and_weight, smart_functions, pain, tasks, other, clams, cat, gm)
            VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            patient_data.id, patient_data.full_name, patient_data.age, patient_data.parents_name,
            patient_data.address, patient_data.date_of_visit, patient_data.specialists_name,
            patient_data.meeting_format, patient_data.personal_factors, patient_data.neurosurgery,
            patient_data.sensitivity, patient_data.neurourology, patient_data.mobility,
            patient_data.self_service, patient_data.TCP, patient_data.neuroorthopedics,
            patient_data.coloproctology, patient_data.productive_activity, patient_data.leisure,
            patient_data.communication, patient_data.ophthalmology, patient_data.height_and_weight,
            patient_data.smart_functions, patient_data.pain, patient_data.tasks, patient_data.other,
            patient_data.clams, patient_data.cat, patient_data.gm
        )

        cursor.execute(query, values)
        connection.commit()

        print("[INFO] Reception data added")

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
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM reception WHERE id = ?", (id, ))
        reception_data = cursor.fetchall()

        print(reception_data)

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return reception_data


async def add_tg_id(email, tg_id):
    connection = None

    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM people WHERE email = ?", (email,))
        reception_data = cursor.fetchone()

        cursor.execute("INSERT INTO tg_users (id, id_tg) VALUES (?, ?)", (reception_data['id'], tg_id))
        connection.commit()

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return reception_data


async def get_table_people():
    connection = None

    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM people")
        temp = cursor.fetchall()

        cursor.execute("PRAGMA table_info(people)")
        temp2 = cursor.fetchall()

        columns = [col[1] for col in temp2]
        temp = [columns] + [tuple(row) for row in temp]

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return temp
