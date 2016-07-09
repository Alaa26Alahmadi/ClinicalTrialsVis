from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import os

app = Flask(__name__)

MONGODB_HOST = 'mongodb://Admin:1qazxsw2@ds025973.mlab.com:25973/mydb'
MONGODB_PORT = 25973
DBS_NAME = 'mydb'
COLLECTION_NAME = 'results'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'collectionDay': True, 'total_donations': True, 'funding_status': True, 'grade_level': True, '_id': False}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo/DemogMesures")
def mesure():
    return render_template("DemogMesures.html")

@app.route("/demo/race")
def race():
    return render_template("AllRace.html")

@app.route("/demo/age")
def age():
    return render_template("AllAge.html")

@app.route("/demo/height")
def height():
    return render_template("AllHeight.html")

@app.route("/demo/StackedToGrouped")
def SToG():
    return render_template("StackedToGrouped.html")

@app.route("/outcomes/finalresult")
def result():
    return render_template("FinalResults.html")

@app.route("/outcomes/interactiveD3")
def interactiveD3():
    return render_template("InteraciveD3.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=5000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run()



