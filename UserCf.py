import math
import sys
from collections import defaultdict
from operator import itemgetter

import metric
import util
from util import load_file, save_file


class UserCf(object):
    def __init__(self):
        pass
    def train(self,data,matrix_path="./user_sim.pkl"):
        """
        训练方法,首先加载先用的相似度矩阵进行计算,若不存在则回重新计算相似矩阵
        可以使得预测快一点,在数据不发生变化的前提下
        :param data: 训练数据
        :param matrix_path:矩阵保存路径
        """
        self.data=data
        self.__init__data(data)
        print("training start ...")
        try:
            print("load local matrix..",file=sys.stderr)
            self.user_item_sim_matrix=load_file(matrix_path)
            print("load matrix finished")
        except BaseException:
            print("load fail ,try to calculate matrix",file=sys.stderr)
            self.user_item_sim_matrix=self.get_user_item_sim_matrix()

            print("save matrix ...",file=sys.stderr)
            # 由于在计算新用户的时候需要重新计算,故注释此行
            # save_file(matrix_path,self.user_item_sim_matrix)
            print("save finished")
    def __init__data(self,data):
        """
        获得训练所需的数据(user,item)集合
        :param data: 训练集数据
        """
        self.training = dict()
        for user,item,_ in data:
            self.training.setdefault(user,set())
            self.training[user].add(item)

    def get_user_item_sim_matrix(self):
        """
        获得user之间的相似度矩阵
        :return: 计算后的相似度矩阵
        """
        item_user=dict()
        for user ,items in self.training.items():
            for item in items:
                item_user.setdefault(item,set())
                item_user[item].add(user)

        user_sim_matrix=dict()
        N = defaultdict(int)
        for item , users in item_user.items():
            for u in users:
                N[u]+=1
                for v in users:
                    if u==v:
                        continue
                    user_sim_matrix.setdefault(u,defaultdict(int))
                    user_sim_matrix[u][v]+=1
        for u,related in user_sim_matrix.items():
            for v,support in related.items():
                user_sim_matrix[u][v]=support/math.sqrt(N[u]*N[v])

        return user_sim_matrix

    def recommend(self,user,N,K):
        """
        为单个用户推荐的方法
        :param user: 用户的ID
        :param N: 选取N个相似用户
        :param K: 推荐K个电影
        :return: 推进的电影ID集合
        """
        related = self.training.get(user,set)
        rec_set = dict()
        for v ,sim in sorted(self.user_item_sim_matrix.get(user,dict).items(),key=itemgetter(1),reverse=True)[:K]:
            for item in self.training[v]:
                if item in related:
                    continue
                rec_set.setdefault(item,0.)
                rec_set[item]+=sim
        return dict(sorted(rec_set.items(),key=itemgetter(1),reverse=True)[:N])


    def recommend_test(self,users,N,K):
        """
        在测试集合上推荐,调用recommend方法
        :param users: 用户的ID集合
        :param N: 选取N个相似用户
        :param K: 推荐K个电影
        :return: {(user_1,{ID_set}),(user_2,{ID_set_2})..}
        """
        rec_set = dict()
        for user in users:
            user_rec = list(self.recommend(user,N,K).keys())
            rec_set[user]=user_rec
        return rec_set

