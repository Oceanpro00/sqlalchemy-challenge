# SQLAlchemy Challenge

## Overview

This repository contains my solution for the **SQLAlchemy Challenge** from Module 10 of the Data Analytics Bootcamp. This project focuses on analyzing climate data for Honolulu, Hawaii, using tools like SQLAlchemy ORM, Pandas, Matplotlib, and Flask. The goal is to demonstrate my ability to analyze datasets and create a dynamic API based on the analysis results.

---

## Contents

- [Setup](#setup)
- [Files](#files)
- [Part 1: Climate Data Analysis](#part-1-climate-data-analysis)
  - [Precipitation Analysis](#precipitation-analysis)
  - [Station Analysis](#station-analysis)
- [Part 2: Climate API](#part-2-climate-api)
  - [Available Routes](#available-routes)
- [Reflections](#reflections)
- [References](#references)

---

## Setup

### Prerequisites

To run this project, ensure the following dependencies are installed:

- Python 3.7+
- Jupyter Notebook
- Flask
- SQLAlchemy
- Matplotlib
- Pandas

### Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sqlalchemy-challenge.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sqlalchemy-challenge
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the analysis in Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
5. Start the Flask API:
   ```bash
   python app.py
   ```

---

## Files

- `climate_starter.ipynb`: Contains the climate data analysis.
- `app.py`: Flask application for the Climate API.
- `Resources/`: Folder containing the following data files:
  - `hawaii_measurements.csv`
  - `hawaii_stations.csv`
  - `hawaii.sqlite`

---

## Part 1: Climate Data Analysis

### Precipitation Analysis

- Identify the most recent date in the dataset.
- Retrieve the last 12 months of precipitation data.
- Store the results in a Pandas DataFrame and create a line plot.
- Print summary statistics for the precipitation data.

### Station Analysis

- Determine the total number of weather stations.
- Identify the most active station based on observation counts.
- Calculate the minimum, maximum, and average temperatures for the most active station.
- Retrieve the last 12 months of temperature observations and plot a histogram.

---

## Part 2: Climate API

### Available Routes

Below are the Flask API routes I created as part of this challenge:

| Route | Description |
|-------|-------------|
| `/` | Homepage with an overview of available routes. |
| `/api/v1.0/precipitation` | JSON representation of the last 12 months of precipitation data. |
| `/api/v1.0/stations` | JSON list of all weather stations. |
| `/api/v1.0/tobs` | JSON list of temperature observations from the most active station for the last 12 months. |
| `/api/v1.0/<start>` | JSON list of TMIN, TAVG, and TMAX from the start date to the end of the dataset. |
| `/api/v1.0/<start>/<end>` | JSON list of TMIN, TAVG, and TMAX for the specified date range. |

---

## Reflections

This challenge helped solidify my understanding of:

1. Using SQLAlchemy ORM for database connections and queries.
2. Analyzing and visualizing data with Pandas and Matplotlib.
3. Building a Flask API to share analysis results dynamically.
4. Handling real-world datasets with missing or inconsistent data.

I found the process of querying and visualizing climate data particularly rewarding, and the ability to design an API felt like a meaningful application of the analysis.