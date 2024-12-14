
from re import A
from flask import Flask,render_template, flash,request,redirect,url_for,jsonify
import gestion_avions.db  as db
import gestion_avions.avion as avion
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from datetime import datetime
from gestion_avions.avion import insert_avion
import sqlite3
app=Flask(__name__)
app.config['SECRET_KEY']='KingCrimson'

DB_PATH = "gestion_avions.db"

db.get_connection()



@app.route('/')

def index():
    word="fly"
    return render_template("index.html",wordused=word)





  # Required for CSRF protection
@app.route('/add_avion', methods=['GET', 'POST'])
def add_avion():
    if request.method == 'POST':
        # Retrieve form data
        numav = request.form['numav']
        typav = request.form['typav']
        datms = request.form['datms']
        nbhddrev = request.form['nbhddrev']
        datrev = request.form['datrev']
        actif = 1 if 'actif' in request.form else 0  # If checkbox is checked, actif is 1, else 0

        # Insert into the database
        avion.insert_avion(numav,typav,datms,nbhddrev,datrev,actif)

        

    return render_template('add_avion.html')
@app.route('/perform_action', methods=['POST'])
def perform_action():
     plane_id = request.json.get('planeId')
     avion.delete_avion(plane_id)
     return jsonify({"message": "Action performed successfully", "planeId": plane_id})
@app.route('/user/<name>')
def user(name):

    return render_template("user.html",user_name = name) 
#errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/planeshow', methods=['GET', 'POST'])
def showp():
    try:
        planes = avion.retrieve_avions()  # Fetch all rows from Avions table
    except Exception as e:
        planes = []  # Handle errors gracefully
        print(f"Error retrieving planes: {e}")
    return render_template("show_plane.html", planes=planes)


@app.route('/name',methods=['GET','POST'])
def name():
    name =None
    form =testform()
    if form.validate_on_submit():
        
        name = form.name.data
        form.name.data = ''
        flash ("data inserted succefully")
    return render_template("name.html",name=name,form=form) 
    
