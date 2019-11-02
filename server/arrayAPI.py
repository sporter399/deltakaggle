from flask import Blueprint, jsonify, request
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
    beta_age = str(entered_age[0])
    print(type(entered_age))
    variable_instances = db.session.query(Variables).filter('25').all()
    print(variable_instances)
    """
    variable_items = [{"age": variable.age} for variable in variable_instances]
    
    new_age = request.json["age_item"]
    
    """
    
    


    return jsonify({"items": variable_items })

@array_api.route('/applicants', methods=['GET'])
def serve_all_applicants():
    
    return jsonify({"items": eligible_applicants })













