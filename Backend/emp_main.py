import pymysql
import json
from app import app
from config import mydb
from flask import jsonify
from flask import flash, request

@app.route('/get', methods=['GET'])
def Get():
    return 'null'

@app.route('/insert', methods=['POST'])
def create_emp():
    try:
        json = request.json
        print(json)
        emp_id= json['emp_id']
        emp_name = json['emp_name']
        emp_age = json['emp_age']
        account = json['account']
        position = json['position']
        if emp_id and emp_name and emp_age and account and  position and request.method == 'POST':
            conn = mydb.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO employe(emp_id  , emp_name, emp_age, account,position) VALUES(%s, %s, %s, %s,%s)"
            bindData = (emp_id  , emp_name, emp_age, account,position)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
        return 'Exception'
    finally:
        cursor.close()
        conn.close()

@app.route('/emp', methods =['GET'])
def emp():
    try:
        conn = mydb.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT emp_id , emp_name, emp_age, account,position FROM employe")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e: 
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/empq/<emp_id>', methods=['GET'])
def emp_details(emp_id):
    try:
        conn = mydb.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT emp_id , emp_name, emp_age, account,position FROM employe WHERE emp_id =%s", (emp_id))
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update/<emp_id>', methods=['PUT'])
def update_emp(emp_id):
    try:
        _json = request.json
        print(_json)
        _emp_id = _json['emp_id']
        _emp_name = _json['emp_name']
        _emp_age= _json['emp_age']
        _account = _json['account']
        _position = _json['position']
        if _emp_name and _emp_age and _account and _position and  _emp_id and request.method  == 'PUT':           
            sqlQuery = ("UPDATE employe SET emp_name= %s, emp_age= %s, account= %s, position= %s WHERE emp_id=%s")
            bindData = ( _emp_name, _emp_age, _account, _position,_emp_id)
            conn = mydb.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery,bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            print(respone)
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close() 


@app.route('/delete/<emp_id>', methods=['DELETE'])
def delete_emp(emp_id):
    try:
        conn = mydb.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employe WHERE emp_id =%s",(emp_id))
        conn.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run()
