from flask import request, Blueprint, jsonify
from SRRMSv2.utils.statusAction import cancelTicket

cancelBP = Blueprint('cancelApi', __name__)

'''@cancelBP.route('/', methods=['GET', 'POST'])
def get_trains():
    data = request.json
    #try:
        #return cancelTicket(find_trains(data))
    #except:
        response_object = {
            "ststus": "fail",
            "message": "error in statusAction"
        }
        return jsonify(response_object), 500'''
    
   