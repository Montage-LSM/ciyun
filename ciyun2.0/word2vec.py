# coding:utf-8

import jieba.analyse as analyse
import jieba
from gensim.models import *
from gensim.models.word2vec import LineSentence,Text8Corpus
import multiprocessing

# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('./stop.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def getData():
    inputs = open('./jd_4213316.txt', 'r', encoding='utf-8')
    outputs = open('./output.txt', 'w')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()

def getModal():
    # inp="./output.txt"
    inp="/home/qlwb/Downloads/text8"
    # outp1 为输出模型
    outp1 = 'wiki.zh.text.model'
    # outp2为原始c版本word2vec的vector格式的模型
    outp2 = 'wiki.zh.text.vector'
    sentences = word2vec.Text8Corpus(inp)
    model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)

def start():
    outp2 = './wiki.zh.text.vector'
    model=KeyedVectors.load_word2vec_format(outp2,binary=False)
    # print(type(model))
    result=model.most_similar(['success'])
    print(result)
    # for item in result:
    #     print(item[0],item[1])


# start()
