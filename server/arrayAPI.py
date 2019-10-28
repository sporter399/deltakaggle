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
c.execute('CREATE TABLE IF NOT EXISTS APPLICANTS (SeriousDlqin2yrs number,RevolvingUtilizationOfUnsecuredLines float, age number,NumberOfTime30to59DaysPastDueNotWorse number,DebtRatio float,MonthlyIncome number,NumberOfOpenCreditLinesAndLoans number,NumberOfTimes90DaysLate number,NumberRealEstateLoansOrLines number,NumberOfTime60to89DaysPastDueNotWorse number,NumberOfDependents number)')
conn.commit()
Applicants = trainDF

trainDF = DataFrame(Applicants, columns= ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30to59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines', 'NumberOfTime60to89DaysPastDueNotWorse', 'NumberOfDependents'])
trainDF.to_sql('APPLICANTS', conn, if_exists='replace', index = False)

c.execute('''  
SELECT * FROM APPLICANTS
          ''')
c.close()
d = conn.cursor()
"""
code above is rather verbose!
"""
eligible_applicants = []

@array_api.route('/user_vars', methods=['GET', 'POST'])
def serve_user_vars():
    
    age_var = (request.json["age_item"])
    income_var = (request.json["income_item"])
    d.execute("SELECT * FROM APPLICANTS WHERE age BETWEEN ? AND ? AND MonthlyIncome >= ?", (age_var[0], age_var[1], income_var[0]))
    eligible_applicants.append(d.fetchall())
    
    
    return jsonify({"items": eligible_applicants })

@array_api.route('/applicants', methods=['GET'])
def serve_all_applicants():
    
    return jsonify({"items": eligible_applicants })












