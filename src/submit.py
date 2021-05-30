import json
import requests
import os

def submit(user_key='', file_path = ''):
    if not user_key:
        raise Exception("No UserKey" )
    url = 'http://ec2-13-124-161-225.ap-northeast-2.compute.amazonaws.com:8000/api/v1/competition/3/presigned_url/?description=&hyperparameters={%22training%22:{},%22inference%22:{}}'
    headers = {
        'Authorization': user_key
    }
    res = requests.get(url, headers=headers)
    print(res.text)
    data = json.loads(res.text)
    
    submit_url = data['url']
    body = {
        'key':'app/Competitions/000003/Users/{}/Submissions/{}/output.csv'.format(str(data['submission']['user']).zfill(8),str(data['submission']['local_id']).zfill(4)),
        'x-amz-algorithm':data['fields']['x-amz-algorithm'],
        'x-amz-credential':data['fields']['x-amz-credential'],
        'x-amz-date':data['fields']['x-amz-date'],
        'policy':data['fields']['policy'],
        'x-amz-signature':data['fields']['x-amz-signature']
    }
    requests.post(url=submit_url, data=body, files={'file': open(file_path, 'rb')})

test_dir = "/opt/ml/code/output" # 변경
user_key = "Bearer c283c44c3796b1715904ecc2e0e27660fe9bb1b4" # 변경
submit(user_key, os.path.join(test_dir, 'output.csv'))