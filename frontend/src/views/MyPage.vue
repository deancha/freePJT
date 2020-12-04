<template>
<div>

    <TopHeader></TopHeader>
    <Header></Header>
  <v-app>
    <MyPageCounselor v-if="mystatus==1"></MyPageCounselor>
    <MyPageUser  v-if="mystatus==0"></MyPageUser>
  </v-app>
</div>
</template>

<script>
import MyPageUser from '../components/MyInfo/MyPageUser.vue'
import MyPageCounselor from '../components/MyInfo/MyPageCounselor.vue'
import TopHeader from '../components/Home/TopHeader.vue'
import Header from '../components/Home/Header.vue'

export default {
    components:{
        MyPageCounselor,
        MyPageUser,
        TopHeader,
        Header,
    },
    data(){
      return{
        mystatus: "",
      }
    },
    created(){
      let cookies = window.$cookies.get("user");
      this.mystatus = cookies.data.isuser;
    }
}
</script>

<style>

</style>