from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS
from pymongo.message import query
import requests

app = Flask(__name__)


mongo = client = MongoClient()
db = mongo["SongFinderApp"]
serverStatusResult = db.command("serverStatus")
CORS(app)

@app.route("/findUserLogin", methods=["POST"])
def getLoginInfo():
    pass
    