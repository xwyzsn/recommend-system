import json

from random import sample
from flask_cors import CORS
import numpy as np
import pandas as pd
from flask import Flask
from flask_restful import Api,Resource

import UserCf
from util import read_rating_data

app = Flask(__name__)
CORS(app,supports_credentials=True)
api = Api(app)

def load_file(filepath):
    """
    加载读入文件,将dat类型文件转为list输出
    :param filepath: 文件路径
    :return: 形如(user,movie,item)的list集合
    """
    data = pd.read_table(filepath,sep = '::',header=None,engine='python')
    data = np.array(data)
    data = data.tolist()
    return data

def read_data(path="H:\desktop\ml-1m\ml-1m\movies.dat"):
    """
    读入数据,返回user->{moive_id}集合和movie->{movie_id,movie_name,movie_types}集合
    :param path: 文件路径
    :return: data_dict:每个类型的电影对应的电影集合;movie_id_name_type每个电影的ID,name,和类型集合
    """
    data_dict=dict()
    data = load_file(path)
    movie_id_name_types=dict()
    for movie_id ,movie_name,movie_types in data:
        movie_id_name_types[movie_id]=[movie_name,movie_types]
        movie_type_list = movie_types.split("|")
        for movie_type in movie_type_list:
            if movie_type not in data_dict.keys():
                data_dict[movie_type]=set()
            else:
                data_dict[movie_type].add(movie_id)

    return data_dict,movie_id_name_types

def read_csv(path="H:/desktop/ml-1m (2)/ml-1m/movie_poster.csv"):
    """
    和read_data作用类似,只不过是读取电影对应的海报集合CSV
    :param path: 文件路径
    :return: 返回形如(movie_id,post_url)的一个list
    """
    data = pd.read_csv(path,header=None)
    data = np.array(data)
    data = data.tolist()
    return data

class Movie(Resource):
    def get(self,Movie_serise):
        """
        get方法,用户根据用户选择的电影,随机挑选一些电影给用户进行算法的进一步推荐
        :param Movie_serise: 从前端接受的电影类型ID序列
        :return: 用户选择的每一个type的电影30部相关电影组成的集合
        格式为Json
        """
        movie_list = Movie_serise.split("&")
        data,movie_detail_dict = read_data()
        movie_id_set=set()
        _data = read_csv()
        movie_url = read_csv(path="H:/desktop/ml-1m (2)/ml-1m/movie_url.csv")
        movie_url = dict(movie_url)
        for i in movie_list:
            movies = data.get(i)
            s = sample(list(movies),10)
            movie_id_set.update(s)
        l = list()
        for i in _data:
            if i[0] in movie_id_set:
                out = dict()
                out["id"]=i[0]
                out["url"]=i[1]
                out["movie_url"] = movie_url.get(i[0])
                out["name"]=movie_detail_dict.get(i[0])[0]
                out["types"]=movie_detail_dict.get(i[0])[1]
                l.append(out)


        return json.dumps(l)

class GetRecommend(Resource):
    def get(self,Movie_id_series):
        """
        根据前端传回来的用户喜欢的电影ID进行推荐
        :param Movie_id_series: 用户喜欢的电影序列
        :return: 推荐的电影信息(id,name,post_url,url)
        """
        id_list = Movie_id_series.split("&")
        model = UserCf.UserCf()
        train,test = read_rating_data(train_rate=0.1)
        l =list()
        for i in id_list:
            l.append([6041,int(i),5])
        total_data = train+l
        model.train(total_data)
        output = model.recommend(6041,30,10)
        output_list=list()
        data, movie_detail_dict = read_data()
        _data = read_csv()
        movie_url = read_csv(path="H:/desktop/ml-1m (2)/ml-1m/movie_url.csv")
        movie_url = dict(movie_url)
        for j in _data:
            if j[0] in output.keys():
                o=dict()
                o["name"] = movie_detail_dict.get(j[0])[0]
                o["types"] = movie_detail_dict.get(j[0])[1]
                o["id"] = j[0]
                o["url"] = j[1]
                o["movie_url"] = movie_url.get(j[0])
                output_list.append(o)

        return json.dumps(output_list)

api.add_resource(Movie,"/movie/<string:Movie_serise>")
api.add_resource(GetRecommend,"/recommend/<string:Movie_id_series>")
if __name__ == '__main__':
    app.run(debug=True)



