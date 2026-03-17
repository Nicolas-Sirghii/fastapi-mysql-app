from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error

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
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="example",
            database="messages_db"
        )
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

@app.get("/message")
def message():
    return {"message": get_message()}