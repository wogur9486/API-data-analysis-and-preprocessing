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

    if(info == 'location_info'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in items]

        csv_file_path = f'{fileName}.csv'

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=["code", "name"])
            
            csv_file.seek(0, 2)
            file_empty = csv_file.tell() == 0
            
            if file_empty:
                csv_writer.writeheader()
            
            for row in filtered_data:
                csv_writer.writerow(row)
    
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