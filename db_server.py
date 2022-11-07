# db_server.py
'''
Database format
[{
'name': <string>
'id': <integer>
'blood_type': <string>
'test_name': [<string1>, <string2>, ...]
'test_result': [<string1>, <string2>, ...]
}]
'''

from flask import Flask, request, jsonify
import logging
from pymodm import connect, MongoModel, fields
from db_definition import Patient

app = Flask(__name__)

db = []

@app.route('/', methods=['GET'])
def server_on():
    return 'DB server is on'


def init_server():
    #add_patient('Ann Ables',1,'A+')
    #add_patient('Bob Boyles',2,'B+')

    # initialize logging
    logging.basicConfig(filename='server.log', filemode = 'w')
    connect("mongodb+srv://ruotongli547:990501lrt@bme547.bmhv3kr.mongodb.net/health_db?retryWrites=true&w=majority")


def add_patient(patient_name, patient_id, blood_type):
    new_patient = Patient(name = patient_name,
                          id = patient_id,
                          blood_type = blood_type)
    added_patient = new_patient.save()
    return added_patient


@app.route('/new_patient', methods=['POST'])
def add_new_patient():
    '''
    Receive data from post request
    Call other functions to do all the work
    Return information
    '''
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


@app.route('/add_test', methods=['POST'])
def add_test():
    in_data = request.get_json()
    message, status_code = add_new_test_worker(in_data)
    return message, status_code


def find_patient(id):
    from pymodm import errors as pymodm_errors
    try:
        found_patient = Patient.objects.raw({'_id': id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return found_patient


def add_new_test_worker(in_data):
    result = validate_test(in_data)
    if result is not True: 
        return result, 400
    
    patient = find_patient(in_data['id'])
    if patient is False:
        return 'Patient ID {} not found in database.'.format(in_data['id']), 400
    patient.test_name.append(in_data['test_name'])
    patient.test_result.append(in_data['test_result'])
    patient.save()
    return 'Test successfully added', 200

def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    
    add_patient(in_data['name'],
                in_data['id'],
                in_data['blood_type'])
    return 'Patient successfully added', 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return 'POST data was not a dictionary'
    expected_keys = ['name','id','blood_type']
    for key in expected_keys:
        if key not in in_data:
            return 'Key {} is missing from POST data'.format(key)
    expected_type = [str,int,str]
    for key,ex_type in zip(expected_keys,expected_type):
        if type(in_data[key]) is not ex_type:
            return "Key {}'s value has the wrong data type".format(key)
    return True


def validate_test(in_data):
    expected_keys = ['id', 'test_name','test_result']
    expected_types = [int, str, int]
    for ex_key, ex_type in zip(expected_keys,expected_types):
        if ex_key not in in_data:
            return 'Key not in'
        if type(in_data[ex_key]) is not ex_type:
            return 'Key type is wrong'
    return True

if __name__ == '__main__':
    init_server()
    app.run()