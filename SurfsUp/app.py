# Import the dependencies.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with = engine)

# Save references to each table

measurement = Base.classes.measurement

station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)

# Query Date Pull

def get_query_date():
    
    # Find the most recent date in the data set

    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    recent_date_converted = dt.datetime.strptime(recent_date[0], '%Y-%m-%d').date()
    
    # Calculate the date one year from the last date in data set

    query_date = recent_date_converted - dt.timedelta(days=365)

    return query_date

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def homepage():

	return ("""<b>Hawaii Weather Data from 2010-01-01 to 2017-08-23 </b> <br/>
<b>Homepage </b> <br/>
<br/>
<b> List of all available routes: </b> <br/>
<b> / </b> <br/>
<b> /api/v1.0/precipitation </b> <br/>
<b> /api/v1.0/stations </b> <br/>
<b> /api/v1.0/tobs </b> <br/>
<b> /api/v1.0/</b> start date YYYY-MM-DD <br/>
<b>/api/v1.0/</b> start date YYYY-MM-DD <b> / </b> end date YYYY-MM-DD
""")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # get query date
    
    query_date = get_query_date()
    
    # Perform a query to retrieve the data and precipitation scores

    precipitation_results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= query_date).\
        order_by(measurement.date).all()
    
    # Create dictionary using date as key and prcp as value

    prcp_dict = [{date : prcp} for date, prcp in precipitation_results]
    
	
    return jsonify(prcp_dict)

@app.route ("/api/v1.0/stations")
def stations():
     
    # Perform a query to retrieve the data and precipitation scores

    stations_list = session.query(station.station, station.name).\
        distinct().all()                                                                                                                                      
    
    # Create dictionary using date as key and prcp as value

    stations_dict = [{"station id": station, "station name": name} for station, name in stations_list]

    return jsonify(stations_dict)

@app.route ("/api/v1.0/tobs")
def tobs():
    # get query date
    
    query_date = get_query_date()

    # Find the most active station
    
    active_stations = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).\
        order_by(func.count(measurement.station).desc()).first()

    # Query temperature data for most active station
    
    temperature_results = session.query(measurement.date, measurement.tobs, measurement.station).\
        filter(measurement.station == active_stations[0]).\
        filter(measurement.date >= query_date).\
        order_by(measurement.date).all()

    # Create list of temperature observations
    
    temp_list = [{"date": date, "temperature": temp, "station": station} for date, temp, station in temperature_results]

    return jsonify(temp_list)

@app.route("/api/v1.0/<start>")
def temp_stats(start):
    # Convert start date string to datetime
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date() # using the string parse time method to convert the input
    
    # Query temperature stats for all stations after start date
    temp_stats = session.query(func.min(measurement.tobs).label('TMIN'),
                            func.max(measurement.tobs).label('TMAX'),
                            func.avg(measurement.tobs).label('TAVG')).\
        filter(measurement.date >= start_date).all()
    
    # Create dictionary of temperature statistics
    temp_dict = {
        "TMIN": temp_stats[0][0],
        "TMAX": temp_stats[0][1],
         "TAVG": temp_stats[0][2]
    }

    return jsonify(temp_dict)

@app.route("/api/v1.0/<start>/<end>")
def temp_stats_range(start, end):
    # Convert start and end dates to datetime
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()

    # Query temperature stats for all stations after start date
    temp_stats = session.query(func.min(measurement.tobs).label('TMIN'),
                            func.max(measurement.tobs).label('TMAX'),
                            func.avg(measurement.tobs).label('TAVG')).\
        filter(measurement.date >= start_date).\
        filter(measurement.date <= end_date).all()
    
    # Create dictionary of temperature statistics
    temp_dict = {
        "TMIN": temp_stats[0][0],
        "TMAX": temp_stats[0][1],
        "TAVG": temp_stats[0][2]
    }

    return jsonify(temp_dict)

if __name__ == "__main__":
    app.run(debug=True)