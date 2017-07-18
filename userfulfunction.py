import random
# 随机生成制定长度的字符串
def randomString(length):
    return ''.join(random.sample('1234567890987654321234567890987654321253711263849271642039', length))
# print(randomString(6))