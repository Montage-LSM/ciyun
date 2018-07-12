# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import sys
import pprint
# reload(sys)
# sys.setdefaultencoding('utf8')


def init_comments(p_id):
    handler = open(str(p_id) + ".txt", encoding="utf8")
    done = True
    comments = list()
    while done:
        line = handler.readline()
        if line == "":
            done = False
            break
        temp = line.strip().split(" @ ")
        temp_dict = {
            'creationTime': temp[0],
            'content': temp[1],
            'days': temp[2],
            'nickname': temp[3],
            'productColor': temp[4],
            'productSize': temp[5],
            'score': temp[6],
            'referenceTime': temp[7],
            'userClient': temp[8],
            'userClientShow': temp[9],
            'userLevelName': temp[10],
            'format_date': datetime.datetime.strptime(temp[7], '%Y-%m-%d %H:%M:%S')
        }
        comments.append(temp_dict)
    return comments
