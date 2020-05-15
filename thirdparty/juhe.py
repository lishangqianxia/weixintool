#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import json
import requests
from urllib.parse import urlencode, quote
from utils import proxy
from pprint import pprint


def weather(cityname):
    '''
    :param cityname: 城市名字
    :return: 返回实况天气
    '''
    key = '1a887166b193e95fdd1dd0d892f2a0c7'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    print(data)
    result = data.get('result')
    sk = result.get('sk')
    response = {}
    response['temperature'] = sk.get('temp')
    response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('wind_strength')
    response['humidity'] = sk.get('humidity')  # 湿度
    response['time'] = sk.get('time')
    return response


def simpleWeather(cityname):
    key = '4f01e5d94ec76504320ebc495f85a211'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    r = requests.get(url=url, proxies=proxy.proxy())

    data = json.loads(r.text)
    result = data.get('result')
    city = result.get('city')
    realtime = result.get('realtime')

    response = {}
    response['city'] = city
    response['info'] = realtime.get('info') # 天气情况
    response['temperature'] = realtime.get('temperature') # 温度
    response['humidity'] = realtime.get('humidity') # 湿度
    response['direct'] = realtime.get('direct') # 风向
    response['power'] = realtime.get('power') # 风力
    response['aqi'] = realtime.get('aqi') # 空气质量指数
    return response


def stock(market, code):
    '''
    沪深股票
    :param market: 上交所 = sh, 深交所 = sz
    :param code: 股票编号
    :return:
    '''
    key = '02708795e48d71c5d79be64c688b5b23'
    api = 'http://web.juhe.cn:8080/finance/stock/hs'
    params = 'gid=%s&key=%s' % (market + code, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    data = data.get('result')[0].get('data')
    response = {
        'name': data.get('name'),
        'now_price': data.get('nowPri'),
        'today_min': data.get('todayMin'),
        'today_max': data.get('todayMax'),
        'start_price': data.get('todayStartPri'),
        'date': data.get('date'),
        'time': data.get('time')
    }
    response['is_rising'] = data.get('nowPri') > data.get('todayStartPri')
    sub = abs(float(data.get('nowPri')) - float(data.get('todayStartPri')))  # 差值
    response['sub'] = float('%.3f' % sub)
    return response


def constellation(cons_name):
    '''
    :param cons_name: 星座名字
    :return: json 今天运势
    '''
    key = '5d8aab86978ee09a8876112734dfa589'
    api = 'http://web.juhe.cn:8080/constellation/getAll'
    types = ('today', 'tomorrow', 'week', 'month', 'year')
    params = 'consName=%s&type=%s&key=%s' % (cons_name, types[0], key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    return {
        'name': cons_name,
        'text': data['summary']
    }


if __name__ == '__main__':
    # data = weather('深圳')
    data = simpleWeather('上海')
