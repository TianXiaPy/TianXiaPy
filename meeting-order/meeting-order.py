_author_ = 'GavinHsueh'

import requests
import bs4
import urllib.request as url_request
import re
from distutils.filelist import findall


#要抓取的目标页码地址
url = 'https://www.imdb.com/chart/top?ref_=nv_ch_250_4'
#抓取页码内容，返回响应对象
page = url_request.urlopen(url)

contents = page.read()

soup = bs4.BeautifulSoup(contents, "html.parser")
print("IMDb电影TOP250"+"\n"+"影片名称                               评分                  连接")
for tag in soup.find_all('td','posterColumn'):
    #print(1)
    tag1 = soup.find("td", "ratingColumn imdbRating")
    print(tag1.find('strong').get("title"))
    movie_url=tag.find('a').get('href')
    movie_name = tag.find('img').get('alt')
    print(movie_name + "https://www.imdb.com"+ movie_url)
