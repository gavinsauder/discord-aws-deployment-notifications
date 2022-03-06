#Python 3.8
#Make sure to add dependencies required for imports via lambda layer

import json
import requests

def lambda_handler(event, context):

    message = json.loads(event['Records'][0]['Sns']['Message'])
        
    url = "YOURDISCORDWEBHOOKURL"
    data = {'username': 'AWS Bot', 'content': message}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
