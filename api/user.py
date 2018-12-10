from flask import request, Blueprint, jsonify
from SRRMSv2.models.userModel import User
import uuid
import datetime
from SRRMSv2.models.userModel import db
import json
from SRRMSv2.auth.auth import validate_key, validate_user

userBP = Blueprint('userApi', __name__)

@userBP.route('/', methods=['GET', 'POST'])
def useraction():
    if request.method == 'POST':
        data = request.json
        if data['action'] == "add":
            return save_new_user(data=data)
    #elif request.method == 'GET':
        elif data['action'] == "get":
            if validate_key(data['key']):
                return get_all_users()
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'provide valid key',
                }
                return jsonify(response_object), 400



@userBP.route('/login', methods=['GET', 'POST'])
def userLogin():
    if request.method == 'POST':
        data = request.json
        return validate_user(data)


def save_new_user(data):
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    user = session.query(User).filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        try:
            session.add(new_user)
            session.commit()
        except:
            response_object = {
                'status': 'fail',
                'message': 'Problem occured in db',
            }
            return jsonify(response_object), 401

        finally:
            response_object = {
                'status': 'Ok',
                'message': 'User Created Successful',
            }
            return jsonify(response_object), 200

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return jsonify(response_object), 409


def get_all_users():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    users_ = session.query(User).all()
    users_ = [{"name": i.username, "email":i.email} for i in users_]
    if len(users_) == 0:
        response_object = {
            'status': 'success',
            'message': 'No user yer!' 
        }
    else:
        response_object = {
            'status': 'success',
            'users': users_
        }
    return jsonify(response_object), 200

