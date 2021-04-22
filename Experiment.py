import progressbar
from tqdm import tqdm

import metric
import util
import UserCf


class Experiment():
    def __init__(self,epoch,K,train_rate,N,model):
        self.epoch=epoch
        self.K=K
        self.N = N
        self.train_rate = train_rate
        self.model=model
    def get_train_test_data(self,train_rate):
        self.train, self.test = util.read_rating_data(train_rate=train_rate)
        self.t = dict()
        for user, item, _ in self.test:
            self.t.setdefault(user, list())
            self.t[user].append(item)

    def evaluate(self, N, K):
        recommens = self.model.recommend_test(self.t.keys(), N=N, K=K)
        all_items = util.all_items()
        item_popularity = metric.train_popularity(self.train)
        recall = metric.recall(recommends=recommens, tests=self.t)
        precision = metric.precision(recommends=recommens, tests=self.t)
        coverage = metric.coverage(recommends=recommens, all_items=all_items)
        popularity = metric.popularity(item_popular=item_popularity, recommends=recommens)

        return precision, recall, coverage, popularity

    def run(self):
        p=progressbar.ProgressBar()
        output =list()
        for i in p(range(self.epoch)):
            user_cf = self.model
            self.get_train_test_data(train_rate=self.train_rate)
            user_cf.train(data=self.train)
            output.append(self.evaluate(self.N,self.K))
        return output

