  <template>
    <!-- Login section -->
    <!-- Chat section -->
    <v-card >
    <div class="message-body">
      <div class="card">
        <body class="card-body" >
          <div
            class="border pl-2 pt-1 ml-2 message-text mb-2"
            v-for="(message,i) in messages"
            :key='i'
          >
            <span class="mg-text">{{ message.username }}</span>
            <p class="message pt-1">{{ message.text }}</p>
          </div>
        </body>
      </div>
      <div  style="max-width:90%; margin:auto">
      <v-text-field value="메시지 입력"
            v-model="showMessage" type="text" class="mt-3 pl-2 pr-2"  append-icon="mdi-send" style="max-width:100%;"
            v-on:keyup.enter="sendMessage"
            @click:append="sendMessage"
            >
      <!-- <button class="btn btn-primary" @click="sendMessage">Send</button> -->
      </v-text-field>
      </div>
    </div>
    </v-card>
</template>

<script>
import firebase from "firebase";
export default {
  name: "App",
  data() {
    return {
      name : "",
      showMessage: "",
      messages: [],
      // counselor: this.$store.state.counselorInfoStore.counselorInfo.counselor_pk
    };
  },
  created() {
  },
  watch: {
      
  },
  methods: {
    sendMessage() {
      // "https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff"
      let name = "";
      if(window.$cookies.get("user").data.isuser == 0)
        name = window.$cookies.get("user").data.user_name
      else
        name = window.$cookies.get("user").data.counselor_name
      const message = {
        text: this.showMessage,
        username: name,
      };
      firebase
        .database()
        .ref("messages")
        .child(this.$store.state.chatStore.room)
        .push(message);
      //유저만 고려하였을 때임.
    
    if(window.$cookies.get("user").data.isuser == 0)
    {
     let itemsRef = firebase.database().ref("users").child(this.$store.state.chatStore.sender+"|user");
     let dkey = ""

     itemsRef.once("value", snapshot => {
      let data = snapshot.val();
      let check = false;
      if(data!=null)
      {
        Object.keys(data).forEach(key => {
          if(data[key].receiver == this.$store.state.chatStore.receiver)
            {
              check=true;
              dkey = key;
            }
      });
      }
      if(!check){
      const receiver = {
        receiver: this.$store.state.chatStore.receiver,
        receiverName: this.$store.state.chatStore.receiverName,
        receiverImg:this.$store.state.chatStore.receiverImg,
        alarm:"off"
      };

      firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.sender+"|user")
        .push(receiver);
      }
      else{
        let ref = firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.sender+"|user/"+dkey)
        ref.update({
        alarm : "off"
        });
      }
    });
    
    itemsRef = firebase.database().ref("users").child(this.$store.state.chatStore.receiver+"|counselor");
     itemsRef.once("value", snapshot => {
      let data = snapshot.val();
      let check = false;
      if(data!=null)
      {
        Object.keys(data).forEach(key => {
          if(data[key].receiver == this.$store.state.chatStore.sender)
            {
              check=true;
              dkey = key;
            }
      });
      }
      if(!check){
      const receiver = {
        receiver: this.$store.state.chatStore.sender,
        receiverName: window.$cookies.get("user").data.user_name,
        receiverImg:"https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff",
        alarm : "on",
      };
      
      firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.receiver+"|counselor")
        .push(receiver);
      }
      else{
        

        let ref = firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.receiver+"|counselor/"+dkey)
        ref.update({
        alarm : "on"
        });
      }
    });
    }
    else{
    let itemsRef = firebase.database().ref("users").child(this.$store.state.chatStore.receiver+"|user");
    let dkey = "";
     itemsRef.once("value", snapshot => {
      let data = snapshot.val();
      if(data!=null)
      {
        Object.keys(data).forEach(key => {
          if(data[key].receiver == this.$store.state.chatStore.sender)
            {
              dkey = key;
            }
      });
      }
    let ref = firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.receiver+"|user/"+dkey)
        ref.update({
        alarm : "on"
        });
    });

    
    
    itemsRef = firebase.database().ref("users").child(this.$store.state.chatStore.sender+"|counselor");
     itemsRef.once("value", snapshot => {

      let data = snapshot.val();
      if(data!=null)
      {
        Object.keys(data).forEach(key => {
          if(data[key].receiver == this.$store.state.chatStore.receiver)
            {
              dkey = key;
            }
      });
      }

        let ref = firebase
        .database()
        .ref("users")
        .child(this.$store.state.chatStore.sender+"|counselor/"+dkey)
        ref.update({
        alarm : "off"
        });
    });
    }



    this.showMessage = "";
    }
  },
  mounted() {
    let viewMessage = this;
    let itemsRef = firebase.database().ref("messages").child(this.$store.state.chatStore.room);
    itemsRef.on("value", snapshot => {
      let data = snapshot.val();
      let messages = [];
      Object.keys(data).forEach(key => {
        messages.push({
          id: key,
          username: data[key].username,
          text: data[key].text
        });
      });
      viewMessage.messages = messages;
    });
  },
};
</script>

<style scoped>
.card-body::-webkit-scrollbar {
    width: 10px;
  }
  .card-body::-webkit-scrollbar-thumb {
    background-color: #2f3542;
  }
  .card-body::-webkit-scrollbar-track {
    background-color: grey;
  }
  
h3 {
  font-size: 30px;
  text-align: center;
}
input {
  width: 100%;
  border-radius: 4px;
  border: 1px solid rgb(156, 156, 156);
  padding-left: 2px;
  padding-right: 2px;
}
.message-body {
  width: 100%;
  height: 80vh;
  margin: auto;
  
}
.message-text {
  min-width: 10%;
  border-radius: 4px;
}
.message {
  font-size: 14px;
}
.mg-text {
  color: rgb(158, 235, 143);
  font-weight: bolder;
}
.message-body input {
  width: 80%;
  border-radius: 4px;
  border: 1px solid rgb(156, 156, 156);
  height: 6vh;
  padding-left: 2px;
  padding-right: 2px;
}
.card {
  width: 100%;
  max-height: 88%;
  margin: auto;
}
.card-body {
  min-height: 72vh;
  overflow-x: hidden;
  overflow-y: scroll;
}
</style>