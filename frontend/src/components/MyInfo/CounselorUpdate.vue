<template>
<div>
<TopHeader></TopHeader>
<Header></Header>
<v-app>
  <v-row justify="center">
    <v-col cols="10" md="8" lg="6">
      <div class="user-info" style="position:relative;">
        <v-avatar color="grey" size="90" class="mb-3">
          <span v-if="!profileURL" class="white--text headline"></span>
          <img v-else :src="profileURL" />
        </v-avatar>
        <h3>{{user_name}}</h3>
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              x-small
              @click="modify"
              style="position:absolute; bottom:5px;"
              color="grey"
              dark
            >
              <span>저장</span>
            </v-btn>
          </template>
          <span>변경된 정보를 저장 합니다.</span>
        </v-tooltip>
      </div>
      <div class="target">
        <h3 class="mb-3">한줄 소개</h3>
        <v-row style="background-color: #eeeeee; border-radius:10px;">
            <v-textarea v-model="user_introduce"></v-textarea>  
        </v-row>
      </div>
      <div id="my-info" class="target">
        <h3 class="mb-3">내정보 </h3>
        <v-row style="background-color: #eeeeee; border-radius:10px;">
          <v-card-text>
            <v-text-field
              dense
              v-model="profileURL"
              label="프로필사진 링크"
              filled
            ></v-text-field>
            <v-text-field
              filled
              dense
              disabled
              :value="user_email"
              label="이메일"
              color="white"
            ></v-text-field>
            <v-text-field
              filled
              dense
              v-model="user_name"
              label="이름"
            ></v-text-field>
            <v-text-field
              filled
              dense
              v-model="user_password"
              label="비밀번호"
            ></v-text-field>
             <v-text-field
              filled
              dense
              v-model="user_age"
              label="나이"
            ></v-text-field>  
             <v-text-field
              filled
              dense
              disabled
              v-model="user_gender"
              label="성별"
            ></v-text-field>  
              <!-- <v-combobox
                v-model="partSelect"
                :items="items"
                label="상담 분야 선택"
                item-text="kor"
                multiple
                chips
                filled
              ></v-combobox>       -->

          </v-card-text>
        </v-row>
      </div>
    </v-col>
  </v-row>
  </v-app>
  </div>

</template>

<script>
import * as easings from "vuetify/es5/services/goto/easing-patterns";
import TopHeader from '../Home/TopHeader.vue'
import Header from '../Home/Header.vue'
import axios from "axios"

export default {
  components: {
    TopHeader,
    Header,
  },
  data() {
    return {
      duration: 500,
      offset: 0,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      hasSaved: false,
      isEditing: null,
      model: null,

      // 상담사 정보
      user: [],
      profileURL: "",
      user_name: "",
      user_email: "",
      user_age: "",
      user_password: "",
      user_gender: "",
      user_introduce: "",

      //상담 종목
      partSelect: [],
      items:[
        {
          eng : 'youth',
          kor : '청소년 우울증' 
        },
        {
          eng : 'senior',
          kor : '노인 우울증'
        },
        {
          eng : 'pregnant',
          kor : '산후 우울증'
        },
        {
          eng : 'drug',
          kor : '약물오남용'
        },
        {
          eng : 'cancer',
          kor : '암환자'
        },
        {
          eng : 'thyroid',
          kor : '갑상선 우울증'
        },
        {
          eng : 'season',
          kor : '계절성 우울증'
        },
      ],
      youth: false,
      senior: false,
      pregnant: false,
      menopause: false,
      drug: false,
      cancer: false,
      thyroid: false,
      season: false,
      etc: "",
    };
  },
  created() {
    this.user = window.$cookies.get("user").data;
    this.user_name = this.user.counselor_name;
    this.user_email = this.user.counselor_email;
    this.user_age = this.user.counselor_age;
    this.user_password = this.user.counselor_pw;
    this.user_gender = this.user.counselor_gender;
    this.profileURL = this.user.counselor_profile;
    this.user_introduce = this.user.counselor_introduce;
    // axios
    //     .get(process.env.VUE_APP_API_URL+"counselor/counselormajor/" + this.user.counselor_pk)
    //     .then((data) => {
    //       console.log(data.data.data[0])
    //     }).catch((er)=>{
    //         console.log(er)
    //     });   
  },
  methods: {
    modify(){
      axios.put(process.env.VUE_APP_API_URL+"counselor/counselor/"+this.user.counselor_pk,
        {
          counselor_name: this.user_name,
          counselor_email: this.user_email,
          counselor_age: this.user_age,
          counselor_pw: this.user_password,
          counselor_gender: this.user_gender,
          counselor_profile: this.profileURL,
          counselor_introduce: this.user_introduce,
        }
      ).then((data)=>{
        window.$cookies.remove("user");
        window.$cookies.set("user", data.data, "1d");
        this.$router.push("/mypage"); 

      })
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
        offset: this.offset + 200,
        easing: this.easing,
      };
    },
  },
  watch:{
    partSelect(list){
      let partname = this.partSelect[list.length-1].eng;
      if(partname == "youth"){
        this.youth = true;
      }else if(partname == "senior"){
        this.senior = true;
      }else if(partname == "pregnant"){
        this.pregnant = true;
      }else if(partname == "menopause"){
        this.menopause = true;
      }else if(partname == "drug"){
        this.drug = true;
      }else if(partname == "cancer"){
        this.cancer = true;
      }else if(partname == "thyroid"){
        this.thyroid = true;
      }else if(partname == "season"){
        this.season = true;
      }else{
        this.etc = partname;
      }   
    },
  }
};
</script>

<style scoped>
.user-info {
  margin: 5px 0;
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

.skills {
  margin: 5px 0;
}

.skill {
  margin: 0 3px;
}
</style>
