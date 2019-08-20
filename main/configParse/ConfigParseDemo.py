# coding: utf-8
import ConfigParser
import os
import numpy as np
import pandas as pd


# 2.x语法
def get_conf(section, key):
    conf_file = ConfigParser.ConfigParser()
    conf_file.read(os.path.join(os.getcwd(), 'config.ini'))
    return conf_file.get(section, key)


print get_conf('local', 'name')
print get_conf('local', 'address')
black = get_conf('local', 'black').split(',')
print black
# black = map(int, black)
df = pd.DataFrame(
    {'value': ['1', '2', '3', '4', '100', '200', '300'], 'rvalx': [4, 5, 4, 22, 2, 2, 4], 'rvaly': [2, 3, 5, 5, 6, 7, 8]},dtype=np.object)


value = df[~df['value'].isin(black)]
print value
