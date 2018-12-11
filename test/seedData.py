from SRRMSv2.models.stationModel import Station, ConsistsOf
from SRRMSv2.models.trainModel import TrainStatus, TrainSpec, Train
from flask import jsonify



#######################################################
########### GENERATING STSTAION DATA ##################
#######################################################


def generate_stations():
    with open("stations.txt", "r") as f:
        stn = f.read()

    stns = stn.split('\n')
    d = {}
    for s in stns:
        l = s.split('\t')
        d[l[0]] = l[1]
    return d


def save_changes_in_station():
    from SRRMSv2.server import SQLSession
    d = generate_stations()
    for st in d.keys():
        session = SQLSession()
        new_stn = Station(
            station_id = st,
            station_name = d[st]
        )
        session.add(new_stn)
        session.commit()

def get_all_stns():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    stns_ = session.query(Station).all()
    for s in stns_:
        print(s.station_id, s.station_name)

#save_changes_in_station()
#get_all_stns()



#######################################################
########### GENERATING TRAINS DATA ####################
#######################################################


def generate_trains():
    with open("trains.txt", "r") as f:
        t = f.read()

    trains = t.split('\n')
    all_trains = []
    for s in trains:
        l = s.split('\t')
        all_trains.append(l)
    return all_trains

def save_changes_in_trains():
    from SRRMSv2.server import SQLSession
    trains = generate_trains()
    for tr in trains:
        session = SQLSession()
        new_train = Train(
            train_id = tr[0],
            train_name = tr[1],
            train_type = tr[2]
        )
        session.add(new_train)
        session.commit()

def get_all_trains():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    trains = session.query(Train).all()
    for t in trains:
        print(t.train_id, t.train_name, t.train_type)

#save_changes_in_trains()
#get_all_trains()





#######################################################
########### GENERATING TRAIN-SPECS DATA ###############
#######################################################




def generate_trains_specs():
    with open("train_specs.txt", "r") as f:
        t = f.read()

    trains = t.split('\n')
    all_trains_specs = []
    for s in trains:
        l = s.split('\t')
        all_trains_specs.append(l)
    return all_trains_specs

def save_changes_in_train_specs():
    from SRRMSv2.server import SQLSession
    train_specs = generate_trains_specs()
    for tr in train_specs:
        session = SQLSession()
        new_train_spec = TrainSpec(
            train_id = tr[0],
            start_sid = tr[1],
            end_sid = tr[2]
        )
        session.add(new_train_spec)
        session.commit()

def get_all_train_specs():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    train_specs = session.query(TrainSpec).all()
    for t in train_specs:
        print(t.train_id, t.start_sid, t.end_sid)

#save_changes_in_train_specs()
#get_all_train_specs()




#######################################################
########### GENERATING ROUTE DATA #####################
#######################################################



def generate_consists_of():
    with open("routes.txt", "r") as f:
        t = f.read()

    trains = t.split('\n')
    all_trains_specs = []
    for s in trains:
        l = s.split('\t')
        all_trains_specs.append(l)
    return all_trains_specs



'''from SRRMSv2.server import SQLSession
sess = SQLSession()
sess.query(ConsistsOf).delete()
sess.commit()'''

def save_changes_in_consists_of():
    from SRRMSv2.server import SQLSession
    train_consistsof = generate_consists_of()
    for tr in train_consistsof:
        session = SQLSession()
        new_consistsof = ConsistsOf(
            train_id = tr[0],
            station_id = tr[1],
            stop_no = tr[2]
        )
        session.add(new_consistsof)
        session.commit()

def get_all_consistsof():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    train_consistsof = session.query(ConsistsOf).all()
    for t in train_consistsof:
        print(t.station_id, t.train_id, t.stop_no)

save_changes_in_consists_of()
get_all_consistsof()



#######################################################
########### TO REPOPULATE THE SEED DATA ###############
#######################################################

#### uncomment the following line:

'''
save_changes_in_consists_of()
save_changes_in_station()
save_changes_in_train_specs()
save_changes_in_trains()
'''

#### To test the commited seed Data uncomment the following line:

'''
get_all_consistsof()
get_all_stns()
get_all_train_specs()
get_all_trains()
'''

def generate_status():
    with open("statuss.txt", "r") as f:
        t = f.read()

    trains = t.split('\n')
    #print(trains)
    all_trains_specs = []
    for s in trains:
        l = s.split(',')
        all_trains_specs.append(l)
    return all_trains_specs

#print(generate_status())


def save_changes_in_tain_status():
    from SRRMSv2.server import SQLSession
    train_consistsof = generate_status()
    for tr in train_consistsof:
        session = SQLSession()
        new_consistsof = TrainStatus(
            wait_seat = int(tr[2]),
            train_id = tr[0],
            available_seat = int(tr[1])
        )
        session.add(new_consistsof)
        session.commit()

def get_all_train_status_():
    from SRRMSv2.server import SQLSession
    session = SQLSession()
    train_consistsof = session.query(TrainStatus).all()
    for t in train_consistsof:
        print(t.train_id, t.wait_seat, t.available_seat)

#save_changes_in_tain_status()
#get_all_train_status_()

