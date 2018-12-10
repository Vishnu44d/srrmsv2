from flask import Blueprint, request, jsonify
from SRRMSv2.auth.auth import validate_user, validate_key
from SRRMSv2.utils.bookAction import book_ticket

bookBP = Blueprint('bookApi', __name__)

@bookBP.route('/', methods=['GET', 'POST'])
def book():
    data = request.json
    _, s = validate_user(data)
    if s > 300:
        responce_object = {
            'Status': 'fail',
            'message': 'not a valid user'
        }
        return jsonify(responce_object), 400
    else:
        try:
            if validate_key(data['key']):
                book_ticket(data)
        except:
            pass

   