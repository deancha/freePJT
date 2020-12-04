<template>
      <v-tab-item        
      >
        <v-simple-table >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                내담자 이름
              </th>
              <th class="text-left">
               상담 시작 시간
              </th>
              <th class="text-left">
                금액
              </th>
              <th class="text-left">
                화상 미팅 열기
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(item, i) in lists"
              :key="item.counselReservation_pk"
            >
              <td>{{userlist[i]}}</td>
              <td>{{item.counsel_startdate}}</td>
              <td>{{item.counsel_fee}}</td>
              <td>
                <v-btn
                  icon
                  color="blue"
                  @click="startMeet(item)"
                >
                <v-icon>mdi-video</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      </v-tab-item>
</template>

// <script>
// import axios from 'axios';

export default {
  props:["cid","lists","userlists"],
    data(){
        return{
            counselor_id: this.cid,
            tab: null,
            list: this.lists,
            userlist: this.userlists,


        }
    },
    methods:{
      startMeet(data){
        // this.$store.state.startdate = data.counsel_startdate
        // this.$store.state.enddate = data.counsel_enddate
        // this.$store.state.user_pk = data.user_pk
        // this.$store.state.counselor_pk = data.counselor_pk
        // this.$store.state.fee = data.counsel_fee
        this.$store.state.counselmeetingData = data;
        this.$router.push("/webmeeting2")
      },

    }

}
</script>

<style>

</style>