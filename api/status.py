from flask import request, Blueprint, jsonify
from SRRMSv2.models.trainModel import TrainStatus
from SRRMSv2.models.passengerModel import Passenger

statusBP = Blueprint('StatusAPI', __name__)

@statusBP.route('/', methods=['POST'])
def get_status():
    data = request.json
    return get_seat(data)



def get_seat(data):
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    train = session.query(TrainStatus).filter_by(train_id=data['train_id']).first()
    print(train.available_seat)
    if not train:
        response_object = {
            "status": "fail",
            "message": "train doesn't exist"
        }
        return jsonify(response_object), 400
    else:
        if train.available_seat == 0:
            response_object = {
                "status": "Success",
                "seat_available": "Not Available",
                "seat_wait": train.wait_seat
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                "status": "Success",
                "seat_available": train.available_seat,
            }
            return jsonify(response_object), 200


@statusBP.route('/pnr', methods=['POST'])
def get_pnr_status():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    data = request.json
    passanger = session.query(Passenger).filter_by(pnr=data['pnr']).first()
    if not passanger:
        response_object = {
            "status": "fail",
            "message": "Not a valid pnr"
        }
        return jsonify(response_object), 202
    else:
        if passanger.reserved_status == True:
            response_object = {
                "status": "success",
                "seat number": passanger.seat_number
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                "status": "success",
                "waiting number": passanger.seat_number
            }
            return jsonify(response_object), 200
    