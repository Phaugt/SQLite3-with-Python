import sqlite3

#create the database (if the file doesn't exist) otherwise it will connect
conn = sqlite3.connect('pythonexplained.db')

#start the cursor instance
c = conn.cursor()

# Create table python
c.execute('''CREATE TABLE python
             (date text, post text, who text)''')

# Insert data to the table
c.execute("INSERT INTO python VALUES ('2020-12-21','SQLite3','phaugt')")

# Save "commit" the changes
conn.commit()

# Close the connection when we are done
conn.close()
