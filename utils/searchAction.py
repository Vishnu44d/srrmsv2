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

    '''
    with open("some.txt", "w") as f:
        f.write(str(start_match))
        f.write(str(dest_match))
    '''
    start_match = [i.__dict__ for i in start_match]
    dest_match = [i.__dict__ for i in dest_match]

    start_match = pd.DataFrame(start_match)
    dest_match = pd.DataFrame(dest_match)

    start_match.to_csv('start_match.csv')
    dest_match.to_csv('dest_match.csv')

    start_match.rename(columns={'stop_no':'source_no'}, inplace=True)
    dest_match.rename(columns={'stop_no':'dest_no'}, inplace=True)
    
    final = pd.merge(start_match , dest_match , how ='inner',on=['train_id'])
    #final.to_csv("final.csv")
    #final = final.apply(pd.to_numeric)
    #final[['dest_no', 'source_no']] =  pd.to_numeric(final[['dest_no', 'source_no']])

    return valid_tid(final)

    #final = final[  final['dest_no'] - final['source_no'] > 0 ]
    #LIST OF TRAIN_ID S THAT Traverse the ROUTE requested by the USER
    #return final['train_id']
    


def valid_tid(final):
    ls=[]
    for i in final.iterrows():
        if int(i[1][6]) - int(i[1][2]) > 0 :
            ls.append(i[1][4])
    return ls