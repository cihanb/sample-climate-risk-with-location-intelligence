import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_baseURL = os.getenv("baseURL")
api_userID = os.getenv("userID")
api_password = os.getenv("password")
api_tenantID = os.getenv("tenantName")

# Get access token
url = api_baseURL + '/sml/auth/v1/Login/implicit'
data = {"username": api_userID,"password": api_password,"tenantname": api_tenantID}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
json_data = response.json()
api_tokenID = (json_data['accessToken'])

# Kick off climate job
api_data = {"m": "P.2023.1",
        "rcp": "rcp8.5",
        "th": "2050",
        "facilities": [
            {"id": "1","name": "CA Office","activity": "Office","street1": "","city": "Newark","state": "CA","country": "USA","exposure_value": 10000000}
            ]}
url = api_baseURL + '/cod/AppsServices/api/v1/score-facilities-impact/jobs'
api_headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_tokenID}
response = requests.post(url, data=json.dumps(api_data), headers=api_headers)
json_data = response.json()
api_jobID = (json_data['job_id'])

# retrieve the results
url = api_baseURL + '/cod/AppsServices/api/jobs/' + str(api_jobID)
response = requests.get(url, headers=api_headers)
json_data = response.json()
print(json_data)
