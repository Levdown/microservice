from flask import Flask
from db import Database
app = Flask(__name__)

db = Database()
db.create_table()

@app.route('/api/update/<name>/<price>')
def update(name, price):
    print('in db ', name, price)
    if db.check_name(name):
        db.update_price(name, price)
    else:
        db.insert_values(name, price)

    return f"{name}: {price}"
    
@app.route('/api/info/<name>')
def get_info(name):
    info = db.get_info(name)
    return f"{info[0]}: {info[1]}"

app.run()
