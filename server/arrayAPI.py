from flask import Blueprint, jsonify, request, render_template
import pandas as pd
import numpy as np
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import sqlite3
from models import Variables
from sql_alchemy_db_instance import db

array_api = Blueprint('array_api', __name__)

eligible_applicants = []

@array_api.route('/user_vars', methods=['GET', 'POST'])
def serve_user_vars():

    entered_age = request.json["age_item"]
    entered_income = request.json["income_item"]
    variable_instances = db.session.query(Variables).filter(Variables.age >= entered_age[0], Variables.age <= entered_age[1],
                            Variables.MonthlyIncome >= entered_income[0])
    eligible_applicants.append([{"age": variable.age, "MonthlyIncome": variable.MonthlyIncome} for variable in variable_instances])
    
    return jsonify({"items": eligible_applicants })

@array_api.route('/applicants', methods=['GET', 'POST'])
def serve_all_applicants():

    
    
    return jsonify({"items": eligible_applicants})

    