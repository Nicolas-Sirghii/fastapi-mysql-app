from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import Error
from db import getConnection


app = FastAPI()

# allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_message():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT text FROM messages LIMIT 1;")
        result = cursor.fetchone()
        return result[0] if result else "No message"
    except Error as e:
        return f"Error: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def get_greeting():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT text FROM gritings LIMIT 1;")
        result = cursor.fetchone()
        return result[0] if result else "No message"
    except Error as e:
        return f"Error: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@app.get("/products")
def message():
    return {"message": get_message()}

@app.get("/griting")
def griting():
    return {"griting": get_greeting()}