
import  random
import pandas as pd
import numpy as np
def train_popularity(train):
    """计算训练集的流行度"""
    train_popularity = dict()
    for user,item,_ in train:
        train_popularity.setdefault(item,0)
        train_popularity[item] += 1
    return train_popularity

def read_rating_data(path='H:/desktop/ml-1m/ml-1m/ratings.dat', train_rate=1.):
    train_list = list()
    test_list = list()
    data = pd.read_table(path, sep='::', header=None, engine='python')
    data = np.array(data)
    data = list(data)
    p = [train_rate, 1 - train_rate]
    for user, movie, rating, _ in data:
        value = np.random.choice([0, 1], p=p)
        if value == 0:
            train_list.append((user, movie, rating))
        else:
            test_list.append((user, movie, rating))

    return train_list, test_list


def all_items(path='H:/desktop/ml-1m/ml-1m/ratings.dat'):
    item = set()
    data = pd.read_table(path,sep='::',header=None,engine='python')
    data = list(np.array(data))
    for user,movie,rating,_ in data:
        item.add(movie)
    return item


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