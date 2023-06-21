from flask import Flask, request
app = Flask(__name__)

@app.route("/add", methods=['GET'])
def add():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    result = num1 + num2
    return {'result': result}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
