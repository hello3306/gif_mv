"""
@file: downloadMove.py
@time: 2019-06-19 13:14
"""
import json
import os
from urllib import request
import requests

size = "5"
url = "https://www.soogif.com/hotGif?start=0&size=" + size
data = requests.get(url)
data = json.loads(data.text)
data = data["data"]['result']

for i in data:
    gifurl = i['gifurl']
    likeNum = i["likeNum"]
    label = i["label"]
    title = i['title']
    sid = i['sid']
    file = str(title) + '.gif'
    localPath = os.path.join('D:/360MoveData/Users/Administrator/Desktop/mv/download/gif', file)
    # 下载gif图片
    request.urlretrieve(gifurl, localPath)
