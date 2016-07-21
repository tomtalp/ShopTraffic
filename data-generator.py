from ironSourceAtom import api
import json
import datetime
import random
import uuid

def get_hour_weight(hour):
    """
    Give every hour range a differetn weight, so that we can replicate real
    customer data more accurately
    """
    if hour <= 8 or hour >= 22:
        return 5
    elif hour > 8 and hour <= 11:
        return 25
    elif hour > 11 and hour <= 14:
        return 100
    elif hour > 14 and hour <= 18:
        return 30
    else:
        return 15

def get_random_hour():
    """
    Generate a random hour, by our "hours-weight list". With the weight list we
    build a list of hours, in which the popular hours appear more often.
    Then with the random.choice function, the popular hours have a higher likelihood
    of getting selected.
    """
    weighted_choices = [hour for hour in range(0, 24)]
    hour_options = []
    for hour in range(0, 24):
        for weight in range(get_hour_weight(hour)):
            hour_options.append(hour)
    return random.choice(hour_options)


def _test_randomness():
    """
    A simple test to make sure we're getting real random values (simply
    by the look of the numbers :) )
    Get a random hour for 10,000 times, we expect to mostly get numbers
    between 12 and 14, which is supposed to be like real "store" data
    """
    stats = {}
    for i in xrange(10000):
        random_hour = get_random_hour()
        if random_hour in stats:
            stats[random_hour] += 1
        else:
            stats[random_hour] = 1


def customer_dates_generator():
    """
    Generate random dates representing the first & last times a user was seen
    """
    first_seen = datetime.datetime(
        random.randint(2010, 2015),
        random.randint(1, 12),
        random.randint(1, 28),
        # random.randint(0, 23),
        get_random_hour(),
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
