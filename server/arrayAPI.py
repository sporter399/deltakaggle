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

conn = sqlite3.connect('applicant_info.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS APPLICANTS (SeriousDlqin2yrs number,RevolvingUtilizationOfUnsecuredLines float, age number,NumberOfTime30to59DaysPastDueNotWorse number,DebtRatio float,MonthlyIncome number,NumberOfOpenCreditLinesAndLoans number,NumberOfTimes90DaysLate number,NumberRealEstateLoansOrLines number,NumberOfTime60to89DaysPastDueNotWorse number,NumberOfDependents number)')
conn.commit()
Applicants = trainDF

trainDF = DataFrame(Applicants, columns= ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30to59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate', 'NumberRealEstateLoansOrLines', 'NumberOfTime60to89DaysPastDueNotWorse', 'NumberOfDependents'])
trainDF.to_sql('APPLICANTS', conn, if_exists='replace', index = False)

c.execute('''  
SELECT * FROM APPLICANTS
          ''')

"""
c.close()
"""




sql_data = []
fetched_info = []
var = [55]

@array_api.route('/uservar', methods=['GET', 'POST'])
def serve_array():

    var.append(request.json["item"])
    print("var at line 42   "   + str(var))
    
    
    return jsonify(success=True)

@array_api.route('/fetched_info', methods=['GET'])
def server_all_fetched_info():
    
    return jsonify(success=True)

"""
The problem now is scope for the code below. It is possible not to get integers
from user but the placement, in the order of logic, for the SQL query is still 
unresolved
"""


c.execute("SELECT * FROM APPLICANTS WHERE age BETWEEN ? AND ?", var)
fetched_info = c.fetchall()


"""
THE CODE BELOW IS GOOD! It just isn't what is needed now. The fetched info var
must now find it's way into var array instaniated above

@array_api.route('/fetched_info', methods=['GET'])
def server_all_fetched_info():
    return jsonify({"items": fetched_info})

"""



