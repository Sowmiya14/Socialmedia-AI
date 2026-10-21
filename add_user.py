import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="local_ai_engine"
)

cursor = db.cursor()

# Let's add a dummy boutique owner named Priya
sql = "INSERT INTO users (business_name, niche, email) VALUES (%s, %s, %s)"
val = ("Priya's Boutique", "Boutique", "priya@boutique.com")

cursor.execute(sql, val)

# Save the changes
db.commit()

print(f"{cursor.rowcount} local business added successfully to MySQL!")

# Close the connection
cursor.close()
db.close()