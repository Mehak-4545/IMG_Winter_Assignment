import requests
import json

URL = "http://127.0.0.1:8000/candidateapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    
    r = requests.get(url = URL, data = json_data)

    data = r.json()

    print(data)

# get_data(5)


def post_data():
    data = {
        'candidate_id':'102',
        'enrollment_number':'21114035',
        'name':'Beth',
        'email':'123',
        'phone':'12345',
        'branch':'cse',
        'year':'2',
        'role':'dev',
        'cg':'9',
        'current_status':'interview',
        # 'RecruitmentSeason':'2017',
        # 'Round':'3',
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL,data=json_data)
    data = r.json()
    print(data)

post_data()


def update_data():
    data = {
        
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL,data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {
        # 'id':3
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL,data=json_data)
    data = r.json()
    print(data)

# delete_data()

