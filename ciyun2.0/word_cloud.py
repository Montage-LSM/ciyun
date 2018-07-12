# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import sys
import function as fun
from PIL import Image
from wordcloud import WordCloud
import jieba
import jieba.analyse
# reload(sys)
# sys.setdefaultencoding('utf8')


def get_by_file():
    stop_list = dict()
    if len(stop_list) > 0:
        return
    files = open('stop_words.log', encoding="utf8")
    done = True
    while done:
        line = files.readline()
        # line = line.decode('utf-8')
        if line == "":
            done = False
            break
        words = line.strip('\n')
        if words in stop_list:
            continue
        stop_list[words] = True
    print(time.strftime("%H:%M:%S"))
    return stop_list


def cut(content):
    stop_list = get_by_file()

    content = "".join(content.split("\n"))
    content = "".join(content.split("\r"))
    content = "".join(content.split("\t"))

    c_list = jieba.cut(content)
    jieba.analyse.set_stop_words("./stop.txt")
    keywords = jieba.analyse.extract_tags(
        content, topK=100, withWeight=True, allowPOS=('n', 'vn', 'v'))
    temp = {}
    i = 0
    for kes in keywords:
        # print(kes[0])
        temp[kes[0]] = kes[1]
        i += 1

    return temp

    # return "\n".join(keywords)

    # n_words = list()
    # for c in c_list:
    #     if c in stop_list:
    #         continue
    #     n_words.append(c)
    # return n_words


def word_cloud(text):
    # print(text)
    # Read the whole text.

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="red",
                          mask=np.array(Image.open("./jiu.jpg")),
                          font_path='ziti.otf'
                          ).generate_from_frequencies(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def start():
    # comments = fun.init_comments("jd_4213316")

    comments = fun.init_comments("1682770")
    contents_list = [x['content'] for x in comments]
    # contents_list = open("./jd_4213316.txt", encoding="utf8")
    contents = " ".join(contents_list)
    text = cut(contents)
    print(text)
    # return
    # word_cloud(text)


start()
