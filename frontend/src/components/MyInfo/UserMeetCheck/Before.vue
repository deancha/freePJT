<template>

        <v-simple-table >
          <thead>
            <tr>
              <th class="text-left">
                상담사
              </th>
              <th class="text-left">
                상담 시작 시간
              </th>
              <th class="text-left">
                금액
              </th>
              <!-- <th class="text-left">
                수락/거절
              </th> -->
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
            </tr>
          </tbody>
      </v-simple-table>
</template>

<script>
// import axios from 'axios';

export default {
  props:["uid","lists","userlists"],
    data(){
        return{
            counselor_id: this.uid,
            list: this.lists,
            userlist: this.userlists,

        }
    },
    created(){

    },

    methods:{
    }

}
</script>

<style>

</style>