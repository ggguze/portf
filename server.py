from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'Form submitted'
    else:
        return 'something went wrong'



