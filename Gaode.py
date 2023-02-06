import requests
import sys
# 高德天气查询平台 https://lbs.amap.com/api/webservice/guide/api/weatherinfo
# 选择Web服务获取key 教程：https://blog.csdn.net/gz2580/article/details/111088190

key = 'xxxxxxxxxxxxxxxxxxxxxxx'
# adcode 城市编码表下载：https://lbs.amap.com/api/webservice/download
# 江夏区 420115
# 大同城区 140213
city = '101010100'

weather_url =  f'https://devapi.qweather.com/v7/weather/3d?location={city}&key=e47eeb840cac4e21a6e477d7d373b619'
def getWeather():
    weather_response = requests.get(weather_url)
    weather_response.encoding = "utf-8"
    return weather_response.json()
