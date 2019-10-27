from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import os
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
sql_data = []
required_age = []



@array_api.route('/age_var', methods=['GET', 'POST'])
def serve_age_var():
    
    var = [55]
    var.append(int(request.json["item"]))
    d.execute("SELECT * FROM APPLICANTS WHERE age BETWEEN ? AND ?", var)
    required_age = d.fetchall()
    print(required_age)
    
    """
    could it be back to the subject of scope on required age?
    """
    
    
    
    return jsonify(success = True)

@array_api.route('/applicants', methods=['GET'])
def serve_all_applicants():

    return jsonify({"items": required_age })












