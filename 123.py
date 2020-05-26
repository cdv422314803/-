
import requests
from urllib.parse import urlencode
import json

def get_response(offset,limit):
    para = {'offset':offset,'limit':limit}
    musicurl = "http://music.163.com/api/v1/resource/comments/R_SO_4_506092019?"+urlencode(para)
    headers = {
        'Authority':'music.163.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':'_iuqxldmzr_=32; _ntes_nnid=87a0cd153c0aa4f8d9ace35924184d51,1587031929400; _ntes_nuid=87a0cd153c0aa4f8d9ace35924184d51; WM_TID=GGYh%2FU8pBmZAVFEAEFd6QzqxXoa47fsz; UM_distinctid=171953e87127fb-051500ace657ac-376b4502-1fa400-171953e87136e7; vinfo_n_f_l_n3=3c0b9fbab9803446.1.1.1587346843326.1587346848384.1589298054342; NTES_OSESS=MMSXReGgBGagxDAOKMGVaT8bJBh13RSZ8kgpbsUqYHyTkkrONDXewnEdxw6YMA8XTilyBwlWHTKZdjdmfr0lkAK60_M2jyEQwntRS.7eootXxKK6GZ6Cw_sG4aNJCZntR4sYOGvG1q9mC3jfG9xlm7MxvpcMqfO9uH1JznMAv08BPVOh_nGmLsZEhjYyS0_Du7VL3LtIG33Me2Zptu2suFGmfEQlKem4Z_NqE88C5zl0X; P_OINFO=b26a7dbf397cec4c4f032edb64bc37ce@tencent.163.com|1589371394|0|cc|00&99|null#0|null|cc_client&cc|b26a7dbf397cec4c4f032edb64bc37ce@tencent.163.com; JSESSIONID-WYYY=ZvyIYQSRa4fKRAUbVrKClm7eESn6CHCXS%2Fr%2FjZoPCS125XchvNnXv3xJ%2BEJTFrRWxr0tnluRX1Zl3ae5eaETEDAc9DvOrEqeZ8qgAMsNZEKlY0Re%2BP9JEbp5RoSz8BvXU7KSYozizr8fm%2BmSD9xalXeMKo6uOfDT5xsV%2FjPhUUotAA1E%3A1590466948456; WM_NI=0Ndj%2B7JotCCPj%2FRk3XqLT%2FbnzQFl0vR54nk4aU0BWGpZoWO9FHgO%2FVECSn%2B901K2Mh%2F5TDNWL6KDHM2YA5ADCbnLkd3h41fZPtHjsYN5mckS1IKRprdbcMnGYSCpQI8TYUQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91d36efbb6a894f55c95b88fa6c55b878b8f84b55d989cfab7ae4e8da7be99e62af0fea7c3b92af492ac8baa3d8ab1bca4c25caaf19e8cb254b3949cd0e166ba8f8a8db37e92ebfc8fea40a38b00a3d64db486a1b8ce338698a9b0ae5e879d9d8faa33f4ef85d3d064edeb9ca5cd5d90ea85a5cb47f2878fd6c45081bea2adea70f1b8fcd2e55294ac888bf2538eeba384ea59f39785b3f37aa8beadaeed4d9b8d8d91d443fc8c97b6d437e2a3',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    response = requests.post(musicurl,headers=headers)
    return response.content


def parse_return(gethtml):
    data = json.loads(gethtml)
    if data.get('comments'):
        comm = data['comments']
        for item in comm:
            data = {
                '用户名': item['user']['nickname'],
                '评论内容': item['content'],
                '评论时间': item['time'],
                '赞': item['likedCount']
            }
            print(data)
        print('-------------------------------------------------分割---------------------------------------------------------' )
def main(offset):
    gethtml = get_response(offset,10)
    parse_return(gethtml)

if __name__ == '__main__':
    for x in range(0,40):
        main(x*10)