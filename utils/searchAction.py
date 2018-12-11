# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 00:49:23 2018
@author: arjun
"""

from SRRMSv2.models.trainModel import *
from SRRMSv2.models.passengerModel import *
from SRRMSv2.models.stationModel import *
from flask import request , jsonify
import pandas as pd

def find_trains(data):
    from SRRMSv2.server import SQLSession
    sess = SQLSession()
    
    start_match = sess.query(ConsistsOf).filter_by(station_id = data['source_id']).all()
    dest_match = sess.query(ConsistsOf).filter_by(station_id = data['dest_id']).all()
    start_match = pd.DataFrame(start_match)
    dest_match = pd.DataFrame(dest_match)
    start_match.rename(columns={'stop_no':'source_no'})
    dest_match.rename(columns={'stop_no':'dest_no'})
    final = pd.merge(start_match , dest_match , how ='inner',on=['train_id'])
    final = final[  final['dest_no'] - final['source_no'] > 0 ]
    
    #LIST OF TRAIN_ID S THAT Traverse the ROUTE requested by the USER
    return final['train_id']