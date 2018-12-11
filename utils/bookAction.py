from SRRMSv2.models.trainModel import *
from SRRMSv2.models.passengerModel import *
from SRRMSv2.models.stationModel import *
from SRRMSv2.models.userModel import User
from flask import request , jsonify
import time

def generate_PNR(s):
    pnr = hash(s+str(time.time()))
    if pnr<0:
        pnr *= -1
    try:
        return pnr[-6:]
    except:
        return pnr
        

    
def book_ticket(data):
    from SRRMSv2.server import SQLSession
    sess = SQLSession()

    station_source = sess.query(Station).filter_by(station_name = data['source']).first()
    station_dest = sess.query(Station).filter_by(station_name = data['dest']).first()
    
    av = sess.query(TrainStatus).filter_by(train_id = data['train_id']).first()
    #if train can accomodate more passenger and is within capacity
    if av.available_seat > 0 :
        
        pnr_for_pass = generate_PNR(data['username'])
        new_pass = Passenger(
                pnr = pnr_for_pass,#generate_pnr(pnr_for_pass),
                p_name = data['pname'],
                reserve_status = True,
                age= data['age'],
                gender = data['gender'],
                seat_no = av.available_seat-1,
                start_sid = station_source.station_id,
                end_sid = station_dest.station_id
                )
        new_book1= Book1(
                #obtained from session: userId of the user booking the ticket for some passenger
                user_id = data['username'],
                pnr = pnr_for_pass,
                train_id = data['train_id']
                )
        new_book2= Book2(
                pnr = pnr_for_pass,
                date = data['date']
                )
        sess.query(TrainStatus).update({"available_seat":TrainStatus.available_seat-1},synchronize_session='evaluate')
        sess.add(new_pass)
        sess.add(new_book1)
        sess.add(new_book2)
        sess.commit()
        responce_object = {
            'Status': 'sucess',
            'message': 'conformed',
            'seat number': av.available_seat-1,
            'pnr': pnr_for_pass
        }
        return jsonify(responce_object), 200
    else :
        pnr_for_pass = generate_PNR(data['username'])
        new_pass = Passenger(
                pnr = pnr_for_pass,#generate_pnr(pnr_for_pass),
                p_name = data['pname'],
                reserve_status = False,
                age= data['age'],
                gender = data['gender'],
                seat_no = -1,
                start_sid = station_source.station_id,
                end_sid = station_dest.station_id
                )
        new_book1= Book1(
                #obtained from session: userId of the user booking the ticket for some passenger
                user_id = data['username'],
                pnr = pnr_for_pass,
                train_id = data['train_id']
                )
        new_book2= Book2(
                pnr = pnr_for_pass,
                date = data['date']
                )
        #sess.query(TrainStatus).update({"available_seat":TrainStatus.available_seat+1},synchronize_session='evaluate')
        sess.query(TrainStatus).update({"wait_seat":TrainStatus.wait_seat+1},synchronize_session='evaluate')
        sess.add(new_pass)
        sess.add(new_book1)
        sess.add(new_book2)
        
        sess.commit()
        responce_object = {
            'Status': 'sucess',
            'message': 'Waiting',
            'pnr': pnr_for_pass
        }
        return jsonify(responce_object), 202
        
        
def get_uid(name):
        from SRRMSv2.server import SQLSession
        sess = SQLSession()
        u = sess.query(User).filter_by(username = name)
        return str(u.username)