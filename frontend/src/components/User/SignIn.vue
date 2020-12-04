<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="10" sm="8" md="6" lg="4" style="max-height:800px; ">
        <div class="logo-container">
            <router-link to="/"><img src="assets/img/115.jpg" alt="" style="height:5vw"></router-link>
            <br><br>

        </div>
        <v-form class="form" ref="form" v-model="valid" lazy-validation>
          <input
            type="hidden"
            th:name="${_csrf.parameterName}"
            th:value="${_csrf.token}"
          />
          <v-text-field
            v-model="email"
            label="이메일"
            required
            outlined
            dense
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="비밀번호"
            @click:append="show = !show"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show ? 'text' : 'password'"
            outlined
            dense
          ></v-text-field>
          <v-btn
            large
            class="button"
            :disabled="!valid"
            color="#C2DEA0"          
            @click="login"
            style="color: #000000;"
            >로그인</v-btn
          >
  
        </v-form>
        <div class="login-body text-center">
          <div class="sns-login">

            <button v-on:click="kakao">
                <img src="../../assets/kakao_login.png" alt />
            </button>
          </div>

        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
// import axios from "axios";
import UserApi from '../../api/UserApi.js';
import axios from 'axios';

export default {
  name: "Login",
  components: {},
  data: () => ({
    id: 0,
    token: "",
    valid: true,
    email: "",
    emailRules: [
      (v) => !!v || "이메일을 입력해주세요",
      (v) => /.+@.+\..+/.test(v) || "올바른 양식의 이메일을 입력해주세요",
    ],
    password: "",
    rules: {
      required: (value) => !!value || "비밀번호를 입력해주세요.",
      min: (v) => (v && v.length >= 8) || "비밀번호는 8글자 이상 입력해주세요",
    },
    checkbox: false,
    show: false,
  }),
  created() {

  },
  methods: {

    login(){
      
      if (this.$refs.form.validate()) {
        let user_email = this.email;
        let user_password = this.password;
        let data = {
          user_email,
          user_password,
        }
        
        console.log(data)

        UserApi.SignIn(
                data,
                  (res) => { // eslint-disable-line no-unused-vars
                    console.log(res)
                    if(res.result == "fail"){
                      alert("로그인 실패!");
                      return;
                    }                   
                    window.$cookies.set("user", res, "1d");                   
                     this.$router.push("/")
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    console.log(error)
                  } 
                )
      }    
    },
    kakao(){
       axios.get(process.env.VUE_APP_API_URL+"account/login/kakao/",{
         
       }).then((data) => {
         location.href=data.data.url
      }).catch((er)=>{
        console.log(er)
      });

    }
  },
};
</script>
<style scoped>
.logo-container {
  text-align: center;
}

.login-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* min-height: 100vh; */
}

h2 {
  text-align: center;
  margin: 0 0 20px;
}

.form .button {
  cursor: pointer;
  color: #fff;
  display: block;
  font-size: 16px;
  width: 100%;
  padding: px;
}

.sns-login {
  margin: 20px 0;
}

.sns-login .sns-btn {
  margin: 0 4px;
  padding: 5px 15px;
}

.add-option .routers {
  margin: 0 5px;
  text-decoration: none;
  color: #222;
}
</style>
