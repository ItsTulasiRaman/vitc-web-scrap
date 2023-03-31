from flask import Flask, Response, jsonify
from flask_pymongo import pymongo, PyMongo
import json
from bson import ObjectId
import subprocess

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://ItsTulasiRaman:admin123@vitccweb.x8cotvw.mongodb.net/?retryWrites=true&w=majority"
# mongo = PyMongo(app)
CONNECTION_STRING = "mongodb+srv://ItsTulasiRaman:admin123@vitccweb.x8cotvw.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client["vitccwebscrap"]
#user_collection = pymongo.collection.Collection(db, "faculty_info")
collection = db["faculty_info"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



@app.route("/vitcweb/api/fetch")
def index():
    #spider_name = "emailSpider"
    # subprocess.getoutput(['scrapy', 'crawl', spider_name])
    #subprocess.run(['scrapy crawl emailSpider'])
    # print("DB =>",mongo.db)
    # data = [i for i in mongo.db.find({})]
    # return Response (JSONEncoder().encode(data),status=200)
    data =[i for i in collection.find({})]
    return Response(JSONEncoder().encode(data), status=200)

@app.route("/vitcweb/api/update")
def update():
    spider_name = "emailSpider"
    subprocess.run(['scrapy', 'crawl', spider_name])
    return "Success"


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)