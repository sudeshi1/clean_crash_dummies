from importlib.metadata import metadata
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def index():
    """This is the index or home route."""
    return render_template("index.html")


@app.route("/states")
def state_list():

    states = state_list()
    return render_template("map.html", states=states)


    
@app.route("/accident-data")
def accident_data():
    metaData = jsonify(DB.get_data()) 
    return (metaData)


@app.route("/plots") 
def accident_plot():

    metaData = jsonify(DB.get_data())
    return render_template("chart.html", metaData=metaData)



if __name__ == '__main__':
    app.run(debug=True)