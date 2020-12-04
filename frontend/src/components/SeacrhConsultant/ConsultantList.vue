<template>
  <v-card
    class="mx-auto"
    max-width="60%"
    max-height="100%"

  >
    <v-container  max-height="10%">
        <div style="display:flex; max-height:50px">
            <!-- <v-btn
               tile
               color="#1f8500"
               outlined
               class="ml-5"
               style="border-radius:8px"
               @click="test()"
             >
               <v-icon left>
                 mdi-format-list-bulleted-square
               </v-icon>
               상세검색
             </v-btn> -->
            <v-pagination
         v-model="page"
         :length="Math.ceil(this.counselorList.length/8)"
         color="#a3d4b0"
         style="margin-left:auto"
       ></v-pagination>
        </div>
        
      <v-row dense>
        <v-col
          v-for="counselor in this.pageCounselorList"
          :key="counselor.counselor_pk"
          :cols="3"
          class="pl-2 pr-2"
        >
          <v-card class="pa-2" style="" >
            <v-img
              :src="counselor.counselor_profile"
              class="white--text align-end "
              height="220px"
              
            >
            <!-- <v-card-title v-text="card.title"></v-card-title> -->
            </v-img>
            <div class="text-center">
                <h4 class="mt-2">
                    {{counselor.counselor_name}}
                </h4>
                <v-row
        align="center"
        class="mx-0"
      >
      </v-row>
      <v-divider class="mx-1"></v-divider>
      <v-row dense>
                <v-btn
                  
                  class="px-4 ma-auto ml-2"
                  style="float:left;"
                  color=""
                  outlined
                  @click="requestInfo(counselor)"
                >
                  상세정보
                </v-btn>
                <v-btn class="mr-2" color="#1f8500" style="float:right" outlined @click="checkCalendar(counselor)"> 
                    <v-icon class="" > 
                        mdi-calendar-clock
                    </v-icon>
                </v-btn>
                </v-row>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    
     <v-dialog
             v-model="dialog"
             max-width="900px"
             max-height="100%"
             style="overflow:hidden;"
            >
      <Calendar style=" overflow: hidden; overflow-y:hidden; padding:0px; " :key="dialog" ></Calendar>
  </v-dialog>
  </v-card>
  
</template>

<script>
  import Calendar from "../calendar/Calendar"
  import CounselorApi from '../../api/CounselorApi'
  export default {
    data: () => ({
      dialog:0,
      page:1,
      pageLength: 2,
      searchField:"",
      counselorList:[],
      pageCounselorList:[],
      componentKey:0,
      items:[
    {
     eng : 'youth',
     kor : '청소년 우울증'
    },
    {
     eng : 'senior',
     kor : '노인 우울증'
    },
    {
     eng : 'pregnant',
     kor : '산후 우울증'
    },
    {
     eng : 'drug',
     kor : '약물오남용'
    },
    {
     eng : 'cancer',
     kor : '암환자'
    },
    {
     eng : 'thyroid',
     kor : '갑상선 우울증'
    },
    {
     eng : 'season',
     kor : '계절성 우울증'
    },
    ],
    }),
    watch: {
      page: function (newVal, oldVal) { // eslint-disable-line no-unused-vars
      this.pageCounselorList.splice(0);
      for (let index = (newVal-1)*8; index < (newVal)*8; index++) {
                      if(index == this.counselorList.length)
                      break
                      this.pageCounselorList.push(this.counselorList[index]);
                    }
    }
    },
    created() {
      CounselorApi.requestCounselorList(
      (res) => { // eslint-disable-line no-unused-vars
         this.$store.state.counselorInfoStore.counselorList.splice(0);
         this.$store.state.counselorInfoStore.counselorList = res;
         this.counselorList = res;
         for (let index = 0; index < 8; index++) {
           if(index == res.length)
           break
           this.pageCounselorList.push(this.$store.state.counselorInfoStore.counselorList[index]);
         }
         this.$store.state.counselorInfoStore.counselorInfo = this.counselorList[0];
         CounselorApi.getreviewcounselor(
            this.counselorList[0].counselor_pk,
            (res)=>{
              this.$store.state.counselorInfoStore.counselorStar = res.star.star__avg;
              this.$store.state.counselorInfoStore.counselorReviewCount = res.reviewlist.length;
              this.$store.state.counselorInfoStore.counselorReviews = res.reviewlist;
            },
            (error)=>{ // eslint-disable-line no-unused-vars

            }

          )
       },
       (error) =>{ // eslint-disable-line no-unused-vars
         console.log(error)
       } 
    )
    },
    mounted(){

    },
    methods: {
        Page(){
          this.pageCounselorList.splice(0);
          // for (let index = 0; index < 8; index++) {
          //       this.pageCounselorList.push(this.counselorList[index]);
          //   }
        },
        searchUser(){
          this.searchField=""
        },
        checkCalendar(counselor){
          this.$store.state.calendarStore.counselor_pk = counselor.counselor_pk;
          this.$store.state.calendarStore.counselor_name = counselor.counselor_name;
          this.dialog=true
          this.componentKey = !this.componentKey
          this.$forceUpdate();
        },
        requestInfo(counselor){
          CounselorApi.getreviewcounselor(
            counselor.counselor_pk,
            (res)=>{
              this.$store.state.counselorInfoStore.counselorStar = res.star.star__avg;
              this.$store.state.counselorInfoStore.counselorReviewCount = res.reviewlist.length;
              this.$store.state.counselorInfoStore.counselorReviews = res.reviewlist;
            },
            (error)=>{ // eslint-disable-line no-unused-vars

            }
          )
          this.$store.state.counselorInfoStore.counselorInfo = counselor;
          console.log(counselor);
         CounselorApi.counselormajorlist(
           counselor.counselor_pk,
           (res)=>{
               this.$store.state.counselorInfoStore.counselorMajor =[];
                  if(res[0].youth == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("청소년 우울증")
                  }
                  if(res[0].senior == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("노인 우울증")
                  }
                  if(res[0].pregnant == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("산후 우울증")
                  }
                  if(res[0].menopause == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("폐경기")
                  }
                  if(res[0].drug == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("약물오남용")
                  }
                  if(res[0].cancer == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("암환자")
                  }
                  if(res[0].thyroid == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("갑상선 우울증")
                  }
                  if(res[0].season == true){
                    this.$store.state.counselorInfoStore.counselorMajor.push("계절성 우울증")
                  }
            },
            (error)=>{ // eslint-disable-line no-unused-vars

            }
         ) 
        }

    },
    components:{
      Calendar
    }
  }
</script>

<style scoped>
 *:focus { outline:none; }
</style>