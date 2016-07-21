from ironSourceAtom import api
import json
import datetime
import random
import uuid
# data = {"mac_addr": "blabla2","first_seen": str(datetime.datetime.now()),"last_seen": str(datetime.datetime.now()),"insertion_time": str(datetime.datetime.now())}

# client.put_event(stream=stream, data=json.dumps(data), method="post")

def customer_dates_generator():
    """
    Generate random dates representing the first & last times a user was seen
    """
    first_seen = datetime.datetime(
        random.randint(2010, 2015),
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(0, 23),
        random.randint(0, 59)
    )

    time_to_add = datetime.timedelta(minutes=random.randint(0,59))
    last_seen = first_seen + time_to_add
    return {"first_seen": first_seen, "last_seen": last_seen}

def get_random_mac_addr():
    """
    Generate a random MAC address.
    To simplify things, we'll generate a UUID for now
    """
    return str(uuid.uuid4())

def get_user_data():

    random_dates = customer_dates_generator()
    data = {
        "mac_addr": get_random_mac_addr(),
        "first_seen": str(random_dates["first_seen"]),
        "last_seen": str(random_dates["last_seen"]),
        "insertion_time": str(datetime.datetime.now())
    }
    return data


client = api.AtomApi(url="http://track.atom-data.io/")
stream = "is_hackathon_tom.public.atom_wifi_data"

for i in xrange(100000):
    data = get_user_data()
    # print "Data to be inserted - " + str(data)

    r = client.put_event(stream=stream, data=json.dumps(data), method="post")
    if r.status_code != 200:
        print "Error!"
        print r.json()
        break
