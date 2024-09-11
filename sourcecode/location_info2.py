import csv
import json
import os
from func_def import *
import requests

# def make_url(url, params):

#     temp = '?'
#     count= 0 #파라미터의 갯수 세기위한 초기값

#     for i in params:
#         temp = temp + i + '=' + params[i] #url 만들어주기 위한 조건
#         count = count + 1 #파라미터를 세기 위한 조건

#         if count != (len(params)): #파라미터의 숫자와 같아지면 if문 빠져나옴
#             temp = temp + '&' #if문이 성립되면 이 식을 수행
    
#     return url + temp

# import requests


url = "https://apis.data.go.kr/B551011/KorService1/locationBasedList1"

#관광 타입 ID
contentTypeId = '15'



params = {
    #필수
    'serviceKey' : "QkiT9isHn%2FngYj7SJNBftK290c7SSWktGzgux4c8T%2Bu5%2BHox2jrUAqrY%2BdIjzM9XMSYrqLuzpU5V%2BvqTyvIs8Q%3D%3D",
    'MobileOS' : "ETC",
    'MobileApp' : "AppTest",
    'mapX' : '126.981611', # 나중에 INPUT으로 할꺼
    'mapY' : '37.567477',
    'radius' : '1000',

    # #선택
    '_type' : 'json',
    'contentTypeId' : contentTypeId,
    'numOfRows' : '10',
    'pageNo' : '1'
}

response = requests.get(make_url(url, params), verify=False)

response

if response.status_code == 200:
    make_csv(response.text, '위치기반_관광정보_조회2', 'location_search_info')
else:
    print(f'Error: {response.status_code}')



