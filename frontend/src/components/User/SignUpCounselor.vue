<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="10" sm="8" md="6" lg="4">
        <h2 class="my-5">가입 정보 입력</h2>
        <v-form class="form" ref="form" v-model="valid" lazy-validation>
          <v-text-field v-model="name" :rules="nameRule" label="이름" outlined dense required></v-text-field>
          <v-row style="width: 100%; margin-left: 1px">
            <v-text-field v-model="email" :rules="emailRules" label="이메일" outlined dense required style="width: 70%"></v-text-field>
            <v-spacer></v-spacer>
            <v-btn style="width: 20%" @click="emailValidation()">이메일인증</v-btn>
          </v-row>
          <v-text-field v-if="this.emailClick == true"  v-model="emailchk" :rules="[emailchkRules,emailValidationRules]"  label="이메일 인증번호" outlined dense required  ></v-text-field>
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
              <v-combobox
                v-model="partSelect"
                :items="items"
                label="상담 분야 선택"
                item-text="kor"
                multiple
                chips
                filled
              ></v-combobox>
              
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
      this.emailClick= false
      console.log(this.items);
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
      address: "",
      
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

    //추가 사항
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
    // items:['청년','성인','갱년기 여성','마약','암','약물','계절'],
    youth: false,
    senior: false,
    pregnant: false,
    menopause: false,
    drug: false,
    cancer: false,
    thyroid: false,
    season: false,
    etc: "",
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
    },
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
  },



  methods: {
    emailValidation(){
      this.emailClick = true
      console.log(this.email)
      axios.post(process.env.VUE_APP_API_URL+"emailvalidation",{
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
        let counselor_email = this.email;
        // let counselor_password = this.password;
        let counselor_name = this.name;
        let counselor_gender = this.gender;
        let counselor_age = this.age;
        let counselor_pw = this.password;
        let counselor_introduce = "";
        let counselor_profile= "";
        let isuser =1;
        let data = {
          counselor_email,
          // counselor_password,
          counselor_name,
          counselor_gender,
          counselor_age,
          counselor_introduce,
          counselor_profile,
          counselor_pw,
          isuser,
        }
        
        console.log(data)

        UserApi.SignUpCounselor(
                data,
                  (res) => { // eslint-disable-line no-unused-vars
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    console.log(error)
                  } 
        )
      let youth = this.youth;
      let senior = this.senior;
      let pregnant = this.pregnant;
      let menopause = this.menopause;
      let drug = this.drug;
      let cancer = this.cancer;
      let thyroid = this.thyroid;
      let season = this.season;
      let data2 = {
            youth,
            senior,
            pregnant,
            menopause,
            drug,
            cancer,
            thyroid,
            season,
      }
      console.log(data2)
        UserApi.AddCounselPart(
                data2,
                  (res) => { // eslint-disable-line no-unused-vars
                    console.log(res)
                    alert("회원가입 되었습니다.")
                    this.$router.push("/")
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    alert("실패!")
                    console.log(error)
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
