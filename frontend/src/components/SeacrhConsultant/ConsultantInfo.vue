<template>
  <v-card
    :loading="loading"
    class="mx-auto "
    max-width="374"
    max-height="650"
    style="margin-top:0px"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      :src="this.$store.state.counselorInfoStore.counselorInfo.counselor_profile"
    ></v-img>

    <v-card-title>{{this.$store.state.counselorInfoStore.counselorInfo.counselor_name}} </v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="this.$store.state.counselorInfoStore.counselorStar"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">
          {{this.$store.state.counselorInfoStore.counselorStar}} ({{this.$store.state.counselorInfoStore.counselorReviewCount}})
        </div>

        <v-dialog
      v-model="rdialog"
      max-width="400px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          text
          v-bind="attrs"
          v-on="on"
        >
          더보기
        </v-btn>
      </template>
      <v-card>
        <v-list rounded>
         <v-subheader>Reviews</v-subheader>
         <v-list-item-group
           color="primary"
         >
           <v-list-item
             v-for="(review, i) in this.$store.state.counselorInfoStore.counselorReviews"
             :key="i"
           >
              <v-list-item-avatar v-if="1">
                <v-img
                  src="https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff"
                ></v-img>
              </v-list-item-avatar>
             <v-list-item-content>
               <v-list-item-title v-text="review.review_contents"></v-list-item-title>
             </v-list-item-content>
             <v-list-item-icon>
               <v-rating
                  :value="review.star"
                  color="amber"
                  dense
                  half-increments
                  readonly
                  size="14"
              ></v-rating>
             </v-list-item-icon>
           </v-list-item>
         </v-list-item-group>
       </v-list>
      </v-card>
    </v-dialog>

      </v-row>




      <div class="my-4 subtitle-1">
        {{this.$store.state.counselorInfoStore.counselorInfo.counselor_introduce}}
      </div>
    </v-card-text>
    <v-divider class="mx-2"></v-divider>
    <v-card-text>
      <v-chip-group
        column
        >
        <v-chip v-for="major in this.$store.state.counselorInfoStore.counselorMajor"
          :key="major"
          disabled>{{major}}</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions style="">
      <v-row dense>
      <v-btn
        color="  float:left"
        style="margin:auto; margin-left:12px;"
        text
        @click="openChat()"
      >
      <v-text>
        메시지 보내기
      </v-text>
        <v-icon large  color="#124559">
          mdi-message-processing-outline
        </v-icon>
      </v-btn>
      <v-btn
        color=" "
        text
        style = "float:right; margin:auto; margin-right:12px"
        @click="checkCalendar()"
      >
      <v-text>
        상담 신청하기
      </v-text>
        <v-icon large  color="#124559" >
          mdi-calendar-clock
        </v-icon>
      </v-btn>
      </v-row>
    </v-card-actions>
    <v-dialog
             v-model="dialog"
             max-width="900px"
             max-height="100%"
             style="overflow:hidden;"
            >
      <Calendar style="overflow: hidden; overflow-y:hidden; padding:0px" :key="dialog"></Calendar>
  </v-dialog>
  <v-dialog
             v-model="mdialog"
             max-height="100%"
             scrollable
             width="30%"
            >
      <Chat style="overflow: hidden; overflow-y:hidden; padding:0px; margin:0px" :key="mdialog"  ></Chat>
  </v-dialog>
  </v-card>
</template>


<script>
  import Calendar from "../calendar/Calendar"
  import Chat from "./Chat"
  export default {
    data: () => ({
      dialog: 0,
      mdialog:false,
      loading: false,
      clear:"",
      rdialog:0
    }),
    components:{
      Calendar,
      Chat
    },
    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      checkCalendar(){
          this.$store.state.calendarStore.counselor_name = this.$store.state.counselorInfoStore.counselorInfo.counselor_name;
          this.$store.state.calendarStore.counselor_pk = this.$store.state.counselorInfoStore.counselorInfo.counselor_pk;
          this.dialog=true
        },
      openChat(){
        console.log(window.$cookies.get("user").data.user_pk);
        this.$store.state.chatStore.sender = window.$cookies.get("user").data.user_pk;
        this.$store.state.chatStore.receiver = this.$store.state.counselorInfoStore.counselorInfo.counselor_pk;
        this.$store.state.chatStore.room = window.$cookies.get("user").data.user_pk+"|"+this.$store.state.counselorInfoStore.counselorInfo.counselor_pk;
        this.$store.state.chatStore.receiverName = this.$store.state.counselorInfoStore.counselorInfo.counselor_name
        this.$store.state.chatStore.receiverImg = this.$store.state.counselorInfoStore.counselorInfo.counselor_profile
        this.mdialog=true;
      }
    },
  }
</script>

<style scoped>
 *:focus { outline:none; }
</style>