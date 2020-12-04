<template>
  <v-app>
      <Calendar></Calendar>
  </v-app>
</template>

<script>
// @ is an alias to /src
import Calendar from '../components/calendar/Calendar'
export default {
  name: 'ConsultantSchedule',
  components: {
      Calendar
  }
}
</script>
