import csv
import json
import os


def make_url(url, params):

    temp = '?'
    count = 0
    for i in params:
        temp = temp + i + '=' + params[i]
        count = count + 1

        if count != (len(params)):    
            temp = temp + '&'

    return url + temp


def make_csv(data, fileName, info):
    # 지역정보조회_광역시_도
    if(info == 'location_info'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in items] # items은 값들을 item에 하나씩 넣어서 반복문돌려

        csv_file_path = f'{fileName}.csv'

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=["code", "name"])
            
            csv_file.seek(0, 2)
            file_empty = csv_file.tell() == 0
            
            if file_empty:
                csv_writer.writeheader()
            
            for row in filtered_data:
                csv_writer.writerow(row)
    # 지역정보조회_시군구
    elif(info == 'location_info_sub'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in items]

        csv_file_path = f'{fileName}.csv'

        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=["code", "name"])
            
            csv_file.seek(0, 2)
            file_empty = csv_file.tell() == 0
            
            if file_empty:
                csv_writer.writeheader()
            
            for row in filtered_data:
                csv_writer.writerow(row)
    # 지역기반정보조회_(예시_숙박)
    elif(info == 'locationBase_info_accom'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "title": item["title"],
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "contentid": item["contentid"],
                "firstimage": item["firstimage"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "tel": item["tel"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel","mapx", "mapy", "firstimage"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 위치기반정보조회
    elif(info == 'location_search_info'):
        data = json.loads(data)
        
        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "title": item["title"],
                "tel": item["tel"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "dist": item["dist"],           # 중심좌표로부터거리
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "contentid": item["contentid"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel", "mapx", "mapy", "dist", "cat1", "cat2", "cat3", "booktour"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 서비스분류코드조회
    elif(info == 'service_code'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "rnum": item["rnum"],
                "name": item["name"],
                "code": item["code"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["rnum", "name", "code"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 여행지 조회
    elif(info == 'locationBase_info'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]

        parsed_list = []

        for item in items:
            parsed_item = {
                "addr1 " : item["addr1"],
                }
    # 숙소정보조회
    elif(info == 'total_search_stay'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "benikia": item["benikia"],                 # 베니키아 여부(해당=1)
                "goodstay": item["goodstay"],               # 굿스테이 여부(해당=1)
                "hanok": item["hanok"],                     # 한옥 여부(해당=1)
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],             
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "title": item["title"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel", "mapx", "mapy", "mlevel", "modifiedtime", "contenttypeid", "firstimage", "firstimage2", "cat1", "cat2", "cat3", "booktour", "benikia","goodstay","hanok"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 행사정보조회
    elif(info == 'search_festival'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],
                "eventstartdate": item["eventstartdate"],       # 행사시작일
                "eventenddate": item["eventenddate"],           # 행사종료일
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "title": item["title"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "eventstartdate", "eventenddate", "addr1", "addr2", "tel", "mapx", "mapy", "mlevel", "modifiedtime", "contenttypeid", "firstimage", "firstimage2", "cat1", "cat2", "cat3", "booktour"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    