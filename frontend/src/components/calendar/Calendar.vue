<template>
<v-card>
  <v-row>
    <v-col style="padding-bottom:0">
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          
          <v-menu
            bottom
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-1"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          <v-spacer></v-spacer>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
          style="margin-right:0px"
          large
         color="grey darken-2"
         class="mx-0 px-0 "
         font-size="40"
         outlined
         @click="openDialog()"
       >
         시간선택
         
       </v-btn>
          
          
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="#ebebeb"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          event-text-color="#737373"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
        ></v-calendar>
        <div style="text-align:center">
          <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
      color="#8A9EEB"
      top
    >
      {{ text }}

    </v-snackbar>
          <v-dialog
            v-model="dialog"
            max-width="690"
            scroll="no"
            overflow-x="hidden"
            style="overflow-x: hidden;"
            top
            >
      <v-card>
        <v-card-text>
          <v-container>
            <v-row>
              <v-date-picker
                 v-model="date"
                full-width
                class="mt-4 mb-0 pb-0"
                color="green lighten-1"
              ></v-date-picker>
              <TimePicker class="mt-0 pt-0"></TimePicker>
              
            </v-row>
          </v-container>
          <small>*상담사의 승인 후 상담일정이 등록됩니다.</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            닫기
          </v-btn>
          
          <v-dialog
      v-model="enddialog"
      persistent
      max-width="330px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="blue darken-1"
            text
            v-bind="attrs"
            v-on="on"
          >
            다음
          </v-btn>
      </template>
      <v-card>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12" class="pb-0 mb-0">
                <v-text-field
                  label="상담사"
                  v-model="this.$store.state.calendarStore.counselor_name"
                  required
                  readonly
                  prepend-icon="mdi-account-arrow-left-outline"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" class="pt-0 mt-0">
                <v-text-field
                  label="신청인"
                  v-model="username"
                  required
                  readonly
                  prepend-icon="mdi-account-arrow-right-outline"
                ></v-text-field>
              </v-col>
              
              <v-col cols="12" sm="12" class= "pt-0 mt-0">
              <v-text-field
              class= "pt-0 mt-0"
              v-model="date"
              label="날짜"
              prepend-icon="mdi-calendar-clock"
              readonly
              ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6" class= "pt-0 mt-0">
              <v-text-field
              class= "pt-0 mt-0"
              v-model="this.$store.state.calendarStore.startTime"
              label="시작 시간"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              ></v-text-field>
              </v-col>
              
              <v-col cols="12" sm="6" class= "pt-0 mt-0">
              <v-text-field
              v-model="this.$store.state.calendarStore.endTime"
              label="종료 시간"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              class= "pt-0 mt-0"
              ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" class="pt-0 mt-0">
                <v-text-field
                  label="요금"
                  v-model="this.$store.state.calendarStore.fee"
                  prepend-icon="mdi-currency-usd"
                  required
                  readonly
                  class= "pt-0 mt-0"
                >
                </v-text-field>
              </v-col>
              
            </v-row>
          </v-container>
          <small>*상담사의 승인 후 상담일정이 등록됩니다.</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="enddialog = false"
          >
            닫기
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="applyCounsel()"
          >
            신청
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
        </v-card-actions>
      </v-card>
        </v-dialog>
          
           
       </div>
      </v-sheet>
    </v-col>
  </v-row>
  </v-card>
</template>


<script>
import TimePicker from './TimePicker'
import CalendarApi from '../../api/CalendarApi'
  export default {
    components:{
      TimePicker
    },
    data: () => ({
      snackbar:false,
      text: '신청이 완료되었습니다. 상담사의 승인을 기다려 주세요.',
      timeout: 3700,
      username :"",
      date: new Date().toISOString().substr(0, 10),
      focus: '',
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
        day: 'Day',
      },
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      colors: ["#C2DEA0","#ABDEB1","#DED995"],
      names: [''],
      dialog: false,
      enddialog: false,
    }),
    created() {
      this.username = window.$cookies.get("user").data.user_name
      const events = []
        CalendarApi.getCounsel(
          this.$store.state.calendarStore.counselor_pk,
          (res) => { // eslint-disable-line no-unused-vars
          for(let i =0;i<res.length;i++){
              events.push({
                name: "",
                start: res[i][0].counsel_startdate,
                end: res[i][0].counsel_enddate,
                // textcolor: "#000000",
                color: this.colors[this.rnd(0, this.colors.length - 1)],
                timed: true,
          })
          }
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    console.log(error)
                  } 
        )
        this.events = [];
        this.events = events
    },
    mounted () {
      // this.$refs.calendar.checkChange()
      
    },

    methods: {
      openDialog(){
        this.dialog=true;
      },
      applyCounsel(){
        this.snackbar=true;
        if(this.$store.state.calendarStore.startTime != "" && this.$store.state.calendarStore.endTime != "" && this.$store.state.calendarStore.fee != "")
        {
        this.dialog=false;
        this.$store.state.calendarStore.date = this.date;
        let counsel_startdate = this.$store.state.calendarStore.date+"T"+this.$store.state.calendarStore.startTime;
        let counsel_enddate = this.$store.state.calendarStore.date+"T"+this.$store.state.calendarStore.endTime;
        let counsel_fee = this.$store.state.calendarStore.fee;
        let user_pk = window.$cookies.get("user").data.user_pk;
        let counselor_pk = this.$store.state.calendarStore.counselor_pk;
        let data ={
          counsel_startdate,
          counsel_enddate,
          user_pk,
          counselor_pk,
          counsel_fee
        }
        CalendarApi.applyCounsel(
          data,
          (res) => { // eslint-disable-line no-unused-vars
                  },
                  (error) =>{ // eslint-disable-line no-unused-vars
                    console.log(error)
                  } 
        )

        }else{
          alert("날짜 또는 시간 선택하세요.")
        }
      },
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => {
            this.selectedOpen = true
          }, 10)
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 10)
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      },
      rnd (a, b) {
        return Math.floor((b - a + 1) * Math.random()) + a
      },
    },
  }
</script>

<style scoped>
*:focus { outline:none; }
</style>