import os

path = os.getcwd()
files = os.listdir(path)
for file in files:
    print(file)