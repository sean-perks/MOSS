# MOSS Making Outstanding Solutions for Seeding
from flask import Flask, render_template, redirect, url_for, request

import pandas as pd
from Data import *


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    data = pd.read_csv(r"mysite/2025_needs.csv")
    fig = static_plot(data)
    graph_json = pio.to_json(fig)
    data = data.drop(["Normalized Size", "Seed Zone Ecoregion", "Text Position"], axis=1)

    table = data.to_html(classes='table table-striped', index=False)

    return render_template('index.html', graph_json=graph_json, table = table)


@app.route('/project/<proj_id>')
def project(proj_id):
    data = pd.read_csv(r"mysite/2025_needs.csv")
    data = data.drop(["Normalized Size", "Seed Zone Ecoregion"], axis=1)
    mhdf = data[data["Project"] == "Mount Hebo"]
    mpdf = data[data["Project"] == "Marys Peak"]
    proj_info = get_project_data(proj_id)
    proj_plant_info = get_project_plants(proj_id)

    mh_table = mhdf.to_html(classes='table table-striped', index=False)
    mp_table = mpdf.to_html(classes='table table-striped', index=False)

    return render_template('project.html', proj_info = proj_info, proj_plant_info = proj_plant_info, project_id = proj_id, lat = proj_info["Location"][0], lon = proj_info["Location"][1], mh_table=mh_table, mp_table=mp_table)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/pointonmap', methods=['GET', 'POST'])
def pointonmap():
    lat = None
    lon = None

    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']

    return render_template('pointonmap.html', lat=lat, lon=lon)



print("Welcome to MOSS")

if __name__ == "__main__":

    app.run(debug=True)
   