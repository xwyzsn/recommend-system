(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[2],{"1e5b":function(e,t,r){},"2da0":function(e,t,r){"use strict";r("1e5b")},"713b":function(e,t,r){"use strict";r.r(t);var c=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("q-layout",{staticClass:"q-layout"},[r("q-header",{staticStyle:{background:"none",border:"none"},attrs:{reveal:""}},[r("q-toolbar")],1),r("div",{staticClass:"section",staticStyle:{height:"90vh",width:"100%"}},[r("div",{staticStyle:{"z-index":"-1",height:"100%",width:"100%"}}),r("div",{staticClass:"center-div",staticStyle:{"font-size":"50px",color:"#F2C037","font-family":"KaiTi","text-align":"center"}},[e._v("\n        推荐系统课设\n        "),r("br"),r("span",[e._v("\n          xwyzsn\n        ")]),r("br"),r("span",{staticStyle:{"font-size":"25px"}},[e._v("这是一个推荐系统的课设,前端使用vue,后端使用flask进行.详细项目可查看\n        "),r("a",{staticStyle:{"text-decoration":"none"},attrs:{href:"https://github.com/xwyzsn/recommend-system",target:"_blank"}},[e._v(" github")])]),r("br"),r("span",{staticStyle:{"font-size":"20px"}},[e._v("原剪辑视频太大这里不展示")])]),r("div",{staticClass:"scroll-down center-in-center ",staticStyle:{"margin-bottom":"2vh"},on:{click:function(t){return e.scrollDown()}}})]),r("div",{staticClass:"section",attrs:{id:"section2"}},[r("div",{staticClass:"q-pa-md"},[r("q-stepper",{ref:"stepper",attrs:{"header-nav":"",color:"primary",animated:"","keep-alive":""},scopedSlots:e._u([{key:"navigation",fn:function(){return[r("q-stepper-navigation",[1==e.step?r("q-btn",{attrs:{color:"primary",label:"Continue"},on:{click:e.getMoviePhoto}}):e._e(),2==e.step?r("q-btn",{attrs:{color:"primary",label:"Continue"},on:{click:e.getRecommend}}):e._e(),3==e.step?r("q-btn",{attrs:{color:"primary",label:"Continue"},on:{click:function(t){return e.$refs.stepper.next()}}}):e._e(),e.step>1?r("q-btn",{staticClass:"q-ml-sm",attrs:{flat:"",color:"primary",label:"Back"},on:{click:function(t){return e.$refs.stepper.previous()}}}):e._e()],1)]},proxy:!0}]),model:{value:e.step,callback:function(t){e.step=t},expression:"step"}},[r("q-step",{staticStyle:{height:"500px"},attrs:{name:1,title:"选择你喜欢的电影类型",caption:"根据电影类型本系统将给您选择部分电影作为您的喜好继续推荐",icon:"settings",done:e.step>1,"header-nav":e.step>1}},[r("div",{staticClass:"q-gutter-sm"},[r("q-checkbox",{attrs:{"keep-color":"",label:"Action",color:"teal"},model:{value:e.checkArray.Action,callback:function(t){e.$set(e.checkArray,"Action",t)},expression:"checkArray.Action"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Adventure",color:"orange"},model:{value:e.checkArray.Adventure,callback:function(t){e.$set(e.checkArray,"Adventure",t)},expression:"checkArray.Adventure"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Animation",color:"red"},model:{value:e.checkArray.Animation,callback:function(t){e.$set(e.checkArray,"Animation",t)},expression:"checkArray.Animation"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Children's",color:"cyan"},model:{value:e.checkArray.Children,callback:function(t){e.$set(e.checkArray,"Children",t)},expression:"checkArray.Children"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Comedy",color:"teal"},model:{value:e.checkArray.Comedy,callback:function(t){e.$set(e.checkArray,"Comedy",t)},expression:"checkArray.Comedy"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Crime",color:"orange"},model:{value:e.checkArray.Crime,callback:function(t){e.$set(e.checkArray,"Crime",t)},expression:"checkArray.Crime"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Documentary",color:"red"},model:{value:e.checkArray.Documentary,callback:function(t){e.$set(e.checkArray,"Documentary",t)},expression:"checkArray.Documentary"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Drama",color:"cyan"},model:{value:e.checkArray.Drama,callback:function(t){e.$set(e.checkArray,"Drama",t)},expression:"checkArray.Drama"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Fantasy",color:"teal"},model:{value:e.checkArray.Fantasy,callback:function(t){e.$set(e.checkArray,"Fantasy",t)},expression:"checkArray.Fantasy"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Film-Noir",color:"orange"},model:{value:e.checkArray.Film_Noir,callback:function(t){e.$set(e.checkArray,"Film_Noir",t)},expression:"checkArray.Film_Noir"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Horror",color:"red"},model:{value:e.checkArray.Horror,callback:function(t){e.$set(e.checkArray,"Horror",t)},expression:"checkArray.Horror"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Musical's",color:"cyan"},model:{value:e.checkArray.Musical,callback:function(t){e.$set(e.checkArray,"Musical",t)},expression:"checkArray.Musical"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Mystery",color:"red"},model:{value:e.checkArray.Mystery,callback:function(t){e.$set(e.checkArray,"Mystery",t)},expression:"checkArray.Mystery"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Romance",color:"cyan"},model:{value:e.checkArray.Romance,callback:function(t){e.$set(e.checkArray,"Romance",t)},expression:"checkArray.Romance"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Sci-Fi",color:"teal"},model:{value:e.checkArray.Sci_Fi,callback:function(t){e.$set(e.checkArray,"Sci_Fi",t)},expression:"checkArray.Sci_Fi"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Thriller",color:"orange"},model:{value:e.checkArray.Thriller,callback:function(t){e.$set(e.checkArray,"Thriller",t)},expression:"checkArray.Thriller"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"War",color:"red"},model:{value:e.checkArray.War,callback:function(t){e.$set(e.checkArray,"War",t)},expression:"checkArray.War"}}),r("q-checkbox",{attrs:{"keep-color":"",label:"Western",color:"cyan"},model:{value:e.checkArray.Western,callback:function(t){e.$set(e.checkArray,"Western",t)},expression:"checkArray.Western"}})],1)]),r("q-step",{staticStyle:{height:"500px"},attrs:{name:2,title:"选择你喜欢的电影",icon:"create_new_folder",done:e.step>2,"header-nav":e.step>2}},[r("q-infinite-scroll",{staticStyle:{height:"500px","max-width":"100%","margin-left":"10%"}},[e.movie?e._l(parseInt(e.movie.length/3),(function(t){return r("div",{key:t,staticClass:"row"},e._l(3,(function(c){return r("div",{key:c,staticClass:"col-3 q-ma-lg"},[r("q-card",{staticClass:"my-card"},[3*(t-1)+c<e.movie.length?[r("q-card-section",[r("a",{attrs:{href:e.movie[3*(t-1)+c]["movie_url"],target:"_blank"}},[e._v(e._s(e.movie[3*(t-1)+c]["name"]))]),r("br"),r("span",{staticStyle:{color:"grey"}},[e._v("\n                      "+e._s(e.movie[3*(t-1)+c]["types"])+"\n                        ")])])]:e._e(),3*(t-1)+c<e.movie.length?[r("q-card-section",{staticStyle:{height:"75%"}},[r("q-img",{attrs:{height:"95%",contain:"",src:e.movie[3*(t-1)+c]["url"]}}),r("q-checkbox",{model:{value:e.options[3*(t-1)+c].value,callback:function(r){e.$set(e.options[3*(t-1)+c],"value",r)},expression:"options[3*(index-1)+j].value"}})],1)]:e._e()],2)],1)})),0)})):e._e()],2)],1),r("q-step",{staticStyle:{height:"500px"},attrs:{name:3,title:"获得推荐电影信息",icon:"add_comment","header-nav":e.step>3}},[r("q-infinite-scroll",{staticStyle:{height:"500px","max-width":"100%","margin-left":"10%"}},[e.recommend?e._l(parseInt(e.recommend.length/3),(function(t){return r("div",{key:t,staticClass:"row"},e._l(3,(function(c){return r("div",{key:c,staticClass:"col-3 q-ma-lg"},[r("q-card",{staticClass:"my-card"},[3*(t-1)+c<e.recommend.length?[r("q-card-section",[r("a",{attrs:{href:e.recommend[3*(t-1)+c]["movie_url"],target:"_blank"}},[e._v("\n                            "+e._s(e.recommend[3*(t-1)+c]["name"])+"\n                          ")]),r("br"),r("span",{staticStyle:{color:"grey"}},[e._v("\n                      "+e._s(e.recommend[3*(t-1)+c]["types"])+"\n                        ")])])]:e._e(),3*(t-1)+c<e.recommend.length?[r("q-card-section",{staticStyle:{height:"75%"}},[r("q-img",{attrs:{height:"95%",contain:"",src:e.recommend[3*(t-1)+c]["url"]}})],1)]:e._e()],2)],1)})),0)})):e._e()],2)],1)],1)],1)]),r("q-footer",{staticStyle:{"background-color":"#1f2329","text-align":"center"}},[r("div",{staticStyle:{color:"#7b7e81"}},[e._v("与我联系 xwyzsn@gmail.com")]),r("div",{staticStyle:{color:"#7b7e81"}},[e._v("Copyright © 2021 xwyzsn  | All rights reserved")])])],1)],1)},a=[],o=(r("e6cf"),r("bc3a")),n=r.n(o),l={data(){return{step:1,movie:[],group:[],options:[],checkArray:{Action:!1,Adventure:!1,Animation:!1,Children:!1,Comedy:!1,Crime:!1,Documentary:!1,Drama:!1,Fantasy:!1,Film_Noir:!1,Horror:!1,Musical:!1,Mystery:!1,Romance:!1,Sci_Fi:!1,Thriller:!1,War:!1,Western:!1},movie_length:0,show:!1,recommend:[]}},methods:{getMoviePhoto(){if(1===this.step){var e="";for(var t in this.checkArray)!0===this.checkArray[t]&&("Children"===t?t="Children's":"Sci_Fi"===t?t="Sci-Fi":"Film_Noir"===t&&(t="Film-Noir"),e+=t+"&");e=e.substr(0,e.length-1);const r=async()=>{await n.a.get("https://api.xwyzsn.site/api/v1/recommend/movie/"+e).then((e=>this.movie=JSON.parse(e.data))),this.movie.unshift({id:0,url:"-1"});for(var t=0;t<this.movie.length;t++)this.options.push({label:this.movie[t]["id"],value:!1});this.$refs.stepper.next()};r()}},getRecommend(){var e="";if(this.options.length>0)for(var t=0;t<this.options.length;t++)void 0!==this.options[t]["value"]&&null!=this.options[t]["value"]&&!1!==this.options[t]["value"]&&(e+=this.options[t]["label"]+"&");e=e.substr(0,e.length-1);const r=async()=>{await n.a.get("https://api.xwyzsn.site/api/v1/recommend/recommend/"+e).then((e=>{this.recommend=JSON.parse(e.data),console.log(this.recommend),this.$refs.stepper.next(),this.$q.loading.hide()}))};this.$q.loading.show({message:"正在获取计算推荐信息,请稍等"}),r()},scrollDown(){document.getElementById("section2").scrollIntoView()}},mounted(){this.$nextTick((()=>{this.$refs.myvideo.volume=.1}))}},i=l,s=(r("2da0"),r("2877")),h=r("4d5a"),m=r("e359"),y=r("65c6"),k=r("f531"),p=r("87fe"),d=r("8f8e"),u=r("ef35"),v=r("f09f"),b=r("a370"),f=r("068f"),A=r("b19c"),x=r("9c40"),g=r("7ff0"),_=r("eebe"),q=r.n(_),C=Object(s["a"])(i,c,a,!1,null,null,null);t["default"]=C.exports;q()(C,"components",{QLayout:h["a"],QHeader:m["a"],QToolbar:y["a"],QStepper:k["a"],QStep:p["a"],QCheckbox:d["a"],QInfiniteScroll:u["a"],QCard:v["a"],QCardSection:b["a"],QImg:f["a"],QStepperNavigation:A["a"],QBtn:x["a"],QFooter:g["a"]})}}]);