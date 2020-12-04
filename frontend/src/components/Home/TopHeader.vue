<template>
    <!-- ======= Top Bar ======= -->
  <div id="topbar" class="d-none d-lg-flex align-items-center fixed-top">
    <div class="container d-flex align-items-center justify-content-between">
      <div class="d-flex align-items-center">
                <i class="icofont-clock-time"></i> 월 - 금, 9am to 6pm

        <!-- <i class="icofont-clock-time"></i> Monday - Saturday, 8AM to 10PM -->
      </div>
      <div class="d-flex align-items-center">
        <!-- <i class="icofont-phone"></i> Call us now +1 5589 55488 55 -->
        <div v-if="isCheck==false">
          <a href="/signin" style="color: white; margin-right: 12px">로그인</a>
          &nbsp;&nbsp;
          <a href="/selectuser" style="color: white">회원가입</a>
        </div>
        <div v-else>
          <a>{{this.myName}}님 안녕하세요</a> &nbsp;&nbsp;&nbsp;
          <a href="/" style="color: white" @click="logout">로그아웃</a>
        </div>

          <!-- <li ><a>{{this.myName}}</a></li>
          <li ><a href="/" @click="logout">로그아웃</a></li> -->
      </div>
      <!-- <div class="d-flex align-items-center">
        우울한 기분 그냥 지나치지 마세요
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
    data(){
     return{
      isCheck : false,
      myName : "",
     }
    },
    created(){
      let cookies = window.$cookies.get("user");
      this.isCheck = false
      console.log(cookies)
      if(cookies == null) {
        this.isCheck = false
      }else {
        if(cookies.data.isuser == 0){
          this.isCheck = true
          this.$store.state.myName = cookies.data.user_name
          this.myName = this.$store.state.myName
        }else{
          this.isCheck = true
          this.$store.state.myName = cookies.data.counselor_name
          this.myName = this.$store.state.myName
          
        }

    }

  },
  methods:{
    logout(){
      window.$cookies.remove("user");
      this.$store.state.myName = "";
    }
  },

}
</script>

<style>

</style>