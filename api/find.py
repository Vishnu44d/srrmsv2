from flask import request, Blueprint, jsonify
from SRRMSv2.models.trainModel import Train, TrainSpec
from SRRMSv2.models.passengerModel import Passenger
from SRRMSv2.utils.searchAction import find_trains

findBP = Blueprint('findApi', __name__)

@findBP.route('/', methods = ['POST'])
def get_trains():
    data = request.json
    #try:
    train_ids = find_trains(data)

    '''with open("some.txt", "w") as f:
        f.write(str(train_ids))'''
    if len(train_ids) != 0:
        from SRRMSv2.server import SQLSession
        session = SQLSession()
        trains = {}
        #try:
        for t in train_ids:
            train = session.query(Train).filter_by(train_id=t).first()
            train_ = session.query(TrainSpec).filter_by(train_id=t).first()
            trains[str(t)] = {"train_name": train.train_name, "train_type": train.train_type, "train_source_stn": train_.start_sid, "train_end_stn": train_.end_sid}
        response_object = {
            "status": "success",
            "data": trains
        }
        return jsonify(response_object), 200
    else:
        response_object = {
            "status": "fail",
            "message": "no trains in this route"
        }
        return jsonify(response_object), 401
