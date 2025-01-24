from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

@app.route('/stats')
def get_stats():
  pref_counts = {}
  programme_counts = {}
  for student in data:
    pref = student['pref']
    programme = student['programme']
    if pref in pref_counts:
      pref_counts[pref] += 1
    else:
      pref_counts[pref] = 1
    if programme in programme_counts:
      programme_counts[programme] += 1
    else:
      programme_counts[programme] = 1
  return jsonify(pref_counts, programme_counts)
    
@app.route('/add/<a>/<b>')
def add(a, b):
    a = int(a)
    b = int(b)
    result = a + b
    return jsonify({'result': result})

      
@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    a = int(a)
    b = int(b)
    result = a - b
    return jsonify(result)

      
@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    a = int(a)
    b = int(b)
    result = a * b
    return jsonify(result)

      
@app.route('/divide/<a>/<b>')
def divide(a, b):
    a = int(a)
    b = int(b)
    result = a / b
    return jsonify(result)

app.run(host='0.0.0.0', port=8080)
