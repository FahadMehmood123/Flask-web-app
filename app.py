from flask import Flask,flash,render_template,url_for,request,redirect
import sqlite3


connection=sqlite3.connect('database.db')
cursor=connection.cursor()



command2="""CREATE TABLE IF NOT EXISTS User(TeacherId INTEGER,Password TEXT)"""
cursor.execute(command2)

comd="""SELECT * FROM User"""
cursor.execute(comd)

connection.commit()


app=Flask(__name__)
app.secret_key="__privatekey__"

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html') 

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        connection=sqlite3.connect('database.db')
        cursor=connection.cursor()
        name=request.form['AdminKey']
        TeacherID=request.form['TeacherId']
        Password=request.form['Password']
        if name=="12345":
            cursor.execute("INSERT INTO User(TeacherId,Password) VALUE(?,?)",(TeacherID,Password))
            connection.commit()
        else:
            flash("Invalid Admin Key")
    return render_template('signup.html') 



if __name__=="__main__":
    app.run(debug=True)