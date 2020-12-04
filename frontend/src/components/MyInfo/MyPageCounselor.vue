<template>
  <v-row justify="center">
    <v-col cols="10" md="8" lg="6" >
      <div class="user-info" style="position:relative;">
        <v-avatar color="#eeeeee" size="90" class="mb-3">
          <i v-if="!profileURL" class="fas fa-user fa-lg"></i>
          <img v-else :src="profileURL" />
        </v-avatar>
        <h3>{{ user.data.counselor_name }}</h3>
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              x-small
              @click="$router.push('/counselorupdate')"
              style="position:absolute; bottom:5px;"
              color="grey"
              dark
            >
              <span>내정보 수정</span>
            </v-btn>
          </template>
          <span>전체 정보 수정이 가능합니다.</span>
        </v-tooltip>
      </div>
      <div class="target">
        <h3 class="mb-3">한줄 소개</h3>
        <v-row style="background-color: #fafafa; border-radius:10px;">
          <v-col class="px-4 py-4">
            <p>{{user.data.counselor_introduce}}</p>
          </v-col>
        </v-row>
      </div>

      <div id="my-info" class="target">
        <h3 class="mb-3">내정보</h3>
        <v-row style="background-color: #fafafa; border-radius:10px;">
          <v-col cols="4" md="2" class="px-4 py-4">
            <p>이메일</p>
            <p class="mb-0">나이</p>
          </v-col>
          <v-col cols="8" md="10" class="px-4 py-4">
            <p>{{user.data.counselor_email}}</p>
            <p class="mb-0">{{user.data.counselor_age}}</p>
          </v-col>
        </v-row>
      </div>

      <div id="certificate" class="target">
        <h3 class="mb-3">나의 상담 분야</h3>
        <v-row style="background-color: #fafafa; border-radius:10px;">
          <v-col cols="12" sm="12" class="px-4 py-4">
            <v-chip-group column>
              <v-chip v-for="tag in part" :key="tag" color="#C2B6DE">
                {{
                tag
                }}
              </v-chip>
            </v-chip-group>
          </v-col>
        </v-row>
      </div>

      <div id="schedule" class="target">
        <h3 class="mb-3">내 상담 현황</h3>
        <v-tabs v-model="tab" color="#C2DEA0" class="tabs">
          <v-tab
            v-for="item in items"
            :key="item"
          >
          {{ item }}
          </v-tab>
        </v-tabs>      
          <v-tabs-items v-model="tab">
            <Before :cid="counselor_id" :lists="list" :userlists="userlist"></Before>
            <Ing :cid="counselor_id"  :lists="inglist" :userlists="inguserlist"></Ing>
            <After :cid="counselor_id"  :lists="edlist" :userlists="eduserlist"></After>
          </v-tabs-items> 
      </div>
    </v-col>
  </v-row>
</template>

<script>
import * as easings from "vuetify/es5/services/goto/easing-patterns";
import Before from "./CounselorMeetCheck/Before.vue";
import Ing from "./CounselorMeetCheck/Ing.vue";
import After from "./CounselorMeetCheck/After.vue";
import axios from 'axios';

// axios.defaults.timeout = 1000;

export default {
  components: {
    Before,
    Ing,
    After,
  },
  data() {
    return {
      duration: 500,
      offset: 0,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      user: [],
      profileURL: "",
      part: [],
      tab: null,
      counselor_id: "",  //상담자 pk
      list: [],
      userlist: [],
      inglist: [],
      inguserlist: [],
      edlist: [],
      eduserlist: [],
      all: [],
      items: [
          '새로운 상담 리스트', '진행 예정인 상담 리스트', '종료된 상담 리스트',
        ],   
      cnt: 0,
    };
  },
  created(){
    let cookies = window.$cookies.get("user");
    this.user = cookies;
    this.profileURL = this.user.data.counselor_profile
    // this.counselor_id = this.user.data.counselor_pk

    this.cnt = 0;
        // this.list = [],       //신청 온 상담 리스트
        // this.userlist = [],   //신청 온 상담 리스트의 유저 pk
        
        // 1. 상담 분야 리스트
        axios
        .get(process.env.VUE_APP_API_URL+"counselor/counselormajor/" + cookies.data.counselor_pk)
        .then((data) => {
          // console.log(data.data.data[0])
          this.partSelect(data.data.data[0])
        }).catch((er)=>{
            console.log(er)
        });        


        //listone, listtwo, listthree
        
        // 2. 상담 리스트 불러오기
        axios
        .get(process.env.VUE_APP_API_URL+"counsel/getmycounsel/" + cookies.data.counselor_pk)
        .then((data) => {
          this.all = data.data.data
          
          // 3. 상담 신청 받은 리스트
          for(var i=0 ; i<this.all.listone.length; i++){
            this.list.push(this.all.listone[i][0]);
          }          
          for(i=0 ; i<this.all.listone.length; i++){
            this.userlist.push(this.all.listone[i][1].name);
          }

          // 4. 상담 수락한 리스트
          for(i=0 ; i< this.all.listtwo.length; i++){
              this.inglist.push(this.all.listtwo[i][0]);
          }  
          for(i=0 ; i< this.all.listtwo.length; i++){
              this.inguserlist.push(this.all.listtwo[i][1].name); 
          }

          //5. 상담 완료된 리스트
          for(i=0 ; i< this.all.listthree.length; i++){
              this.edlist.push(this.all.listthree[i][0]);
          }  
          for(i=0 ; i< this.all.listthree.length; i++){
                this.eduserlist.push(this.all.listthree[i][1].name); 
          }
        }).catch((er)=>{
            console.log(er)
        });
        
  },
  watch:{
    cnt(){
    }
  },
  computed: {
    target() {
      const value = this[this.type];
      if (!isNaN(value)) return Number(value);
      else return value;
    },
    options() {
      return {
        duration: this.duration,
        offset: this.offset,
        easing: this.easing,
      };
    },
  },
  methods:{
    partSelect(list){
      if(list.youth == true){
        this.part.push("청소년 우울증")
      }
      if(list.senior == true){
        this.part.push("노인 우울증")
      }
      if(list.pregnant == true){
        this.part.push("산후 우울증")
      }
      if(list.menopause == true){
        this.part.push("폐경기")
      }
      if(list.drug == true){
        this.part.push("약물오남용")
      }
      if(list.cancer == true){
        this.part.push("암환자")
      }
      if(list.thyroid == true){
        this.part.push("갑상선 우울증")
      }
      if(list.season == true){
        this.part.push("계절성 우울증")
      }
    },
  }

};
</script>

<style scoped>
.user-info {
  margin: 0px 0;
  padding: 30px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.tabs {
  margin-bottom: 30px;
}

.target {
  margin: 30px 0;
}

#my-info p {
  margin-bottom: 5px;
}

.skill {
  margin: 0 3px;
}

hr {
  margin: 30px 0;
}
</style>

