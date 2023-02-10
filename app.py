import flask
from flask import Flask, request, render_template
import datetime
import mysql.connector

app = Flask(__name__)

# Connect to Google Cloud SQL database
mydb = mysql.connector.connect(
  host="host_name",
  user="user_name",
  password="password",
  database="database_name"
)

# Create table for storing experiment entries
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS experiments (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, title VARCHAR(255), entry TEXT)")

# Route for main page that displays table of contents
@app.route('/')
def index():
    mycursor.execute("SELECT id, date, title FROM experiments")
    experiments = mycursor.fetchall()
    return render_template('index.html', experiments=experiments)

# Route for adding new experiment entry
@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        title = request.form['title']
        entry = request.form['entry']
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        mycursor.execute("INSERT INTO experiments (date, title, entry) VALUES (%s, %s, %s)", (date, title, entry))
        mydb.commit()
        return flask.redirect('/')
    return render_template('add.html')

# Route for viewing individual experiment entry
@app.route('/view/<int:id>')
def view_entry(id):
    mycursor.execute("SELECT * FROM experiments WHERE id = %s", (id,))
    experiment = mycursor.fetchone()
    return render_template('view.html', experiment=experiment)

if __name__ == '__main__':
    app.run()
