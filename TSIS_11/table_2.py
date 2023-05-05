import psycopg2

# Connect to the database
conn = psycopg2.connect(
    database='snake',
    user='postgres',
    password='2679528',
    host="localhost",
)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create the phonebook table
cur.execute("CREATE TABLE phonebook (name VARCHAR(50), number VARCHAR(20))")

# Commit the changes
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()