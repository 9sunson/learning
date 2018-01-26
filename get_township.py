# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_data(path, which=1):
    data_r = pd.read_csv(path)
    if which==1:
        return np.array(data_r.values[:, :2])
    elif which==2:
        return np.array(data_r.values)


def handel_data(data):
    url = 'http://restapi.amap.com/v3/geocode/regeo?'
    key = '6e69ab281347091d370dfe2d7404d172'
    for i in range(30760,31432):
        list_township = []
        for line in range(1*i, 1*(i+1)):
            loc = data[line]
            loc = loc.astype(np.str_)
            location = loc[0] + ',' + loc[1]
            para = {'key': key, 'location': location}
            r = requests.get(url, params=para)
            list_township.append(get_township(r.text))
        list_township = np.array(list_township)
        data_frame = pd.DataFrame(data=list_township)
        data_frame.to_csv('hi3.csv',mode='a+',header=False, index=False)


def get_township(response):
    township = json.loads(response)
    return township["regeocode"]["addressComponent"]["township"]


path = './input_430_train.csv'
path2 = './hi3.csv'
path3 = './address'
data = get_data(path2,which=2)
address_all = np.loadtxt(path3,dtype=np.str_)
address = list(address_all[:, 0])
address_index = list(address_all[:, 1])
dic = dict(zip(address, address_index))
address_code = []
data = data.astype(np.str_)
for i in data[:, 0]:
    code = dic.get(i)
    address_code.append(code)
data_frame = pd.DataFrame(address_code)
data_frame.to_csv('hi4.csv',mode='a+',header=False, index=False)