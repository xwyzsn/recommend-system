import progressbar
from tqdm import tqdm

import metric
import util
import UserCf

class Experiment():
    def __init__(self,epoch,K,train_rate,N,model):
        """

        :param epoch: 运行的次数参数
        :param K: 最后推荐的个数
        :param train_rate: 训练集的占比
        :param N: 选择相似的N个用户进行推荐
        :param model: 使用的模型算法有user_cf或者item_cf两种
        """
        self.epoch=epoch
        self.K=K
        self.N = N
        self.train_rate = train_rate
        self.model=model
    def get_train_test_data(self,train_rate):
        """

        :param train_rate: train_rate 为训练集的占比,切分测试机和训练集
        """
        self.train, self.test = util.read_rating_data(train_rate=train_rate)
        self.t = dict()
        for user, item, _ in self.test:
            self.t.setdefault(user, list())
            self.t[user].append(item)

    def evaluate(self, N, K):
        """
        评估方法,调用Metric中的评估方法,对预测进行评估
        :param N: 选取N个相似的用户进行推荐
        :param K: 推荐K个物品
        :return: 准确率,召回率,覆盖率,流行度
        """
        recommens = self.model.recommend_test(self.t.keys(), N=N, K=K)
        all_items = util.all_items()
        item_popularity = metric.train_popularity(self.train)
        recall = metric.recall(recommends=recommens, tests=self.t)
        precision = metric.precision(recommends=recommens, tests=self.t)
        coverage = metric.coverage(recommends=recommens, all_items=all_items)
        popularity = metric.popularity(item_popular=item_popularity, recommends=recommens)

        return precision, recall, coverage, popularity

    def run(self):
        """
        定义了训练模型,将会运行epoch次数
        :return: 返回epoch次运行后的每次的结果的一个list集合
        """
        p=progressbar.ProgressBar()
        output =list()
        for i in p(range(self.epoch)):
            user_cf = self.model
            self.get_train_test_data(train_rate=self.train_rate)
            user_cf.train(data=self.train)
            output.append(self.evaluate(self.N,self.K))
        return output

