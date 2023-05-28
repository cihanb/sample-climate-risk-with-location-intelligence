import requests
import json
from dotenv import load_dotenv
import os
import pandas
import uuid
import random

def get_cod_api_token(api_userID, api_password, api_tenantID):
    url = api_baseURL + '/sml/auth/v1/Login/implicit'
    data = {"username": api_userID,"password": api_password,"tenantname": api_tenantID}
    headers = {'Content-type': 'application/json', "Connection": "keep-alive"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    json_data = response.json()
    api_tokenID = (json_data['accessToken'])
    return api_tokenID

def kick_off_cod_lookup_job(api_tokenID, api_data):
    url = api_baseURL + '/cod/AppsServices/api/v1/score-facilities-impact/jobs'
    api_headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_tokenID, "Connection": "keep-alive", "Accept-Encoding": "gzip, deflate, br"}
    response = requests.post(url, data=json.dumps(api_data), headers=api_headers)
    json_data = response.json()
    api_jobID = (json_data['job_id'])
    return api_jobID

def get_cod_data(api_tokenID, api_jobID):
    url = api_baseURL + '/cod/AppsServices/api/jobs/' + str(api_jobID)
    api_headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_tokenID, "Connection": "keep-alive"}
    response = requests.get(url, headers=api_headers)
    while response.json()['status'] != 'FINISHED':
        response = requests.get(url, headers=api_headers)
    return response.json()

# load the .env file
load_dotenv()
api_baseURL = os.getenv("baseURL")
api_userID = os.getenv("userID")
api_password = os.getenv("password")
api_tenantID = os.getenv("tenantName")

# read random addresses
with open('sample-data/addresses-us-all.min.json') as f:
    data = [json.loads(line)['addresses'] for line in f]


# get cod api token
api_tokenID = get_cod_api_token(api_userID, api_password, api_tenantID)

# build cod climate job
api_job_data = {"m": "P.2023.1",
                    "rcp": "rcp8.5",
                    "th": "2030",
                    "facilities": []}
j=0
while (j<100):
    random_number = random.randint(1, 50)
    i = data[0][random_number]
    try:
        api_job_data['facilities'].append({
        "id": str(uuid.uuid4()),
        "name": str(uuid.uuid4()),
        "activity": "Office",
        "street1": i['address1'],
        "city": i['city'],
        "state": i['state'],
        "country": 'USA'
        })    
    except:
        # ignore errors and move to next line
        pass
    j=j+1
# kick off cod climate  job
api_jobID = kick_off_cod_lookup_job(api_tokenID, api_job_data)

# retrieve the results
cod_data = get_cod_data(api_tokenID, api_jobID)

# convert to pandas dataframe
df = pandas.json_normalize(cod_data, record_path=['output'])
df.to_csv('cod_output.csv', index=False)



