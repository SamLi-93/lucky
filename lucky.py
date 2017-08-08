from flask import Flask, render_template
import pymysql

# db = pymysql.connect("127.0.0.1", "root", "root", "flight_tickets", charset='utf8')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'


@app.route('/lucky', methods=['GET', 'POST'])
def lucky():
    # cursor = db.cursor()
    # sql = "SELECT distinct airline_name FROM flight where price > 2000"
    # cursor.execute(sql)
    # results = cursor.fetchall()
    return render_template('lucky.html')

if __name__ == '__main__':
    app.run()
