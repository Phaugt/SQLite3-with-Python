import sqlite3

#create the database (if the file doesn't exist) otherwise it will connect
conn = sqlite3.connect('pythonexplained.db')

#start the cursor instance
c = conn.cursor()

# Larger example that inserts many records at a time
posts = [('2020-12-21', 'PyQt5', 'phaugt'),
             ('2020-12-20', 'JSON', 'phaugt'),
             ('2020-12-19', 'SHORT-URL', 'phaugt'),
            ]
c.executemany('INSERT INTO python VALUES (?,?,?)', posts)

# Save "commit" the changes
conn.commit()

# Close the connection when we are done
conn.close()