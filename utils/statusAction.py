# -*- coding: utf-8 -*-
from SRRMSv2.models.trainModel import *
from SRRMSv2.models.passengerModel import *
from flask import request , jsonify
import re

def cancelTicket(data):
    from SRRMSv2.server import SQLSession
    
    sess = SQLSession()
    
    passenger = sess.query(Passenger).filter_by(pnr = data["pnr"]).first()
    if not passenger :
        response_object ={
                "status": "fail",
                "message": "PNR number not valid"
                }
        return jsonify(response_object) , 400
    else:
        # True : passenger is in confirmed status
        if passenger.reserved_status == True:
            
            try:
                book1 = sess.query(book1).filter_by(pnr = passenger.pnr).first()
                sess.query(Passenger).filter(passenger.pnr == data['pnr']).delete(synchronize_session = False)
                sess.query(book1).filter(book1.pnr == data['pnr']).delete(synchronize_session = False)
                sess.query(book2).filter(book2.pnr == data['pnr']).delete(synchronize_session = False)
                train_status = sess.query(TrainStatus).filter_by(train_id==book1.train_id).first()
                if train_status.wait_seat > 0:
                    passenger2 = sess.query(Passenger).filter_by(reserve_status == False ).first()
                    
                    
                else:
                    sess.query(TrainStatus).update({"available_seat":TrainStatus.available_seat+1},synchronize_session='evaluate')
                    #sess.query(update(train_status,values={train_status.available_seat:train_status.available_seat+1}))
        # passenger was in waiting list , before cancelling ticket
        else:
            try:
                sess.query(Passenger).filter(passenger.pnr == data['pnr']).delete(synchronize_session = False)
                sess.query(book1).filter(book1.pnr == data['pnr']).delete(synchronize_session = False)
                sess.query(book2).filter(book2.pnr == data['pnr']).delete(synchronize_session = False)
            except:
                ro = {
                        'status' : 'fail',
                        'message': 'could not cancel your ticket'
                        }
                return jsonify(ro),401
                
                
                

