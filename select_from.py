import sqlite3

#create the database (if the file doesn't exist) otherwise it will connect
conn = sqlite3.connect('pythonexplained.db')

#start the cursor instance
c = conn.cursor()

for row in c.execute('SELECT * FROM python ORDER BY date'):
    print(row)