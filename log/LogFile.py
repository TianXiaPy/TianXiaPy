# encoding with utf-8
# date:2020-03-22
# author:cyh
# copyright: TianxiaPy.ltd
import configparser
from typing import List

LogFileInfo = "LogInfo.cfg"
config = configparser.RawConfigParser()
config.read(LogFileInfo)


class LogConfigInfo(object):
    def __init__(self):
        self.logDir = config.get('LogDir', 'log_path')
        self.logType = config.items("LogType")

    def get_log_dir(self) -> str:
        return self.logDir

    def get_log_type(self) -> List:
        return self.logType


if __name__ == "__main__":
    log = LogConfigInfo()



