<template >
  <div >
    <q-layout class="q-layout">
      <q-header style="background: none;border: none"  reveal >
        <q-toolbar>

          <!-- <q-btn flat round dense label="图标" class="q-mr-sm" /> -->
        </q-toolbar>
      </q-header>



      <div class="section" style=" height:90vh;width:100%;"  >
        <div  style="z-index: -1;height:100%;width:100%;">
          <video ref="myvideo"  id="#myVideo"  tabindex="-1" style="height:100%;width:100%;object-fit: cover" autoplay loop >
            <source type="video/mp4" src="http://127.0.0.1:8081/pictures/marvel.webm" >
          </video>
        </div>


        <div class="center-div" style="font-size: 50px;color: #F2C037;font-family: KaiTi;text-align: center">
          推荐系统课设
          <br>
          <span style="font-size: 25px">来获得你的专属推荐吧!</span>
          <br>
          <span style="font-size: 25px" >大数据1801 庄志豪</span>
        </div>


        <a href="#section2">
          <div class="scroll-down center-in-center " style="margin-bottom: 2vh" >
          </div>

        </a>

      </div >
      <div class="section" id="section2">
        <div class="q-pa-md">
          <q-stepper
            v-model="step"
            header-nav
            ref="stepper"
            color="primary"
            animated
            keep-alive
          >
            <q-step
              style="height: 500px"
              :name="1"
              title="选择你喜欢的电影类型"
              caption="根据电影类型本系统将给您选择部分电影作为您的喜好继续推荐"
              icon="settings"
              :done="step > 1"
              :header-nav="step > 1"
            >
              <div class="q-gutter-sm">
                <q-checkbox keep-color v-model="checkArray.Action" label="Action" color="teal" />
                <q-checkbox keep-color v-model="checkArray.Adventure" label="Adventure" color="orange" />
                <q-checkbox keep-color v-model="checkArray.Animation" label="Animation" color="red" />
                <q-checkbox keep-color v-model="checkArray.Children" label="Children's" color="cyan" />
                <q-checkbox keep-color v-model="checkArray.Comedy" label="Comedy" color="teal" />
                <q-checkbox keep-color v-model="checkArray.Crime" label="Crime" color="orange" />
                <q-checkbox keep-color v-model="checkArray.Documentary" label="Documentary" color="red" />
                <q-checkbox keep-color v-model="checkArray.Drama" label="Drama" color="cyan" />
                <q-checkbox keep-color v-model="checkArray.Fantasy" label="Fantasy" color="teal" />
                <q-checkbox keep-color v-model="checkArray.Film_Noir" label="Film-Noir" color="orange" />
                <q-checkbox keep-color v-model="checkArray.Horror" label="Horror" color="red" />
                <q-checkbox keep-color v-model="checkArray.Musical" label="Musical's" color="cyan" />
                <q-checkbox keep-color v-model="checkArray.Mystery" label="Mystery" color="red" />
                <q-checkbox keep-color v-model="checkArray.Romance" label="Romance" color="cyan" />
                <q-checkbox keep-color v-model="checkArray.Sci_Fi" label="Sci-Fi" color="teal" />
                <q-checkbox keep-color v-model="checkArray.Thriller" label="Thriller" color="orange" />
                <q-checkbox keep-color v-model="checkArray.War" label="War" color="red" />
                <q-checkbox keep-color v-model="checkArray.Western" label="Western" color="cyan" />
              </div>

            </q-step>

            <q-step
              style="height: 500px"
              :name="2"
              title="选择你喜欢的电影"
              icon="create_new_folder"
              :done="step > 2"
              :header-nav="step > 2"
            >

              <q-infinite-scroll
                style="height: 500px;max-width: 100%;margin-left: 10%"
              >

                <template v-if="movie">
                <div  class="row" v-for="index in parseInt((movie.length/3))" :key="index"  >
                  <div class="col-3 q-ma-lg"  v-for="j in 3" :key="j"  >
                    <q-card class="my-card" >
                      <template v-if="3*(index-1)+j<movie.length">
                      <q-card-section  >
                        <a :href="movie[3*(index-1)+j]['movie_url']" target="_blank">{{movie[3*(index-1)+j]['name']}}</a>
                        <br>
                        <span style="color: grey">
                        {{movie[3*(index-1)+j]['types']}}
                          </span>
                      </q-card-section>
                      </template>
                      <template v-if="3*(index-1)+j<movie.length">
                      <q-card-section style="height: 75%">
                        <q-img height="95%" contain :src="movie[3*(index-1)+j]['url']"></q-img>
                        <q-checkbox v-model="options[3*(index-1)+j].value"></q-checkbox>
                      </q-card-section>
                      </template>
<!--                      <q-card-section style="margin-bottom: 2px">-->
<!--                        <q-checkbox v-model="options[3*(index-1)+j].value"></q-checkbox>-->
<!--                      </q-card-section>-->
                    </q-card>
                  </div>
                </div>
                </template>

              </q-infinite-scroll>


            </q-step>


            <q-step
              style="height: 500px"
              :name="3"
              title="获得推荐电影信息"
              icon="add_comment"
              :header-nav="step > 3"
            >
              <q-infinite-scroll
                style="height: 500px;max-width: 100%;margin-left: 10%"
              >

                <template v-if="recommend">
                  <div  class="row" v-for="index2 in parseInt((recommend.length/3))" :key="index2"  >
                    <div class="col-3 q-ma-lg"  v-for="j in 3" :key="j"  >
                      <q-card class="my-card" >
                        <template v-if="3*(index2-1)+j<recommend.length">
                          <q-card-section >
                            <a  :href="recommend[3*(index2-1)+j]['movie_url']" target="_blank">
                            {{recommend[3*(index2-1)+j]['name']}}
                            </a>
                            <br>
                            <span style="color: grey">
                        {{recommend[3*(index2-1)+j]['types']}}
                          </span>
                          </q-card-section>
                        </template>
                        <template v-if="3*(index2-1)+j<recommend.length">
                          <q-card-section style="height: 75%">
                            <q-img height="95%" contain :src="recommend[3*(index2-1)+j]['url']"></q-img>
                          </q-card-section>
                        </template>
                      </q-card>
                    </div>
                  </div>
                </template>

              </q-infinite-scroll>

            </q-step>
            <template v-slot:navigation>
              <q-stepper-navigation>
                <q-btn @click="getMoviePhoto" color="primary" label="Continue" v-if="step==1" />
                <q-btn @click="getRecommend" color="primary" label="Continue" v-if="step==2" />
                <q-btn @click="$refs.stepper.next()" color="primary" label="Continue" v-if="step==3" />
                <q-btn v-if="step > 1" flat color="primary" @click="$refs.stepper.previous()" label="Back" class="q-ml-sm" />
              </q-stepper-navigation>
            </template>
          </q-stepper>
        </div>

      </div>
      <q-footer style="background-color:#1f2329;text-align: center">
        <div style="color: #7b7e81">与我联系 +86 13819123757</div>
        <div style="color: #7b7e81">Copyright © 2021 xwyzsn  | All rights reserved</div>
      </q-footer>
    </q-layout>
  </div>
</template>

<script>

import axios from "axios";

export default {

  data () {
    return {
      step: 1,
      movie:[],
      group:[],
      options:[],
      // options:[{label:"Action",value:"Action"},
      //   {label: "Adventure",value: "Adventure"},
      //   {label: "Animation",value: "Animation"},
      //   {label: "Children's",value: "Children's"},
      //   {label: "Comedy",value: "Comedy"},
      //   {label: "Crime",value: "Crime"},
      //   {label: "Documentary",value: "Documentary"},
      //   {label: "Drama",value: "Drama"},
      //   {label: "Fantasy",value: "Fantasy"},
      //   {label: "Film_Noir",value: "Film-Noir"},
      //   {label: "Horror",value: "Horror"},
      //   {label: "Musical",value: "Musical"},
      //   {label: "Mystery",value: "Mystery"},
      //   {label: "Romance",value: "Romance"},
      //   {label: "Sci_Fi",value: "Sci-Fi"},
      //   {label: "Thriller",value: "Thriller"},
      //   {label: "War",value: "War"},
      //   {label: "Western",value: "Western"}
      //
      // ],
      checkArray:{
        Action: false,
        Adventure: false,
        Animation: false,
        Children: false,
        Comedy:false,
        Crime:false,
        Documentary:false,
        Drama:false,
        Fantasy:false,
        Film_Noir:false,
        Horror:false,
        Musical:false,
        Mystery:false,
        Romance:false,
        Sci_Fi:false,
        Thriller:false,
        War:false,
        Western:false},
      movie_length:0,
      show:false,
      recommend:[]
    }
  },

  methods:{
    getMoviePhoto(){
      if (this.step==1){
        var str = ""
        for (var i in this.checkArray){
          if(this.checkArray[i]==true){
            if (i=="Children"){
              i="Children's"
            }
            else if(i=="Sci_Fi"){
              i="Sci-Fi"
            }
            else if(i=="Film_Noir"){
              i="Film-Noir"
            }

            str+=i+"&"
          }
        }
        str=str.substr(0,str.length-1)

        const getData = async ()=>{
          // await fetch("http://localhost:5000/movie/"+str)
          //   .then(res=>res.json()).then(data=>{this.movie=JSON.parse(data)}).catch(err=>console.log(err))

          await axios.get("http://127.0.0.1:5000/movie/"+str)
           .then(res=>(this.movie=JSON.parse(res.data)))
             this.movie.unshift({"id":0,"url":"-1"})
              for(var i =0;i<this.movie.length;i++){
                  this.options.push({label:this.movie[i]["id"],value:false})
              }
          this.$refs.stepper.next()
        }
        getData()

      }

    },
    getRecommend(){

        var str=""
      if(this.options.length>0) {
        for (var i = 0; i < this.options.length; i++) {
          if (this.options[i]["value"] != undefined && this.options[i]["value"] != null) {
            if (this.options[i]["value"] != false) {
              str += this.options[i]["label"] + "&"
            }
          }
        }
      }
        str = str.substr(0,str.length-1)
        const getRecommendId = async ()=>{

        await axios.get("http://127.0.0.1:5000/recommend/"+str).then(res=>{
          this.recommend=JSON.parse(res.data)
          console.log(this.recommend)
          this.$refs.stepper.next()
          this.$q.loading.hide()
        })
        }
      this.$q.loading.show({
        message:'正在获取计算推荐信息,请稍等'
      })
      getRecommendId()

    }
  },
  mounted() {
    this.$nextTick(()=>{
      this.$refs.myvideo.volume=0.1
    })
  }
}
</script>
<style  >
html, body { scroll-behavior:smooth; }
.my-card{
  width: 100%;
  max-width: 500px;
  height: 500px;
  height: 100%;
}
.center-div{
  position: absolute;
  top: 50vh;
  left: 50%;

  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);

}

.center-in-center{
  position: relative;
  top: 95vh;
  left: 50vh;

  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);

}
#myVideo {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
}

.header{
  opacity: 1;

}
.section{
  min-height: 100vh;

}
.scroll-down {
  height: 50px;
  width: 30px;
  position: absolute;
  left: 50%;
  bottom: 5%;
  cursor: pointer;
}
.scroll-down::before,
.scroll-down::after {
  content: "";
  position: absolute;
  top: 20%;
  left: 50%;
  height: 10px;
  width: 10px;
  transform: translate(-50%, -100%) rotate(45deg);
  border: 2px solid black;
  border-top: transparent;
  border-left: transparent;
  animation: scroll-down 1s ease-in-out infinite;
}
.scroll-down::before {
  top: 30%;
  animation-delay: 0.3s;
  /* animation: scroll-down 1s ease-in-out infinite; */
}


@keyframes scroll-down {
  0% {
    /* top:20%; */
    opacity: 0;
  }
  30% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    top: 90%;
    opacity: 0;
  }
}
@keyframes scrollToRight {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}
</style>
