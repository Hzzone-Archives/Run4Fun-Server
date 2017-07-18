from flask import Flask, request, session
from Database import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form.get('user_id')
    user_passwd = request.form.get('password')
    print("id: "+user_id)
    print("password: "+user_passwd)
    return isUserExistsOrPasswdCorrect(user_id=user_id, password=user_passwd, cursor=conn.cursor())

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form.get('user_id')
    user_passwd = request.form.get('password')
    phone_number = request.form.get('phone_number')
    user_name = request.form.get('user_name')
    ismale = request.form.get('ismale')
    return isUserExistsOrRegisterSuccess(User(user_id=user_id, phone_number=phone_number, user_name=user_name, password=user_passwd, ismale=ismale), conn=conn)

# 数据库连接
global conn

if __name__ == '__main__':
    conn = connectPostgreSQL()
    app.run()
