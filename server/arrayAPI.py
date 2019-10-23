from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import os
import sqlite3

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
code below is interesting:
cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
or
cursor.execute("INSERT INTO table VALUES (?, ?, ?)", (var1, var2, var3))
or
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)


"""


sql_data = []
var = ('48',)
c.execute("SELECT * FROM APPLICANTS WHERE age=?", var)
fetched_info = c.fetchall()


array = ['dogs', 'cats', 'chickens']

array_api = Blueprint('array_api', __name__)


@array_api.route('/array', methods=['GET'])
def serve_array():
    return jsonify({"animals": array}, {"applicants": fetched_info})

@array_api.route('/todo', methods=['POST'])
def add_todo():
    array.append(request.json["item"])
    print(array)
    return jsonify(success=True) 