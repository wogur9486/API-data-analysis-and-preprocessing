import pandas as pd
import requests
import pprint
from pj1_test2 import make_url
from pj1_test2 import make_csv

url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1'

#관광타입
contentTypeId = '15'

params = {
    #한 페이지의 결과수
    'numOfRows' : "10",
    #페이지 넘버
    'pageNo' : "1",
    #OS 구분
    'MobileOS' : "ETC",
    #서비스명
    'MobileApp' : "AppTest",
    #인증키(서비스키)
    'serviceKey' : "QkiT9isHn%2FngYj7SJNBftK290c7SSWktGzgux4c8T%2Bu5%2BHox2jrUAqrY%2BdIjzM9XMSYrqLuzpU5V%2BvqTyvIs8Q%3D%3D",
    #X좌표
    'mapX' : "126.981611",
    #Y좌표
    'mapY' : "37.568477",
    #거리반경
    'radius' : "1000",
    
    'contentTypeId' : contentTypeId,
    '_type' : 'json',

}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    print(response.text)
    make_csv(response.text, '위치기반 관광정보 조희', 'location_info_accom')
else:
    print(f'Error: {response.status_code}')


