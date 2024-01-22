#  For this project we are going to store all of our currently vehicles in a list
#  we should be able to perform a get request to retrieve a list of these vehicles
#  we should also be able to perform a post request to add a new vehicle to the list

from flask import Flask, jsonify

app = Flask(__name__)

vehicles = [
    {"Id": 1, "Make": "RAM", "Model": "3500", "Year": 2018, "Color": "White"},
    {"Id": 2, "Make": "RAM", "Model": "1500", "Year": 2022, "Color": "Red"},
    {"Id": 3, "Make": "Harley-Davidson", "Model": "Road Glide", "Year": 2023, "Color": "Black"},
]


@app.get("/vehicles")
def get_vehicles():
    return jsonify(vehicles)
