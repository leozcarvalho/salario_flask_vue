from flask import Flask, jsonify, request
from flask_cors import CORS

SALARY = [
{
    'jobtime': 40,
    'cash': 20
}
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/salary', methods=['GET'])
def get_salary():
    response_object = {'status': 'success'}
    response_object['salary'] = SALARY
    return jsonify(response_object)

@app.route('/salary', methods=['POST'])
def post_salary():
    
    post_data = request.get_json()
    
    time = post_data.get('jobtime')
    money = post_data.get('cash')
    
    SALARY.append({
        'jobtime': post_data.get('jobtime'),
        'cash': post_data.get('cash')
    })

    fullSal = fullSalary(time,money)

    return jsonify({'fullsalary' : fullSal, 'inss' : calcInss(fullSal), 'sind' : calcSind(fullSal), 'ir' : calcIr(fullSal), 'finalsalary' : finalSalary(fullSal)})

def fullSalary(time, money):
    return time * money

def calcInss(salary):
    return salary * 0.08

def calcIr(salary):
    return salary * 0.11

def calcSind(salary):
    return salary * 0.05

def finalSalary(salary):
    return salary - calcInss(salary) - calcIr(salary) - calcSind(salary)
    
if __name__ == '__main__':
    app.run()