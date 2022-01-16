from curses import meta
from importlib.metadata import metadata
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, request, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def index():
    """This is the index or home route."""
    return render_template("index.html")


@app.route("/states/")
def state_list():

    months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

    states = DB.states()
    return render_template("chart.html", months=months, states=states)

    
@app.route("/accident-data/")
def accident_data():
    # print(request.args.get("month"))
    metaData = DB.get_data()

    if request.args.get("index"):
        metaData = metaData[:400]

    elif request.args.get("month"):
        month = request.args.get("month")
        metaData = [data for data in metaData if data.get("month") == month]

    elif request.args.get("state"):
        state = request.args.get("state")
        metaData = [data for data in metaData if data.get("state") == state]

    return jsonify(metaData)


@app.route("/plots/") 
def accident_plot():

    metaData = jsonify(DB.get_data())
    return render_template("chart.html", metaData=metaData)



if __name__ == '__main__':
    app.run(debug=True)