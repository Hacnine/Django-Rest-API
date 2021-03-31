import json
import requests

URL = "http://127.0.0.1:8000/crud/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)

    r = requests.get(url=URL, headers=headers, data=json_data)

    data = r.json()
    print(data)


# get_data()


def post_data():
    data = {
        'name': 'Yasin',
        'roll': 111,
        'city': 'Bogura'
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    request = requests.post(url=URL, headers=headers, data=json_data)
    data = request.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id': 2,
        'name': 'Jabir',
        'roll': 103,
        'city': 'Meherpur'
    }
    headers = {'content-type': 'application/json'}

    json_data = json.dumps(data)
    req = requests.put(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)


# update_data()


def delete_data():
    data = {
        'id': 6,
    }
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    req = requests.delete(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)


delete_data()


