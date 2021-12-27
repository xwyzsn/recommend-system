# 基于UserCf的推荐系统实例(vue+flask)

## 介绍

推荐系统课设得前端,使用了简单的user -cf 作为推荐算法，flask后端，vue.js前端，做的一个简单的推荐系统。

### 数据集

数据集基于movielens-1m(ML-1M)[数据集地址](https://grouplens.org/datasets/movielens/1m/)

## 前端

基于一个基于vue.js的前端框架quasar，[官网地址](https://quasar.dev/)

### 概览

首页视频基于B站混剪，网站找不到了。。。

![image-20210422161848305](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422161848305.png)

下滑页面后选择喜欢的电影类型

![image-20210422161907092](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422161907092.png)

选择完类型后将从后端随机传输对应的类型电影数据展示如下

![image-20210422162107938](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422162107938.png)

选择感兴趣的电影,为了进一步的推荐

![image-20210422162153832](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422162153832.png)

选择完毕后则可进行推荐(后端获得推荐的电影信息)

![image-20210422162229532](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422162229532.png)

可以点击标题进入到IMDB中进行查看相关的电影信息

![image-20210422162306529](https://gitee.com/xwyzsn/Picture/raw/master/image-20210422162306529.png)



## 后端

基于flask实现的一个简单的API用于跑推荐算法和相关的API工作





## 推荐算法

基于user-cf的推荐算法，实现简单，但是效率不高，对于每一个新用户都需要重新计算其相似度从而进行推荐，待改善。



## TODO

1. 推荐算法待完善
2. 代码注释待加



## 代码

后端代码

```python
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

def read_data(path="./data/ml-1m/movies.dat"):
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

def read_csv(path="./data/ml-1m (2)/ml-1m/movie_poster.csv"):
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
        movie_url = read_csv(path="./data/ml-1m (2)/ml-1m/movie_url.csv")
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
        movie_url = read_csv(path="./data/ml-1m (2)/ml-1m/movie_url.csv")
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
    app.run(host='127.0.0.1',port=5000)

```





完整源码地址:[GitHub](https://github.com/xwyzsn/recommend-system).



