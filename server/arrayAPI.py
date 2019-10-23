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

sql_age = []
c.execute("SELECT age FROM APPLICANTS;")
result = c.fetchall()

ints_only = [item[0] for item in result] 


array = ['dogs', 'cats', 'chickens']

array_api = Blueprint('array_api', __name__)

for i in range(len(ints_only)):

    test_var = int(ints_only[i])

    if test_var < 24:
        sql_age.append(test_var)


@array_api.route('/array', methods=['GET'])
def serve_array():
    return jsonify({"animals": array}, {"applicants": sql_age})

@array_api.route('/todo', methods=['POST'])
def add_todo():
    array.append(request.json["item"])
    print(array)
    return jsonify(success=True) 