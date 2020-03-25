# encoding with utf-8
# date:2020-03-22
# author:cyh
# copyright: TianxiaPy.ltd
import configparser
import os
import re
from typing import List

LogFileInfo = "LogInfo.cfg"
config = configparser.RawConfigParser()
config.read(LogFileInfo)


class LogConfigInfo(object):
    def __init__(self):
        self.logDir = config.get('LogDir', 'log_path')
        items = config.items("LogType")
        type_list = []
        for logItem in items:
            type_list.append(logItem[1])
        self.logTypes = type_list

    def dir(self) -> str:
        return self.logDir

    def target(self, target_file):
        for logType in self.logTypes:
            if re.search(logType, target_file):
                return True
            else:
                return False

if __name__ == "__main__":
    logConfig = LogConfigInfo()
    path = logConfig.dir()
    files = os.listdir(path)
    logConfig.target(files[0])
    #for file in files:
    #    if logConfig.target(file):
    #        print(file)



