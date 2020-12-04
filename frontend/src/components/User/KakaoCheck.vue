<template>
  <v-container v-if="idCheck==false">
    <v-row  justify="center">
      <v-col cols="10" sm="8" md="6" lg="4">
        <h2 class="my-5">추가 정보 입력</h2>
        <v-form class="form" ref="form" v-model="valid" lazy-validation>
          <v-text-field :value="this.userinfo.name" outlined dense readonly></v-text-field>
          <v-text-field v-model="email" :rules="emailRules" label="이메일" outlined dense required></v-text-field>
          <v-text-field
            v-model="password"
            :rules="passwordRules"
            @click:append="show1 = !show1"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            label="비밀번호"
            required
            outlined
            dense
          ></v-text-field>
          <v-text-field
            v-model="passwordchk"
            :rules="[passwordchkRules, passwordconfirmRules]"
            @click:append="show2 = !show2"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show2 ? 'text' : 'password'"
            label="비밀번호 확인"
            required
            outlined
            dense
          ></v-text-field>
          <v-text-field v-model="age"  label="나이" outlined dense required ></v-text-field>
            <v-radio-group v-model="gender" row label="성별" style="margin-top: 0px;">
                <v-radio label="남자" value="man" color="#C2DEA0"></v-radio>
                <v-radio label="여자" value="woman" color="#C2DEA0"></v-radio>
            </v-radio-group>
          <v-btn large class="button" :disabled="!valid" color="#c2dea0" @click="signup">회원가입</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import UserApi from '../../api/UserApi.js'

export default {
     data(){
       return{
        idCheck: false,
        userinfo : {},
        sID : "",
        age : "",
        gender : "",

        signupData: {
          name: null,
          email: null,
          password: null,
          radioGroup: 1,
        },

        valid: true,
        name: "",
        nameRule: [(v) => !!v || "이름은 필수 입력항목입니다."],
        email: "",
        emailRules: [
          (v) => !!v || "E-Mail은 필수 입력항목입니다",
          (v) => /.+@.+\..+/.test(v) || "E-mail 양식이 올바르지 않습니다.",
        ],
        password: "",
        passwordRules: [
          (v) => !!v || "비밀번호는 필수 입력항목입니다",
          (v) => (v && v.length >= 8) || "8글자 이상 입력해야 합니다.",
        ],
        passwordchk: "",
        passwordchkRules: [(v) => !!v || "비밀번호 확인은 필수 입력항목입니다."],
        checkbox: false,
        show1: false,
        show2: false,
      }
     },
       computed: {
    passwordconfirmRules() {
      return () => this.password === this.passwordchk || "비밀번호가 다릅니다";
    },
  },
    created(){
      var access_token = location.search.split('=')[1]
      console.log(location.search.split('=')[1])
      axios.post(process.env.VUE_APP_API_URL+"account/login/kakao/callback/check/",{
          "access_token" : access_token
       }).then((data) => {
         console.log(data.data);
         if(data.data.link == false){
           console.log("없는 아이디")
           this.idCheck = false;
          //  this.$router.push('/logincheck');
           this.sID = data.data.id;
           this.userinfo = data.data;
          //  console.log(data.data.id)
          this.$router.push("/kakaocheck")
         }else{
           console.log("있는 아이디") 
            this.idCheck = true;
            window.$cookies.set("user", data.data, "1d");
            this.$router.push("/")
         }
      }).catch((er)=>{
        console.log(er)
      });
    },
     methods: {
    signup(){
      if (this.$refs.form.validate()) {
        let user_email = this.email;
        let user_password = this.password;
        let user_name = this.userinfo.name;
        let user_gender = this.gender;
        let user_age = this.age;
        let issocial = this.sID;
        let data = {
          user_email,
          user_password,
          user_name,
          user_gender,
          user_age,
          issocial
        }
        
        console.log(data)

        UserApi.SignUp(
                data,
                  (res) => { // eslint-disable-line no-unused-vars
                    console.log(res)
                    this.$router.push("/")

                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    console.log(error)
                  } 
                )
      }    
    },
    reset() {
      this.$refs.form.reset();
    },
  },
}
</script>

<style scoped>
.form .button {
  cursor: pointer;
  color: #fff;
  display: block;
  font-size: 16px;
  width: 100%;
}
</style>