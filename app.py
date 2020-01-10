from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Go to specific routes for cars  by typing dogs after localhost."

cars = []

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/cars/<cars_id>', methods=['GET'])
def get_car(car_id):
    for car in cars: 
        if car['id'] == car_id:
            return car
    return None

@app.route('/cars', methods=['POST'])
def create_cars():
    cars.append(request.json)
    return jsonify(cars)

@app.route('/cars/<car_id>', methods=['PUT'])
def update_car(car_id):
    for car in cars:
        if car['id'] == car_id:
            car['make', 'model', 'year', 'body'] = request.json['make', 'model', 'year', 'body']
            return get_cars()

@app.route('/cars/<car_id>', methods=['DELETE'])
def delete_car(car_id):
    for car in cars: 
        if car['id'] == car_id:
            cars.remove(car)
            return get_cars()

app.run()