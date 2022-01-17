from optparse import Values
from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np


app = Flask(__name__)

# Read in the data

data_df = pd.read_excel("static/data/full_data_final.xlsx", index_col=0, dtype=object)
fatal_df = data_df[(data_df['DOA_Status'] == 'Fatal').notnull()]


@app.route('/')
def index():
    return render_template('index.html')

def calculate_percentage(val, total):
   """Calculates the percentage of a value over a total"""
   percent = np.round((np.divide(val, total) * 100), 2)
   return percent


def data_creation(data, percent, class_labels, group=None):
   for index, item in enumerate(percent):
       data_instance = {}
       data_instance['category'] = class_labels[index]
       data_instance['value'] = item
       data_instance['group'] = group
       data.append(data_instance)


@app.route('/get_piechart_data')
def get_piechart_data():

    class_labels = ["Male", "Female"]
    _ = fatal_df.groupby('DOA_Status').size().values
    class_percent = calculate_percentage(_, np.sum(_)) #Getting the value counts and total

    piechart_data= []
    data_creation(piechart_data, class_percent, class_labels)
    return jsonify(piechart_data)



@app.route('/get_barchart_data')
def get_barchart_data():

    age_labels = ['0-15', '16-25', '26-35', '36-45', '46-55', '56-65', '66-75', '86-99']
    data_df['age_group'] = pd.cut(data_df.AGE, 8, labels=age_labels)
    select_df = data_df[['age_group','Sex']]

    male = select_df[select_df['Sex']=='Male']
    female = select_df[select_df['Sex']=='Female']

    _ = male.groupby('age_group').size().values
    male_percent = calculate_percentage(_, np.sum(_))
    _ = female.groupby('age_group').size().values
    female_percent = calculate_percentage(_, np.sum(_))
    _ = select_df.groupby('age_group').size().values
    all_percent = calculate_percentage(_, np.sum(_))

    barchart_data = []
    data_creation(barchart_data,all_percent, age_labels, "All")
    data_creation(barchart_data,male_percent, age_labels, "Month-to-month")
    data_creation(barchart_data,female_percent, age_labels, "One year")
    return jsonify(barchart_data)


if __name__ == '__main__':
   app.run(debug=True)
