import json
import boto3
import http.client
from botocore.vendored import requests
def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName='searchphotos',
        botAlias='beta',
        userId='test',
        inputText=event['q'],
    )
    keyword = response["slots"]
    seq = (keyword['typeone'],keyword['typetwo'])
    if keyword['typetwo']:
         arg = '+'.join(seq)
    else:
        arg = keyword['typeone']

    # client = boto3.client('lex-runtime')
    # response = client.post_text(
    #     botName='searchphotos',
    #     botAlias='beta',
    #     userId='test',
    #     inputText='show me person and bird',
    # )
    # keyword = response["slots"]
  
  
    # a = keyword["typeone"]
    # b = keyword["typetwo"]
    # if a == None:
    #     labellist = b
    # elif b == None:
    #     labellist = a
    # else:
    #     s = (a,b)
    #     labellist = "+".join(s)

    conn = http.client.HTTPSConnection('vpc-photos-5hdiqbqrtxts3ck5ufcg45qgba.us-east-1.es.amazonaws.com')
   
    
    conn.request("GET", "/photos/_search?q=labels:%s"%(arg))
    res = conn.getresponse()   
    rst = json.loads(res.read().decode('utf-8'))
    
    # print(event)
    # return event['']
    return rst
    # return a,b


