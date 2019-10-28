from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import sqlite3

array_api = Blueprint('array_api', __name__)

trainDF = pd.read_csv('cs-test.csv')

conn = sqlite3.connect('applicant_info.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS APPLICANTS (SeriousDlqin2yrs number,RevolvingUtilizationOfUnsecuredLines float, 
            age number,NumberOfTime30to59DaysPastDueNotWorse number,DebtRatio float,MonthlyIncome number,
            NumberOfOpenCreditLinesAndLoans number,NumberOfTimes90DaysLate number,NumberRealEstateLoansOrLines number,
            NumberOfTime60to89DaysPastDueNotWorse number,NumberOfDependents number)''')
conn.commit()
Applicants = trainDF

trainDF = DataFrame(Applicants, columns= ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 
                                        'NumberOfTime30to59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome', 
                                        'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines', 
                                        'NumberOfTime60to89DaysPastDueNotWorse', 'NumberOfDependents'])
trainDF.to_sql('APPLICANTS', conn, if_exists='replace', index = False)

c.execute('''  
SELECT * FROM APPLICANTS
          ''')
c.close()
d = conn.cursor()
"""
closing and reopening of curseor above was unwanted but necessary
"""
eligible_applicants = []

@array_api.route('/user_vars', methods=['GET', 'POST'])
def serve_user_vars():
    
    age_var = (request.json["age_item"])
    income_var = (request.json["income_item"])
    revolving_var = (request.json["revolving_item"])
    lessthansixty_var = (request.json["lessthansixty_item"])
    debtratio_var = (request.json["debtratio_item"])
    minlines_var = (request.json["minlines_item"])
    overninety_var = (request.json["overninety_item"])
    realestate_var = (request.json["realestate_item"])
    sixtyninety_var = (request.json["sixtyninety_item"])
    maxdependents_var = (request.json["maxdependents_item"])
    d.execute('''SELECT * FROM APPLICANTS WHERE age BETWEEN ? AND ? AND MonthlyIncome >= ? AND RevolvingUtilizationOfUnsecuredLines<=? 
                AND NumberOfTime30to59DaysPastDueNotWorse<=? AND DebtRatio <=? AND NumberOfOpenCreditLinesAndLoans>=? AND NumberOfTimes90DaysLate<=? 
                AND NumberRealEstateLoansOrLines>=? AND NumberOfTime60to89DaysPastDueNotWorse<=?
                AND NumberOfDependents<=?''', (age_var[0], age_var[1], income_var[0], revolving_var[0], lessthansixty_var[0], 
                debtratio_var[0], minlines_var[0], overninety_var[0], realestate_var[0], sixtyninety_var[0], maxdependents_var[0]))
    eligible_applicants.append(d.fetchall())


    print("Number of eligible applicants    "   + str(max(map(len, eligible_applicants))))
    percent_accepted = (((max(map(len, eligible_applicants)))/(len(Applicants)) * 100))
    print("Percent of applicants accepted:     " + "%.2f" % percent_accepted)

    return jsonify({"items": eligible_applicants })

@array_api.route('/applicants', methods=['GET'])
def serve_all_applicants():
    
    return jsonify({"items": eligible_applicants })













