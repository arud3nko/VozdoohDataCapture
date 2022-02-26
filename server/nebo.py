import requests
import hashlib
import json
from datetime import datetime
#
api_code = ''
api_token = ''

# "id":"7cea1d2f-9f03-4056-97ed-29574e1f4d26","name":"АПН «Красноярск-Свердловский»"


def get_json_data():

    current_ts = str(int(datetime.now().timestamp()))

    api_hash_object = hashlib.sha1((current_ts+api_code).encode("ascii"))
    api_hash = api_hash_object.hexdigest()[5:16]

    request_header = {'X-Auth-Nebo': api_token}
    pars = {'hash': api_hash, 'time': current_ts}

    response = requests.get('https://nebo.live/api/v2/sensors/7cea1d2f-9f03-4056-97ed-29574e1f4d26', headers=request_header, params=pars)
    response = response.text

    data = json.loads(response)
    result = data['instant']['aqi']

    return result


def get_additional_data():

    current_ts = str(int(datetime.now().timestamp()))

    api_hash_object = hashlib.sha1((current_ts+api_code).encode("ascii"))
    api_hash = api_hash_object.hexdigest()[5:16]

    request_header = {'X-Auth-Nebo': api_token}
    pars = {'hash': api_hash, 'time': current_ts}

    response = requests.get('https://nebo.live/api/v2/sensors/7cea1d2f-9f03-4056-97ed-29574e1f4d26', headers=request_header, params=pars)
    response = response.text

    data = json.loads(response)
    result = data

    return result


def get_current_pollution():
    return int(get_json_data())


def main():
    print(get_additional_data())


if __name__ == '__main__':
    main()