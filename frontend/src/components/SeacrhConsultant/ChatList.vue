<template>
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
</template>

<script>
import Chat from '../SeacrhConsultant/Chat'
import firebase from 'firebase';
  export default {
    data: () => ({
      lists: [
      ],
      mdialog:false,
      
    }),
    components:{
        Chat
    },
    created() {
    if(window.$cookies.get("user").data.isuser == 0) //상담사가 아닌 일반 유저라면,
    {
        let self = this;
        let itemsRef = firebase.database().ref("users").child(window.$cookies.get("user").data.user_pk+"|user");
        itemsRef.on("value", snapshot => {
          let data = snapshot.val();
          let lists = [];
          Object.keys(data).forEach(key => {
            lists.push({

                active : true,
                receiver: data[key].receiver,
                receiverName: data[key].receiverName,
                receiverImg: data[key].receiverImg,
            });
          });
          self.lists = lists;
          console.log(lists);
    });
    }
    },
    methods: {
        openChat(chat){
            console.log(this.mdialog);
            console.log(chat);
            this.$store.state.chatStore.sender = window.$cookies.get("user").data.user_pk;
            this.$store.state.chatStore.receiver = chat.receiver;
            if(window.$cookies.get("user").data.isuser==0)
                this.$store.state.chatStore.room = window.$cookies.get("user").data.user_pk+"|"+chat.receiver;
            else{
                this.$store.state.chatStore.room = chat.receiver+"|"+window.$cookies.get("user").data.user_pk;
            }
            this.$store.state.chatStore.receiverName = chat.receiverName
            this.$store.state.chatStore.receiverImg = chat.receiverImg
            this.mdialog=true;
            console.log(this.mdialog);

        }
    },
  }
</script>