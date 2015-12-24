#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import base64
import json
# httplib2.debuglevel = 1


class APIObj(object):

    '''
    This class is used for API related operation
    '''

    def __init__(self, urlBase=''):
        self.http = httplib2.Http()
        # self.http.add_credentials(username, password)
        if urlBase == '' or urlBase is None:
            urlBase = "http://127.0.0.1:5000"
        self.urlBase = urlBase

    def sendAPI(self, path, headers="", body=""):
        # auth = base64.encodestring(self.username + ':' + self.password)
        if headers == "":
            # headers = {
            #     "Content-Type": "application/octet-stream",
            # }
            # headers = {
            #     "Content-Type" : "text/plain"
            # }
            headers = {
                "Content-Type": "application/json",
            }
        else:
            headers = headers

        body = body
        url = self.urlBase + path
        print url
        response, data = self.http.request(url, "POST",
                                           headers=headers, body=body)
        print response
        return data

if __name__ == "__main__":
    apiObj = APIObj("http://sensoro-cloud.chinacloudapp.cn:8080")
    # apiObj = APIObj()
    api_path = "/device_test/000004/upload"
    # api_path = "/"
    # body = bytes(b'\0x05\0x97\0x01\0x64\0x01\0x13')

    # body = {"payload": '\0x05\0x97\0x01\0x64\0x01\0x13'}
    payload = {
        'accelerometer': [{
            'type': 'accelerometer',
            'upType': 'scheduleAck',
        }],
        'temperature': [{
            'type': 'temperature',
            'alarm': False,
            'upType': 'uploadData',
            'data': {'value': 10}
        }]
    }

#     payload = {
#         accelerometer: [ {
#             type:  'accelerometer', // 传感器类型
#             upType:  'removeSensor', // 移除传感器
#         } ]
#     }


#     payload = {accelerometer: [ {
#     type:  'accelerometer', // 传感器类型
#     alarm:  true, // 是否紧急上传
#     upType:  'uploadData', // 数据类型为 上传传感器数据
#     data:  { value:  356 }   // 传感器数据值
#       } ]
#     }
    data = apiObj.sendAPI(api_path, body=json.dumps(payload))
    print data
