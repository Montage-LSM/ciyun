# -*- coding: utf-8 -*-
from os import path
import os
from wordcloud import WordCloud, STOPWORDS
import requests
import matplotlib.pyplot as plt
# from scipy.misc import imread
import numpy as np
from PIL import Image
import jieba
import jieba.posseg as pseg
import jieba.analyse


def makeCiyun(file_name):
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, file_name), encoding="utf8").read()
    jieba_info = jieba.cut(text, cut_all=True)

    font = os.path.join(os.path.dirname(__file__), "ziti.otf")
    imgmask = "255fk.jpg"
    alice_mask = np.array(Image.open(path.join(d, imgmask)))
    # lower max_font_size
    wordcloud = WordCloud(
        max_font_size=40, font_path=font, mask=alice_mask,
        stopwords=STOPWORDS
    ).generate(jieba_info)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file(path.join(d, "xiaoguo.png"))


import json


def getInfo(productId, page):
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv7667&productId=" + \
        productId + "&score=0&sortType=5&page=" + str(page) + "&pageSize=10&isShadowSku=0&fold=1"
    header = {
        'Host': 'club.jd.com',
        'Referer': "https://item.jd.com/" + productId + ".html"
    }
    content = requests.get(url, headers=header).content
    content = content[len("fetchJSON_comment98vv7667("):-2]
    # print(type(content))

    # open("li.txt", 'w').write(str(content))
    # print(content)
    content = json.loads((content).decode("GBK"))
    comments = content['comments']
    infos = ""
    for item in comments:
        # print(item['content'])
        # files.write(item['content'] + "\n")
        infos += item['content'] + "\n"
        # break
    return infos
    # print(content)
    # files.close()


def start(productId):
    file_name = "jd_" + productId + ".txt"
    try:
        os.remove(file_name)
    except Exception as ex:
        pass
    files = open(file_name, 'a', encoding="utf8")
    for i in range(100):
        infos = getInfo(productId, i)
        files.write(infos)
        print("finish", i)
        files.write("//*\n")
    files.close()
    makeCiyun(file_name)


# start("4213316")
makeCiyun("jd_4213316.txt")
