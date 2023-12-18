from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from passlib.hash import sha256_crypt

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/"
client = MongoClient("mongodb://localhost:27017")
db = client["trees"]  # Replace with your database name
collection = db["disease"]

@app.route('/')
def display_info():
    # Retrieve contact data from MongoDB
    info_collection = db.disease #variable = database.collectionname
    info_11 = info_collection.find() # query to find and storing in variable
    return render_template('Student_info.html', info_22=info_11)

@app.route('/3_funds')
def display_items():
    # Retrieve contact data from MongoDB
    prepmat_collection = db.funds #database.collectionname
    prepmat_11 = prepmat_collection.find()
    return render_template('item_info.html', prepmat_22=prepmat_11)

@app.route('/4_progress')
def display_transactions():
    # Retrieve contact data from MongoDB
    courses_collection = db.progress #database.collectionname
    courses_11 =  courses_collection.find()
    return render_template('Trans_info.html', courses_22=courses_11)

# @app.route('/4_jobrole')
# def jobrole():
#     return render_template('4_jobrole.html')





app.run(debug=True)