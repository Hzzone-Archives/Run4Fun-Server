from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/register', methods=['POST'])
def register():
    pass


if __name__ == '__main__':
    app.run()
