from flask import Flask,request,json,jsonify
from flask_cors import CORS
from flask_mail import Mail, Message


app = Flask(__name__)
CORS(app)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'joyoonsik18011@gmail.com'
app.config['MAIL_PASSWORD'] = 'dnwjd@456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/hi',methods=['GET', 'POST'])
def hi():
    print('zz')
    returnVal = { 
        'row' : 30,
        'col' : 40,
    }
    # msg = Message('Hello', sender='joyoonsik18011@gmail.com', recipients=['snsnsjsn24@gmail.com'])
    # msg.body = 'Hello Flask message sent fro Flask-Mail'
    # mail.send(msg)
    return json.dumps(returnVal)


if __name__ == '__main__' :
    app.run(debug=True)