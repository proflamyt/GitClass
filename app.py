from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "xnbdjhx hsnmhbhsd"


db = SQLAlchemy(app)


# Table 
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


with app.app_context():
    db.create_all()

@app.route('/', methods= ['GET'])
def first():
    ola = students.query.all()
    return {
        "name": ola[0].name,
        "city": ola[0].city,
        "addr": ola[0].addr,
        "pin": ola[0].pin
    }
    

@app.route('/new', methods = ['GET', 'POST'])
def new_student():
    if request.method == 'POST':

        try:
            if not request.json['name'] or not request.json['city'] or not request.json['addr'] or not request.json['pin'] :
                return {
                    "message": "kindly supply all the user input"
                }
            student = students(request.json['name'], request.json['city'], request.json['addr'], request.json['pin'])
            db.session.add(student)
            db.session.commit()
            return {
                "message": "user stored successfully"
            }
        except:
        
            return {
                    "message": "kindly supply all the user input"
                }

    else:
        return {
            "message": "send in a post request"
        }


if __name__ == '__main__':
    
    app.run(debug = True)