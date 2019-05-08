import json
import boto3
import http.client
from botocore.vendored import requests
# from datetime import datetime
def lambda_handler(event, context):
    # TODO implement
    file = event['Records'][0]['s3']['object']['key']
    client_rek = boto3.client('rekognition')
    response = client_rek.detect_labels(
        Image={
            # 'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'image0428',
                'Name': event['Records'][0]['s3']['object']['key']
                # 'Version': 'string'
            }
        },
        MaxLabels=4,
        MinConfidence=70
    )
    
    # # print(r.text)
    labels = []
    for dic in response['Labels']:
        labels.append(dic['Name'])
    data = {"objectKey":event['Records'][0]['s3']['object']['key'],"bucket":'image0428',"createdTimestamp":event['Records'][0]['eventTime'],
        "labels":labels
    }
    url = 'https://vpc-photos-5hdiqbqrtxts3ck5ufcg45qgba.us-east-1.es.amazonaws.com/photos/photo'
    r = requests.post(url, json=data)
    
    # conn = http.client.HTTPSConnection('vpc-photos-5hdiqbqrtxts3ck5ufcg45qgba.us-east-1.es.amazonaws.com')
    # conn.request("GET", "/photos/_search?q=objectKey:%s"%('bird.jpg'))
    # res = conn.getresponse()   
    # rst = json.loads(res.read().decode('utf-8'))

    # return rst

