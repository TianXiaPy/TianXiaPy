#encoding utf-8

import os
import sys
import os.path as os_path


class LogFile(object):

    def __init__(self):
        self.log = ".log"

    def endswith(self, type):
        pass


if __name__ == "__main__":
    fp = open("./1215log.txt",encoding="utf-8")
    line_content = fp.readlines()
    print(ospath.abspath(""))
    print(line_content)
    for line in line_content:
        print(line)
    fp.close()
