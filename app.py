from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route('/sum', methods=['GET'])
def get_sum():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return {'sum': sum([num1, num2])}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')