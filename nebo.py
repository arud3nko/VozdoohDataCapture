import requests
import hashlib
from datetime import datetime

api_code = 'Q8otgL7Cyvo7CitFtvJZuLzL'
api_token = 'BwJSyQaCCQLE3aEiy579A5J1'

current_ts = str(int(datetime.now().timestamp()))


api_hash_object = hashlib.sha1((current_ts+api_code).encode("ascii"))
api_hash = api_hash_object.hexdigest()[5:16]


request_header = {'X-Auth-Nebo': api_token}
pars = {'hash': api_hash}

response = requests.get('https://nebo.live/api/v2/cities', headers=request_header, params=pars)
print(response)