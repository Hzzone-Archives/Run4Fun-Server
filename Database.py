import psycopg2
from DataType import *

def connectPostgreSQL():
    conn = psycopg2.connect(database="run4fun", user="", password="", host="127.0.0.1", port="5432")
    print('connect successful!')
    return conn

# 登录主要逻辑，判断是否存在用户密码是否正确
def isUserExistsOrPasswdCorrect(user_id, password, cursor):
    cursor.execute("select * from public.user where user_id=%s", [user_id])
    rows = cursor.fetchall()
    if(len(rows)==0):
        return ReturnValue(msg='login: user does not exist').toString()
    else:
        one = rows[0]
        user = User(user_id=one[0], phone_number=one[1], user_name=one[2], password=one[3], ismale=[4])
        if user.password != password:
            return ReturnValue(isOk=False, msg='password is not correct', user=user).toString()
        else:
            return ReturnValue(isOk=True,msg='login success', user=user).toString()

# 判断用户是否已经存在，不存在则插入
def isUserExistsOrRegisterSuccess(user, authcode=None, conn=None):
    cursor = conn.cursor()
    cursor.execute("select * from public.user where user_id=%s", [user.user_id])
    rows = cursor.fetchall()
    if (len(rows) == 0):
        cursor.execute("insert into public.user values(%s, %s, %s, %s, %s)", [user.user_id, user.phone_number, user.user_name, user.password, 'True' if user.ismale else 'False'])
        conn.commit()
        return ReturnValue(isOk=True, msg='register success', user=user).toString()
    else:
        return ReturnValue(isOk=False, msg='register: user exists', user=user).toString()


conn = connectPostgreSQL()
# print(isUserExistsOrPasswdCorrect("11@qq.com", "1111", conn.cursor()))
user = User(user_id='11@qq.com', password='1111')
print(isUserExistsOrRegisterSuccess(user, conn=conn))
