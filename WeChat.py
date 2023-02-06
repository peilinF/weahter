import requests
import json
import datetime
import re

# APP的ID号
appID = 'wx8ae3c85f16bdcad3'
# 安全秘钥
appsecret = '73df2ec0f636b3910104d3e43215038e'
province  = '北京'
city = '北京市'
# 获取access_token
def getAccessToken():
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appID,
            "secret": appsecret
        }
    )
    print(r1.text)
    access_token = r1.json()['access_token']
    
    return access_token


# 发送天气提醒推送
def sendMessage(weatherData, wx_id, template_id):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # 在一起的日期
    togetherDay = datetime.date(2021, 10, 12)
    # 她的下一个生日

    #print(weatherData)
    today = datetime.date(int(year), int(month), int(day))
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    body = {
        "touser": wx_id,  # 推送消息的对象（用户微信id）
        "template_id": template_id,  # 模板ID
        "data": {
            'date': {
                'value': datetime.datetime.now().strftime('%Y-%m-%d'),
                'color': '#228B22'
            },
            'week': {
                'value': week_list[datetime.date(year, month, day).weekday()],
                'color': '#228B22'
            },
            'province': {
                'value': province,
                'color': '#FF6347'
            },
            'city': {
                'value': city,
                'color': '#FF6347'
            },
            'weather': {
                'value': weatherData['daily'][0]['textDay'],
                'color': '#FF8C00'
            },
            'tempMax': {
                'value': weatherData['daily'][0]['tempMax'] + '℃',
                'color': '#8A2BE2'
            },
            'tempMin': {
                'value': weatherData['daily'][0]['tempMin'] + '℃',
                'color': '#8A2BE2'
            },

            'humidity': {
                'value': weatherData['daily'][0]['humidity'] + '%',
                'color': '#FF69B4'
            },
            'winddirection': {
                'value': weatherData['daily'][0]['windDirDay'],
                'color': '#00BFFF'
            },
            'windpower': {
                'value': weatherData['daily'][0]['windSpeedDay'],
                'color': '#00BFFF'
            },
            'togetherDays': {
                'value': int(re.search('(?P<days>.*?) days', str(today.__sub__(togetherDay))).group('days')) + 1,
                'color': '#FF4500'
            },
            'hua': {  # 情话
                'value': '我是你最可爱的修勾',
                'color': '#FF0000'
            }
        }
    }

    r2 = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            "access_token": getAccessToken()
        },
        data=json.dumps(body)
    )

    print(r2.text)



