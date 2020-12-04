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
                상담 일지 확인
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

              <v-dialog
                v-model="dialog"
                width="600px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    v-bind="attrs"
                    v-on="on"
                    color="green"
                    @click="confirmNote(i)"
                    style="margin-left: 20px"
                  >
                  <v-icon>mdi-clipboard-file</v-icon>
                </v-btn>
                </template>
                <v-card >
                <!-- <v-progress-circular v-if="!done"
                  indeterminate
                  color="success"
                ></v-progress-circular> -->
                

                      <v-card-title  >
                        <span class="headline">📔상담 일지</span>
                      </v-card-title >
                      <v-card-text class="text-right" >
                        {{ $moment(detail.counsel_startdate).format("YYYY년MM월DD일")}}
                      </v-card-text>
                      <v-card-text >
                        {{detail.counsel_detail}}
                      </v-card-text>
                </v-card>
              </v-dialog>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      </v-tab-item>
</template>

<script>
import axios from "axios";

export default {
  props:["cid","lists","userlists"],
    data(){
        return{
            counselor_id: this.cid,
            tab: null,
            list: this.lists,
            userlist: this.userlists,
            dialog: false,
            detail: "",
            counsel_date : "",
            done: false,
        }
    },
    created() {
      
    },
    methods:{
      confirmNote(num){
      this.done = false;
      this.dialog = true;
      // console.log("@@@@ " + num)
      // console.log(this.list[num].counselor_pk + "  counselor_pk")
      // console.log(this.list[num].counselReservation_pk + " counselReservation_pk")
      axios.post(process.env.VUE_APP_API_URL+"counsel/counseleddocument",{
              "counselor_pk": this.list[num].counselor_pk,
              "counselReservation_pk" : this.list[num].counselReservation_pk
       }).then((data) => {
        this.detail = data.data.data;
        this.done = true;
        
      }).catch((er)=>{
        console.log(er)
      });       

      },
      rejectReservation(){

      },
    }

}
</script>

<style>

</style>