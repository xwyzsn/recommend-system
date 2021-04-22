
import  random
import numpy as np
def train_popularity(train):
    """计算训练集的流行度"""
    train_popularity = dict()
    for user,item,_ in train:
        train_popularity.setdefault(item,0)
        train_popularity[item] += 1
    return train_popularity
def loadfile(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line


def read_rating_data(path='H:\desktop\ml-1m\ml-1m\\ratings.dat', train_rate=1.):
    """载入评分数据
        @param path:  文件路径
        @param train_rate:   训练集所占整个数据集的比例，默认为1，表示所有的返回数据都是训练集
        @return: (训练集，测试集)
    """
    trainset = list()
    testset = list()
    prob=[train_rate,1-train_rate]
    for line in loadfile(filename=path):
        user, movie, rating, _ = line.split('::')
        value=np.random.choice([0,1],p=prob)
        if value ==0:
            trainset.append([int(user), int(movie), int(rating)])
        else:
            testset.append([int(user), int(movie), int(rating)])
    print("train set len"+str(len(trainset))+"   test set len " +str(len(testset)))
    return trainset, testset


def all_items(path='H:\desktop\ml-1m\ml-1m\\ratings.dat'):
    """返回所有的movie"""
    items = set()
    for line in loadfile(filename=path):
        _, movie, _, _ = line.split("::")
        items.add(movie)
    return items


import os
import pickle


def save_file(filepath, data):
    """
        保存数据
        @param filepath:    保存路径
        @param data:    要保存的数据
    """
    parent_path = filepath[: filepath.rfind("/")]

    if not os.path.exists(parent_path):
        os.mkdir(parent_path)
    with open(filepath, "wb") as f:
        pickle.dump(data, f)


def load_file(filepath):
    """载入二进制数据"""
    with open(filepath, "rb") as f:
        data = pickle.load(f)
    return data


def open_text(filename,skip_row = 0):
    """打开文本文件
    :param filename: str
        文件名
    :param skip_row: int
         需要跳过的行数
    :return generator
        生成每一行的文本
    """
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i < skip_row:
                continue
            yield line