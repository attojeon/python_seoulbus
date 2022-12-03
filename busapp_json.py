'''
제목: 정류장 버스 도착정보 앱
설명: 정류장코드를 사용하여 도착 버스 정보를 알아낸다.
입력: 정류장 코드
    - 강남역12번출구:23284
    - 강남역: 22339
출력: 
    - 도착 버스 정보들

'''
import requests
from urllib.parse import urlencode
import config
import pprint 

bus_infos = []

url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid"
service_key = config.SERVIDE_KEY
# bus_station_id = 25143
bus_station_id = int( input("--- 버스정류장 코드>>> "))

params = {  "ServiceKey": service_key, 
            "arsId": bus_station_id, 
            "resultType": "json"
         }
         
encoded = urlencode(params).encode()
print(encoded)
response = requests.get(url, encoded)   
if response.status_code == 200:
    json_obj = response.json()
    pprint.pprint(json_obj)
    for bus in json_obj['msgBody']['itemList']:
        bus_num = bus['rtNm']
        arrival_msg1 = bus['arrmsg1']
        arrival_msg2 = bus['arrmsg2']
        bus_direction = bus['adirection']
        new_bus = { "버스": bus_num,
                    "도착메시지1": arrival_msg1,
                    "도착메시지2": arrival_msg2,
                    "방향": bus_direction
                    }
        bus_infos.append(new_bus)

    print(bus_infos)

else:
    print("query error...")


'''
# 참조 문서: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000303
#   - 제공상세문서의 각종 코드 값을 반드시 참조해야 함. 
'''
