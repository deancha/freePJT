<template>
<div>
    <TopHeader style=" z-index: 1;"></TopHeader>
    <Header style=" z-index: 1;"></Header>
    <v-app >
        <div style="display:flex">
        <ConsultantInfo ></ConsultantInfo>
        <ConsultantList ></ConsultantList>
        </div>
    </v-app>
</div>
</template>

<script>
import ConsultantList from '../components/SeacrhConsultant/ConsultantList'
import TopHeader from '../components/Home/TopHeader.vue'
import Header from '../components/Home/Header.vue'
import ConsultantInfo from '../components/SeacrhConsultant/ConsultantInfo'
export default {
  name: 'SearchConsultant',
  components: {
      ConsultantList,
      TopHeader,
      Header,
      ConsultantInfo
  },
  created() {
    
  },
}
</script>
