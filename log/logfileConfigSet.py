# encoding is utf-8
# copyright:TianXiaPy
# date:2020-03-22
# author:cyh

import configparser
config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('LogDir')
config.set('LogDir', 'log_path', 'C:\\Users\\MGF\\Documents\\GitHub\\TianXiaPy\\log')
config.add_section('LogType')
config.set('LogType', 'aiu_log1', '1.log')
config.set('LogType', 'aiu_log61', '61.log')
config.set('LogType', 'aiu_log62', '62.log')
config.set('LogType', 'aiu_log74', '74.log')
config.set('LogType', 'aru_log1', '1_au0.log')
config.set('LogType', 'aru_log61', '61_au0.log')
config.set('LogType', 'aru_log62', '62_au0.log')

# Writing our configuration file to 'example.cfg'
with open('LogInfo.cfg', 'w') as configfile:
    config.write(configfile)