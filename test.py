from sendemail import sendEmail
# sendEmail("test", 'hahah', "zhizhonghwang@gmail.com")

import requests
data = {'user_id':'zhizhonghwang@gmail.com', 'password':'11111'}
url = '127.0.0.1:5000/login'
response = requests.post(url=url, data=data)
print(response.text)
