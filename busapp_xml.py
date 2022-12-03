import json
import requests
from urllib.parse import urlencode
import xmltodict
import config

bus_infos = []

url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid"
service_key = config.SERVIDE_KEY
bus_station_id = 25143

params = {  "ServiceKey": service_key, 
            "arsId": bus_station_id
         }
         
encoded = urlencode(params).encode()
print(encoded)
response = requests.get(url, encoded)   # xml 타입
if response.status_code == 200:
    json_obj = json.loads( json.dumps( xmltodict.parse(response.text), ensure_ascii=False) )
    # dict_obj = xmltodict.parse(response.text)
    # pprint.pprint(json_obj)
    for bus in json_obj['ServiceResult']['msgBody']['itemList']:
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
