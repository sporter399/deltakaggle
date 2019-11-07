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
    entered_income = request.json["income_item"]
    entered_util = request.json["util_item"]
    entered_thirtysixty = request.json["thirtysixty_item"]
    entered_debtratio = request.json["debtratio_item"]
    entered_minopenlines = request.json["minlines_item"]
    entered_ninety = request.json["ninety_item"]
    entered_realestate = request.json["realestate_item"]
    entered_sixtyninety = request.json["sixtyninety_item"]
    entered_dependents = request.json["dependents_item"]
    variable_instances = db.session.query(Variables).filter(Variables.age >= entered_age[0], Variables.age <= entered_age[1],
                            Variables.MonthlyIncome >= entered_income[0], Variables.RevolvingUtilizationOfUnsecuredLines <= entered_util[0],
                            Variables.NumberOfTime30to59DaysPastDueNotWorse <= entered_thirtysixty[0], Variables.DebtRatio <= entered_debtratio[0],
                            Variables.NumberOfOpenCreditLinesAndLoans >= entered_minopenlines[0], Variables.NumberOfTimes90DaysLate <= entered_ninety[0],
                            Variables.NumberRealEstateLoansOrLines >= entered_realestate[0], Variables.NumberOfTime60to89DaysPastDueNotWorse <= entered_sixtyninety[0],
                            Variables.NumberOfDependents <= entered_dependents[0])
    eligible_applicants.append([{"age": variable.age, "MonthlyIncome": variable.MonthlyIncome} for variable in variable_instances])
    
    return jsonify({"items": eligible_applicants})

@array_api.route('/accepted_applicants', methods=['GET', 'POST'])
def serve_all_accepted():

    return jsonify({"items": eligible_applicants})





    