<template>
  <v-row
  >
    <v-col
      cols="11"
      sm="3"
      class="mt-0 pt-0"
    >
      <v-menu
      
        ref="startMenu"
        v-model="startMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="startTime"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
          class="mt-0 pt-0"
            v-model="startTime"
            label="시작 시간"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
            :rules="[rules.required]"
          ></v-text-field>
        </template>
        <v-time-picker
          color="green lighten-1"
          v-if="startMenu"
          v-model="startTime"
          full-width
          @click:minute="selectStartTime()"
          scrollable=TRUE
          ampm-in-title='TRUE'
        ></v-time-picker>
      </v-menu>
    </v-col>
    
    <v-col
      cols="11"
      sm="3"
      class="mt-0 pt-0"
    >
      <v-menu
        ref="endMenu"
        v-model="endMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="endTime"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
        
      >
        <template v-slot:activator="{ on, attrs }" >
          <v-text-field
          class="mt-0 pt-0"
            v-model="endTime"
            label="종료 시간"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
            :rules="[rules.required]"
          ></v-text-field>
        </template>
        <v-time-picker
          color="green lighten-1"
          v-if="endMenu"
          v-model="endTime"
          full-width
          @click:minute="selectEndTime()"
          scrollable=TRUE
          ampm-in-title=TRUE
        ></v-time-picker>
      </v-menu>
    </v-col>
    <v-spacer></v-spacer>
    <v-col
      cols="11"
      sm="3"
      class="mt-0 pt-0"
    >
          <v-text-field
          class="mt-0 pt-0"
            v-model="fee"
            label="요금"
            right
            prepend-icon="mdi-currency-usd"
            :rules="[rules.required]"
          ></v-text-field>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        startTime: null,
        endTime: null,
        startMenu: false,
        endMenu: false,
        fee: "",
        rules: {
          required: value => !!value || 'Required.',
        },
      }
    },
    watch:{
    fee(){
      this.$store.state.calendarStore.fee = this.fee
    }
    },
    methods: {
      selectStartTime(){
        this.$store.state.calendarStore.startTime = this.startTime;
        this.$refs.startMenu.save(this.startTime)
      },
      selectEndTime(){
        this.$store.state.calendarStore.endTime = this.endTime;
        this.$refs.endMenu.save(this.endTime)
      }
    },
  }
</script>

<style scoped>
*:focus { outline:none; }
</style>