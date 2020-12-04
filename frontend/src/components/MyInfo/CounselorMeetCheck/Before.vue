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
                수락/거절
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
                  color="green"
                  @click="confirmReservation(item.counselReservation_pk , i)"
                >
                <v-icon>mdi-check</v-icon>
                </v-btn>
                <v-btn
                  icon
                  color="red"
                >
                <v-icon>mdi-close</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
          <v-snackbar
            v-model="snackbar"
            timeout=-1
            color="success"
            >
            수락 완료
            <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="move()"
        >
          Close
        </v-btn>
      </template>
          </v-snackbar>
        </template>
      </v-simple-table>
      </v-tab-item>
</template>

<script>
import axios from 'axios';

export default {
  props:["cid","lists","userlists"],
    data(){
        return{
            counselor_id: this.cid,
            tab: null,
            list: this.lists,
            userlist: this.userlists,
            snackbar: false,

        }
    },
    created(){
    },

    methods:{

      confirmReservation(num , i){
        axios.put(process.env.VUE_APP_API_URL+"counsel/confirmcounselReservation/" + num).then(() => {
            this.list.splice(i, 1);
            this.snackbar = true;
            console.log("Reservation Success")            
        }).catch(()=>{
            console.log("Reservation Fail")
        });

      },
      move(){
        this.snackbar = false;
        this.$forceUpdate();
      },
    }

}
</script>

<style>

</style>