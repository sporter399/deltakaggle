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
statistics = []

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
    
    eligible_applicants.append([variable.id for variable in variable_instances])
    calculate_statistics(variable_instances)

    return jsonify({"items": eligible_applicants})

@array_api.route('/calculate_statistics', methods=['GET', 'POST'])
def calculate_statistics(variable_instances):

    total_age = []
    total_income = []
    total_revolveutil = []
    total_thirtysixty = []
    total_debttoincome = []
    total_opencreditlines = []
    total_overninety = []
    total_sixtyninety = []
    total_realestate = []
    total_dependents = []

    number_of_apps = db.session.query(Variables).count()
    percent_accepted = (((max(map(len, eligible_applicants)))/(number_of_apps) * 100))
    statistics.append({"Percentage accepted: " : "%.2f" % percent_accepted})

    for variable in variable_instances:
        total_age.append(variable.age)
        total_income.append(variable.MonthlyIncome)
        total_revolveutil.append(variable.RevolvingUtilizationOfUnsecuredLines)
        total_thirtysixty.append(variable.NumberOfTime30to59DaysPastDueNotWorse)
        total_debttoincome.append(variable.DebtRatio)
        total_opencreditlines.append(variable.NumberOfOpenCreditLinesAndLoans)
        total_overninety.append(variable.NumberOfTimes90DaysLate)
        total_realestate.append(variable.NumberRealEstateLoansOrLines)
        total_sixtyninety.append(variable.NumberOfTime60to89DaysPastDueNotWorse)
        total_dependents.append(variable.NumberOfDependents)

    average_age = sum(total_age)/len(total_age)
    statistics.append({"Average age of accepted: " : "%.2f" % average_age})
    average_income = sum(total_income)/len(total_income)
    statistics.append({"Average monthly income of accepted: " : "%.2f" % average_income})
    average_revolveutil = sum(total_revolveutil)/len(total_revolveutil)
    statistics.append({"Average revolving utilization of unsecured credit of accepted: " : "%.2f" % average_revolveutil})
    average_thirtysixty = sum(total_thirtysixty)/len(total_thirtysixty)
    statistics.append({"Average number of thirty to sixty day delinquencies of accepted: " : "%.2f" % average_thirtysixty})
    average_debttoincome = sum(total_debttoincome)/len(total_debttoincome)
    statistics.append({"Average debt to income ratio of accepted: " : "%.2f" % average_debttoincome})
    average_opencreditlines = sum(total_opencreditlines)/len(total_opencreditlines)
    statistics.append({"Average number of open credit lines of accepted: " : "%.2f" % average_opencreditlines})
    average_overninety = sum(total_overninety)/len(total_overninety)
    statistics.append({"Average number of delinquencies over ninety days of accepted" : "%.2f" % average_overninety})
    average_realestate = sum(total_realestate)/len(total_realestate)
    statistics.append({"Average number of real estate loans or lines of accepted: " : "%.2f" % average_realestate})
    average_sixtyninety = sum(total_sixtyninety)/len(total_sixtyninety)
    statistics.append({"Average number of sixty to ninety day delinquencies of accepted: " : "%.2f" % average_sixtyninety})
    average_dependents = sum(total_dependents)/len(total_dependents)
    statistics.append({"Average number of dependents of accepted: " : "%.2f" % average_dependents})

    return jsonify({"stats": statistics})


@array_api.route('/accepted_applicants', methods=['GET', 'POST'])
def serve_all_accepted():

   

    return jsonify({"items": eligible_applicants})

@array_api.route('/applicants_stats', methods=['GET', 'POST'])
def serve_statistics():

    return jsonify({"stats": statistics })







    