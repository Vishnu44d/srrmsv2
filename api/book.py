from flask import Blueprint, request, jsonify
from SRRMSv2.auth.auth import validate_user, validate_key, is_valid_user
from SRRMSv2.utils.bookAction import book_ticket

bookBP = Blueprint('bookApi', __name__)

@bookBP.route('/', methods=['GET', 'POST'])
def book():
    data = request.json
    s = is_valid_user(data)
    if s > 300:
        responce_object = {
            'Status': 'fail',
            'message': 'not a valid user'
        }
        return jsonify(responce_object), 400
    else:
        if validate_key(data['key']):
            return book_ticket(data)
        else:
            responce_object = {
                'Status': 'fail',
                'message': 'db error'
            }
            return jsonify(responce_object), 400

   