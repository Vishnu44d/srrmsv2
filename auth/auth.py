from SRRMSv2.config import key
from flask import request, jsonify
from SRRMSv2.models.userModel import User
from SRRMSv2.config import pub_key
from flask_bcrypt import Bcrypt

flask_bcrypt = Bcrypt()

def validate_key(user_key):
    if user_key == pub_key:
        return 1
    return 0


def validate_user(data):
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    user = session.query(User).filter_by(email=data['email']).first()
    if not user:
        responce_object = {
            'Status': 'fail',
            'message': 'no such user exist',
        }
        return jsonify(responce_object), 400
    else:
        if user.check_password(data.get('password')):
            responce_object = {
                'status': 'success',
                'key': pub_key
            }
            return jsonify(responce_object), 200
        else:
            responce_object = {
                'status': 'fail',
                'message': 'enter valid password/email'
            }
            return jsonify(responce_object), 400
        

