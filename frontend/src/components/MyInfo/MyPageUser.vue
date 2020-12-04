<template>
  <v-row justify="center">
    <v-col cols="10" md="8" lg="6" >
      <div class="user-info" style="position:relative;">
        <v-avatar color="#eeeeee" size="90" class="mb-3">
          <v-icon size="60">mdi-account</v-icon>
        </v-avatar>
        <h3>{{ user.user_name }}</h3>
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              x-small
              @click="$router.push('/userupdate')"
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
      <div id="my-info" class="target">
        <h3 class="mb-3">내정보</h3>
        <v-row style="background-color: #fafafa; border-radius:10px;">
          <v-col cols="4" md="2" class="px-4 py-4">
            <p>이메일</p>
            <p class="mb-0">나이</p>
          </v-col>
          <v-col cols="8" md="10" class="px-4 py-4">
            <p>{{user.user_email}}</p>
            <p class="mb-0">{{user.user_age}}</p>
          </v-col>
        </v-row>
      </div>

      <div id="schedule" class="target">
        <h3 class="mb-3">내 상담 리스트</h3>
          <Before :uid="user_id" :lists="list" :userlists="counselorlist"></Before>
      </div>
    </v-col>
  </v-row>
</template>

<script>
import * as easings from "vuetify/es5/services/goto/easing-patterns";
import Before from "./UserMeetCheck/Before.vue";
import axios from 'axios';

export default {
  components: {
    Before,
  },

  data() {
    return {
      duration: 500,
      offset: 0,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      user: [],
      tab: null,
      user_id: "",
      list: [],
      counselorlist: [],

    
    };
  },
  created(){
    let data = window.$cookies.get("user");
    this.user = data.data;
    this.user_id = this.user.user_pk
    // 1. 상담자의 신청 온 리스트 불러오기
      axios
        .get(process.env.VUE_APP_API_URL +"counsel/getcounsel/" + this.user_id)
        .then((data) => {
          this.list = data.data.data 
          //유저들 pk를 userlist에 넣기 
          // for(var i=0 ; i< this.list.length; i++){
          //       axios.get("http://127.0.0.1:8000/counselor/counselor/" + this.list[i].counselor_pk). then((data)=>{
          //         // this.counselorlist.push(data.data.data[0].counselor_name); 
          //         this.cnt++;
          //         console.log(data.data)
          //       })
          //   }
            for(var i=0 ; i< 1; i++){
                axios.get(process.env.VUE_APP_API_URL + "counselor/counselor/" + 2). then((data)=>{
                  this.counselorlist.push(data.data.data[0].counselor_name); 
                  this.cnt++;
                })
            }
        }).catch((er)=>{
            console.log(er)
        });
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

