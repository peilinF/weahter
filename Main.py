import Gaode
import WeChat

# 微信id列表 给谁发加谁
wx_id = ["oTHVk6HT36zza7ettY_Z9RnNIJoM","oTHVk6BpKArCbX3Zi6EHq504vf_s"]
# 模板消息id
template_id = 'gCmzvR82QGq2eCsiDmE3uqyTSi5kCMcNd6Dw3YUTWSM'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)
