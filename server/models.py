from sql_alchemy_db_instance import db
import pandas as pd
import sqlite3
from sqlalchemy import Column, Integer, Float
import pandas as pd
import numpy as np
from pandas import DataFrame
from flask_sqlalchemy import SQLAlchemy



class Variables(db.Model):

    __tablename__ = 'APPLICANTS'
    id = db.Column(db.Integer, primary_key=True)
    dlqin2yrs =  db.Column(db.Integer)
    revolveUtil = db.Column(db.Float)
    age = db.Column(db.Integer)
    thirtySixtyPastDue = db.Column(db.Integer)
    debtRatio = db.Column(db.Float)
    monthlyIncome = db.Column(db.Integer)
    openCreditLines = db.Column(db.Integer)
    ninetyPastDue = db.Column(db.Integer)
    realEstateLines = db.Column(db.Integer)
    sixtyNinetyPastDue = db.Column(db.Integer)
    numberDependents = db.Column(db.Integer)




       