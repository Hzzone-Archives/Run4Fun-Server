# Run4Fun-Server API

* 登录        
<br>向```127.0.0.1:5000/login```发送post请求，参数如下:
```json
    {
      "user_id": "用户id",
      "password": "用户密码"
    }
```
返回值     
1. 登录成功
```json
{
    "isOk": true,
    "msg": "login success",
    "user": {
        "ismale": [
            4
        ],
        "password": "1111",
        "phone_number": "17721876903",
        "user_id": "zhizhonghwang@gmail.com",
        "user_name": "hzzone"
    }
}
```
2. 登录失败
```json
{
    "isOk": false,
    "msg": "password is not correct",
    "user": {
        "ismale": [
            4
        ],
        "password": "1111",
        "phone_number": "17721876903",
        "user_id": "zhizhonghwang@gmail.com",
        "user_name": "hzzone"
    }
}
```

* 注册    
 
注册分为两步，需要分别发送post请求 

<br>向```127.0.0.1:5000/register-1```发送post请求，参数如下:
```json
{
  "user_id": "zhizhizhonghwang@gmail.com",
  "password": "1111",
  "phone_number": "17721876903",
  "user_name": "Hzzone",
  "ismale": true
}
```
1. 如果用户不存在，发送验证码到用户邮箱或手机(如果手机号不为空的话，优先发送短信，验证码为6位纯数字)
    
    **这时候没有插入到数据库**
```json
{
    "isOk": true,
    "msg": "142421",
    "user": {
        "ismale": "true",
        "password": "1111",
        "phone_number": "111",
        "user_id": "zhizhonghwang@gmail.com",
        "user_name": "2222"
    }
}
```
验证码效果简略如下:
![](http://omoitwcai.bkt.clouddn.com/2017-07-18-IMG_0785-1.PNG)

2. 如果用户存在：
```json
{
    "isOk": false,
    "msg": "register: user exists",
    "user": {
        "ismale": "true",
        "password": "1111",
        "phone_number": "111",
        "user_id": "zhizhonghwang@gmail.com",
        "user_name": "2222"
    }
}
```

3. 正式注册，验证成功后插入数据库  

向```127.0.0.1:5000/register-2```发送post请求
参数一样，插入成功后返回：
```json
{
    "isOk": true,
    "msg": "verify authcode success",
    "user": {
        "ismale": "true",
        "password": "1111",
        "phone_number": "111",
        "user_id": "zhizhonghwang@gmail.com",
        "user_name": "2222"
    }
}
```

