import sqlite3

#create the database (if the file doesn't exist) otherwise it will connect
conn = sqlite3.connect('pythonexplained.db')

#start the cursor instance
c = conn.cursor()

#select from the database
c.execute(('SELECT post FROM python WHERE post = "SQLite3"'))

#get the result
result = c.fetchone()

#assing the result to post
post = result[0]

#print post
print(post)
