<template>
<div>
<TopHeader></TopHeader>
<Header></Header>
<v-app>
  <v-row justify="center">
    <v-col cols="10" md="8" lg="6">
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
      <div id="my-info" class="target">
        <h3 class="mb-3">내정보 </h3>
        <v-row style="background-color: #eeeeee; border-radius:10px;">
          <v-card-text>
            <v-text-field
              filled
              dense
              disabled
              v-model="user_email"
              label="이메일"
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
      user: [],
      user_name: "",
      user_email: "",
      user_age: "",
      user_password: "",
      user_gender: "",

    };
  },
  created() {
    this.user = window.$cookies.get("user").data;
    this.user_name = this.user.user_name;
    this.user_email = this.user.user_email;
    this.user_age = this.user.user_age;
    this.user_password = this.user.user_password;
    this.user_gender = this.user.user_gender;

  },
  methods: {
    modify(){
      axios.put(process.env.VUE_APP_API_URL+"user/user/"+this.user.user_pk,
        {
          user_name: this.user_name,
          user_email: this.user_email,
          user_age: this.user_age,
          user_password: this.user_password,
          user_gender: this.user_gender,
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
