<template>
<div>
  <v-app >
  <Animation ></Animation>
      <v-progress-linear
        class="pl"
        height="20"
        :value="count"
        striped
        color="#EBE59D"
        
    >{{count}}%</v-progress-linear>
    <!-- <v-progress-linear class="pl" v-model="count" height="20" color="#666666">{{count}}%</v-progress-linear> -->
    <v-carousel v-model="model" class="pll" hide-delimiters next-icon prev-icon >
      <v-carousel-item
        v-for=" item in items"
        :key="item.question"
      >
        <v-sheet 
          color="#ffffff"
          height="100%"
          tile
          fluid
        >
          <h5 style="color: black; text-align: center;"><span style="color: red; font-size: 30px">Q. </span>{{item.question}}</h5>
          <v-row align="center">
            <v-col
                class="fill-height"
                  align="center"
                  justify="center"
            >
              <div class="text-center">
                <div class="my-2">
                  <v-btn
                    rounded
                    color="#EBA291"
                    dark
                    width="320px"
                    height="70px"
                    @click="total=total+1"                                       
                  >
                    거의 드물게 그랬다
                  </v-btn>
                  <v-btn
                    rounded
                    color="#EBA291"
                    dark
                    width="320px"
                    height="70px"
                    @click="total=total+2"  
                  >
                    때때로 그랬다
                  </v-btn>
                </div>
                <div class="my-2">
                  <v-btn
                    rounded
                    color="#EBA291"
                    dark
                    width="320px"
                    height="70px"
                    @click="total=total+3"  
                  >
                    꽤 자주 그랬다
                  </v-btn>
                  <v-btn
                    rounded
                    color="#EBA291"
                    dark
                    width="320px"
                    height="70px"
                    @click="total=total+4"  
                  >
                    상당히 자주 그랬다
                  </v-btn>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </v-app>
</div>
</template>

<script>
import Animation from "./Animation.vue"
export default {
  components:{
    Animation
  },
  data(){
    return{
      end: false,
      count: 0,
      total: 0,
            items:[
                {question: "평소에는 성가시지 않았던 일이 성가시게 느껴졌다."},
                {question: "입맛이 없었다."},
                {question: "가족이나 친구들을 만나보고 얘기도 했지만 계속 기분이 좋지 않았다"},
                {question: "나는 남들만큼 괜찮은 사람이라고 생각했다."},
                {question: "내가 하는 일에 마음을 집중하기가 어려웠다."},
                {question: "기분이 우울했다."},			
                {question: "내가 하고자 하는 일 모두가 어렵게 느껴졌다."},			
                {question: "미래에 대하여 희망적으로 느꼈다."},				
                {question: "내 인생은 실패작이라고 생각했다."},				
                {question: "두려움을 느꼈다."},				
                {question: "잠을 시원하게 못잤다."},				
                {question: "행복한 편이였다."},				
                {question: "평상시보다 대화를 적게 하였다."},				
                {question: "외로움을 느꼈다."},				
                {question: "다른 사람들이 다정하지 못하다고 느꼈다."},				
                {question: "생활이 즐겁다고 느꼈다."},			
                {question: "울었던 적이 있다."},				
                {question: "슬픔을 느꼈다."},				
                {question: "주위 사람들이 나를 싫어한다는 생각이 들었다."},				
                {question: "무슨 일이든 제대로 할 수가 없었다."},	
            ],
            model: 0,
        }
    },
    methods:{

    },
    watch:{
      total(){
        this.model++;
        this.count = this.count + 5
        if(this.model == 20){
          this.end = true
          
          this.$router.push({name: 'SelfDiagResult', params: {result: this.total - 20}})
          // this.$router.push("/selfDiagResult")
        }
      }
    }
}
</script>

<style scoped>
.pl{
    left: 25.5%;
    width: 50%;
    position: absolute;
    top: 35%
 
}
.pll{
    left: 25.5%;
    width: 50%;
    position: absolute;
    top: 40%
}
.v-btn{
  margin: 10px;
  outline: none;
}
</style>
