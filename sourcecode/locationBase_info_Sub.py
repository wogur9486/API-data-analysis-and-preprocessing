import requests
from func_def import *

url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1"

params = {

    'serviceKey': 'DuNAHD53YMihcAYk251OZibIu7IxjIwuoPP365VnntZyBrwmHQqRhdA3Ed%2BiLCH5oasIn9aZGKE7LcITX8mVeA%3D%3D',
    'numOfRows':'10',       
    'pageNo':'1',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',
    '_type':'json',
    'listYN':'Y',
    'arrange':'A',
    'contentTypeId':'32',
    'areaCode':'4',
    'sigunguCode':'4'
#    'cat1':'B02',
#    'cat2':'B0201',
#    'cat3':'B02010100',
#    'modifiedtime':'20240721'

}

response = requests.get(make_url(url, params), verify= False)
print(response)

print(response.text)
if response.status_code ==200:
    make_csv(response.text, '여행지 조회', 'locationBase_info')
else:
    print(f'Error: {response.status_code}')