<template>
  <v-container >
    <v-row justify="center" >
      <v-col cols="10" sm="8" md="6" lg="4" >
        <h2 class="my-5" >가입 정보 입력</h2>
        <v-form class="form" ref="form" v-model="valid" lazy-validation>
          <v-text-field v-model="name" :rules="nameRule" label="이름" outlined dense required></v-text-field>
          <v-row style="width: 100%; margin-left: 1px">
            <v-text-field v-model="email" :rules="emailRules" label="이메일" outlined dense required style="width: 70%"></v-text-field>
            <v-spacer></v-spacer>
            <v-btn style="width: 20%" required @click="emailValidation()">이메일인증</v-btn>
          </v-row>
          <v-text-field v-if="emailClick == true"  v-model="emailchk" :rules="[emailchkRules,emailValidationRules]"  label="이메일 인증번호" outlined dense required  ></v-text-field>
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
            <v-radio-group v-model="gender" row label="성별" style="margin-top: 0px;" >
                <v-radio label="남자" value="man" color="#C2DEA0"></v-radio>
                <v-radio label="여자" value="woman" color="#C2DEA0"></v-radio>
            </v-radio-group>
          <v-btn large class="button" :disabled="!valid" color="#C2DEA0" @click="signup" style="color: #000000">회원가입</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UserApi from '../../api/UserApi.js'
import axios from "axios";

export default {
  name: "SignUp",
  components: {},
  created(){
      this.emailClick = false
  },
  data(){
    return{
      emailCheck : "",
      emailClick : false, 
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
    emailchk: "",
    emailchkRules:  [(v) => !!v || "인증번호 확인은 필수 입력항목입니다."],
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
    emailValidationRules(){
      return () => this.emailCheck == this.emailchk || "인증번호와 다릅니다";
    }
  },
  watch:{
    emailchk(){
      // console.log(this.emailchk)
    }
  },



  methods: {
    emailValidation(){
      this.emailClick = true;
      console.log(this.email)
      axios.post(process.env.VUE_APP_API_URL+"validation/emailvalidation",{
          "request_email" : this.email
       }).then((data) => {
         console.log(data.data.random_number);
         this.emailCheck = data.data.random_number;
      }).catch((er)=>{
        console.log(er)
      });


    },
    signup(){
      
      if (this.$refs.form.validate()) {
        let user_email = this.email;
        let user_password = this.password;
        let user_name = this.name;
        let user_gender = this.gender;
        let user_age = this.age;
        let isuser = 0;
        let data = {
          user_email,
          user_password,
          user_name,
          user_gender,
          user_age,
          isuser
        }
        
        console.log(data)
        UserApi.SignUp(
                data,
                  (res) => { // eslint-disable-line no-unused-vars
                    alert("회원가입 되었습니다.")
                    this.$router.push("/")
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    alert("실패!")
                  } 
                )
      }    
    },
    reset() {
      this.$refs.form.reset();
    },
  },
};
</script>

<style scoped>
.form .button {
  cursor: pointer;
  color: #fff;
  display: block;
  font-size: 16px;
  width: 100%;
  padding: px;
}
</style>
