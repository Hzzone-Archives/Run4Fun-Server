import json
class User(object):
    def __init__(self, user_id, phone_number=None, user_name='新用户', password=None, ismale=True):
        self.user_id = user_id
        self.phone_number = phone_number
        self.user_name = user_name
        self.password = password
        self.ismale = ismale

class ReturnValue(object):
    def __init__(self, isOk=False, msg=None, user=None):
        self.isOk = isOk
        self.user = user
        self.msg = msg
    def toString(self):
        value = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return value
