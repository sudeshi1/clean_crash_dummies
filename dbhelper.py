# This Python script connects to a PostgreSQL database and utilizes Pandas to obtain data and create a data frame
# A initialization and configuration file is used to protect the author's login credentials 
import psycopg2
import pandas as pd
from flask import jsonify
import json
from dbconfig import config



class DBHelper:

# Establish a connection to the database by creating a cursor object
# Obtain the configuration parameters
    def connect(self):
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        return conn

# A function that takes in a PostgreSQL query and outputs a jsonified result
# Store the data as a variable
    def get_data(self):
        connection = self.connect()
        try:
            query = '''SELECT a.case_number, a.month, a.day, a.state, a.city, a.lat, a.lon, p.sex, p.age_label, \
                p.age, p.doa_status, p.vehicle_model, p.vehicle_manufacturer, \
                a.route, a.first_harm, a.man_collision, a.light_condit, a.weather, a.rural_urban, v.hit_run \
                from accidents a \
                inner join people p \
                on a.case_number=p.case_number \
                inner join vehicle v \
                on p.case_number=v.case_number'''

            # Create DataFrame using pandas
            df = pd.read_sql(query, connection)
            # Remove duplicate case_number's from retrieved query
            no_dups_df = df.drop_duplicates()
            # Transform result into json object
            result = no_dups_df.to_json(orient="records")
            # Load result into json object and return to flask route
            parsed = json.loads(result)
            return (parsed)

        finally:
            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            connection.close()



    def states(self):

        connection = self.connect()

        try:
            states = connection.get("state")

            return list(states)

        finally:
            connection.close()