import sqlite3

#connect to database, if it doesnt exist it will create the database

conn = sqlite3.connect("my_database.db")

#create a cursor object so that you can interact with the databse
cursor = conn.cursor()
#create tables 
#using cursor object
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               Name TEXT,
               Surname TEXT,
               Age INT,
               DOB DATE,
               GENDER CHAR(1),
               NUMBER INT,
               ADDRESS TEXT,
               EMAIL TEXT,
               PASSWORD TEXT,
               )
               ''')

#Commikt changes
conn.commit()

#close databse connection 
conn.close()

