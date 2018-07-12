# -*- coding: utf-8 -*-
from os import path
import os
from wordcloud import WordCloud
import requests
import matplotlib.pyplot as plt
import jieba
import jieba.analyse


def get_content():
    file_name = "xiaoshuo.txt"
    d = path.dirname(__file__)
    content = open(path.join(d, file_name), encoding="utf8").read()
    # content = "我来到了北京清华大学"
    return content


def cut_content():
    # d = path.dirname(__file__)
    content = get_content()
    jieba.analyse.set_stop_words("stop_words.log")
    keywords = jieba.analyse.extract_tags(content)
    # keywords2 = jieba.cut(content, cut_all=False)

    print("/".join(keywords))
    # print("/".join(keywords2))


def makeCiyun(file_name):
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, file_name), encoding="utf8").read()
    # text = open(file_name).read().decode("utf8")

    # Generate a word cloud image
    font = os.path.join(os.path.dirname(__file__), "ziti.otf")
    # wordcloud = WordCloud(font_path=font).generate(text)
    # Display the generated image:
    # the matplotlib way:

    # plt.imshow(wordcloud)
    # plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40, font_path=font).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


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
    # makeCiyun(file_name)


# start("4213316")
# makeCiyun("jd_4912606.txt")
cut_content()
