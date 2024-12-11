# MOSS Making Outstanding Solutions for Seeding
from flask import Flask, render_template, redirect, url_for
import pandas as pd
from Data import *

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/project/<proj_id>')
def project(proj_id):
    proj_info = get_project_data(proj_id)
    proj_plant_info = get_project_plants(proj_id)
    return render_template('project.html', proj_info = proj_info, proj_plant_info = proj_plant_info, project_id = proj_id, lat = proj_info["Location"][0], lon = proj_info["Location"][1])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


print("Welcome to MOSS")

if __name__ == "__main__":

    app.run(debug=True)
   