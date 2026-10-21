import mysql.connector

# Try to connect to your local MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",        # Default MySQL username
        password="",        # Put your MySQL password here if you set one, otherwise leave empty
        database="local_ai_engine"
    )

    if db.is_connected():
        print("Yay! Python is successfully connected to MySQL!")

except Exception as e:
    print(f"Oops, something went wrong: {e}")