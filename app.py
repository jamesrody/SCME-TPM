from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to your database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hotwheels68!",
    database="SCME_users"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    class_name = request.form['class']
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, class) VALUES (%s, %s, %s)",
        (name, email, class_name)
    )
    db.commit()
    return redirect('/')


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
