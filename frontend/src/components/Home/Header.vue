<template>
    <!-- ======= Header ======= -->
  <header id="header" class="fixed-top">
    <div class="container d-flex align-items-center">

      <a href="/" class="logo mr-auto"><img src="assets/img/115.jpg" alt=""></a>
      <!-- Uncomment below if you prefer to use an image logo -->
      <!-- <h1 class="logo mr-auto"><a href="index.html">Medicio</a></h1> -->

      <nav class="nav-menu d-none d-lg-block">
        <ul>
          <!-- <li class="active" ><a href="/" >Home</a></li> -->
          <li v-if="isCheck==true"><router-link to="/mypage"
                    >마이페이지</router-link
                  ></li>
          <li><router-link to="/survey"
                    >우울증 자가 진단</router-link
                  ></li>
          <li><router-link to="/searchConsultant"
                    >상담사 찾기</router-link
                  ></li>
          
          <li><router-link to="/"
                    >상담 시설</router-link
                  ></li>
          <li>
            <v-app class="test">
               <div class="text-center">
                <v-menu offset-y v-model="menu">
                  <template v-slot:activator="{ on, attrs }">
                    <v-icon class="" v-bind="attrs"
                      v-on="on">
                            mdi-email-multiple-outline
                          </v-icon>
                  </template>
                  <v-card
    class="mx-auto"
    max-width="500"
  >

    <v-list subheader>
      <v-subheader>최근 메시지</v-subheader>
      <v-dialog
             v-model="mdialog"
             max-height="100%"
             scrollable
             width="30%"
            >
            <template v-slot:activator="{ on, attrs }">
      <v-list-item
        v-for="chat in lists"
        :key="chat.receiver"
        @click="openChat(chat)"
        v-bind="attrs"
          v-on="on"
      >
        <v-list-item-avatar v-if="1">
          <v-img
            :alt="`${chat.receiverImg} avatar`"
            :src="chat.receiverImg"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="chat.receiverName"></v-list-item-title>
        </v-list-item-content>

        
    
        <v-list-item-icon>
          <v-icon 
          :color="chat.active ? 'deep-purple accent-4' : 'grey'">
            mdi-message-outline
          </v-icon>
        </v-list-item-icon>
      </v-list-item>
      </template>
      <Chat style="overflow: hidden; overflow-y:hidden; padding:0px; margin:0px" :key="mdialog"  ></Chat>
  </v-dialog>
    </v-list>
  </v-card>
                </v-menu>
              </div>
              
            </v-app>
          </li>
          <!-- <li class="drop-down"><a href="">Drop Down</a>
          <ul>
            <li><a href="#">Drop Down 1</a></li>
            <li class="drop-down"><a href="#">Deep Drop Down</a>
              <ul>
                <li><a href="#">Deep Drop Down 1</a></li>
                <li><a href="#">Deep Drop Down 2</a></li>
                <li><a href="#">Deep Drop Down 3</a></li>
                <li><a href="#">Deep Drop Down 4</a></li>
                <li><a href="#">Deep Drop Down 5</a></li>
              </ul>
            </li>
            <li><a href="#">Drop Down 2</a></li>
            <li><a href="#">Drop Down 3</a></li>
            <li><a href="#">Drop Down 4</a></li>
          </ul>
        </li> -->

          
        </ul>
      </nav><!-- .nav-menu -->

      <!-- <a href="#appointment" class="appointment-btn scrollto"><span class="d-none d-md-inline">Make an</span> Appointment</a> -->

    </div>
  </header><!-- End Header -->

</template>

<script>
import firebase from 'firebase'
import Chat from '../SeacrhConsultant/Chat'
export default {
  components:{
    Chat
  },
  data(){
    return{
      menu : 0,
      isCheck : false,
      myName : "",
      
      lists: [
      ],
      mdialog:false,
    }
  },
  watch: {
    lists(){

    }
  },
  mounted(){
    let cookies = window.$cookies.get("user");
    this.isCheck = false
    console.log(cookies)
    if(cookies == null) {
      this.isCheck = false
    }else {
      this.isCheck = true
      this.$store.state.myName = cookies.data.user_name
      this.myName = this.$store.state.myName
    }
    if(window.$cookies.get("user").data.isuser == 0) //상담사가 아닌 일반 유저라면,
    {
        let self = this;
        let itemsRef = firebase.database().ref("users").child(window.$cookies.get("user").data.user_pk+"|user");
        itemsRef.on("value", snapshot => {
          let data = snapshot.val();
          let lists = [];
          let onoff = false;
          Object.keys(data).forEach(key => {
            if(data[key].alarm == "on")
              {
                onoff = true 
              }
            lists.push({
                active :onoff,
                receiver: data[key].receiver,
                receiverName: data[key].receiverName,
                receiverImg: data[key].receiverImg,
            });
          });
          self.lists = lists;
    });
    }
    else{
      let self = this;
        let itemsRef = firebase.database().ref("users").child(window.$cookies.get("user").data.counselor_pk+"|counselor");
        itemsRef.on("value", snapshot => {
          let data = snapshot.val();
          let lists = [];
          let onoff = false;
          Object.keys(data).forEach(key => {
            if(data[key].alarm == "on")
              {
                onoff = true 
              }
            lists.push({
                active : onoff,
                receiver: data[key].receiver,
                receiverName: data[key].receiverName,
                receiverImg: "https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff",
            });
          });
          self.lists = lists;
    });
    }
  },
  methods:{
    logout(){
      window.$cookies.remove("user");
    },
    openChat(chat){
            if(window.$cookies.get("user").data.isuser==0)
                {
                  this.$store.state.chatStore.room = window.$cookies.get("user").data.user_pk+"|"+chat.receiver;
                  this.$store.state.chatStore.sender = window.$cookies.get("user").data.user_pk;
                  this.$store.state.chatStore.receiver = chat.receiver;
                  this.$store.state.chatStore.receiverName = chat.receiverName
                  this.$store.state.chatStore.receiverImg = chat.receiverImg
                }
            else{
                this.$store.state.chatStore.room = chat.receiver+"|"+window.$cookies.get("user").data.counselor_pk;
                this.$store.state.chatStore.sender = window.$cookies.get("user").data.counselor_pk;
                this.$store.state.chatStore.receiver = chat.receiver;
                this.$store.state.chatStore.receiverName = chat.receiverName
                this.$store.state.chatStore.receiverImg = "https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff"
            }
            
            this.mdialog=true;
        }
  }
}
</script>

<style scoped>
.test{
  position: absolute;
  height: 0px;
  padding-top:0px;
  margin-top:0px;
  top:7.8px;
  left:19px;
  z-index: 1;
}

</style>