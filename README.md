# recommendweb (recommendweb)

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



