from flask import Flask, request,redirect
import sqlite3

app = Flask(__name__)

#function to insert form data into database
def insert_user(data):
    #establish connection 
    conn = sqlite3.connect('my_database.db')
    #create cursor
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO users(  --inserts into these columns table --
               Name,
               Surname,
               Age,
               DOB,
               GENDER,
               NUMBER,
               ADDRESS,
               EMAIL,
               PASSWORD)
    VALUES(?,?,?,?,?,?,?,?)     --defines placeholders for values to be inserted
                   ''',
                   #actual data being passed into columns 
                  (data['Name'],data['Surname'],data['Age'],data['DOB'],data['GENDER'],data['NUMBER'],data['ADDRESS'],data['EMAIL'],data['PASSWORD']))
    
    #commit changes
    conn.commit()
    conn.close()

    
    @app.route('/register',methods = ['POST'])

    def register():
        #extract form data

        data = {
            'Name':request.form['Name'],
            'Surname':request.form['Surname'],
            'Age':request.form['Age'],
            'DOB':request.form['Date'],
            'GENDER':request.form['Gender'],
            'NUMBER':request.form['number'],
            'ADDRESS':request.form['address'],
            'EMAIL':request.form['email'],
            'PASSWORD':request.form['password']
        }
        insert_user(data)
        return redirect('/')
    
    if __name__ == '__main__':
        app.run(debug = True)


