import json
from flask_restful import Resource
from flask import Response, request
import pymysql as sql

class get_items(Resource):
    def __init__(self, db_params):
        self.host_ = db_params['host']
        self.db_ = db_params['db']
        self.pass_ = db_params['password']
        self.user_ = db_params['user']
        print(self.user_)
        # def __init__(self, user='root', host='localhost', pw_='', db='derived', table_name="tmp_assoc"):
        # the connection to the database only has to occur once therefor, it can occur in the initialization
    def get(self):
        try:
            conn = sql.connect(user=self.user_, host=self.host_, db=self.db_, passwd=self.pass_)
            cursor = conn.cursor()
            query_row_string = """SELECT
            DISTINCT
            CASE WHEN LEFT(t1.item,1)='T'
            THEN t4.DRUG
            WHEN LEFT(t1.item,1)='O'
            THEN t3.LABEL
            ELSE t2.SHORT_TITLE END AS itemType
            FROM APIv1.items t1
            LEFT JOIN mimiciiiv14.D_ICD_DIAGNOSES t2 ON SUBSTRING(t1.item,3)  = t2.ICD9_CODE
            LEFT JOIN mimiciiiv14.D_LABITEMS t3 ON SUBSTRING(t1.item,3)  = t3.ITEMID
            LEFT JOIN mimiciiiv14.D_DRUGS t4 ON SUBSTRING(t1.item,3)  = t4.NDC
            ;"""
            cursor.execute(query_row_string)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')
            return response
        except:
             return "failed"
