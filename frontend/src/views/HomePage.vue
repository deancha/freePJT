<template>
  <div>
    <TopHeader></TopHeader>
    <Header></Header>
    <Carousel style="margin-top: -7px"></Carousel>
      <main id="main">

        <Maker></Maker>
        <Card></Card>
        <!-- <Count_Section></Count_Section> -->
      </main>
        <Service></Service>
      <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import TopHeader from '../components/Home/TopHeader.vue'
import Header from '../components/Home/Header.vue'
import Carousel from '../components/Home/Carousel.vue'
import Card from '../components/Home/Card.vue'
// import Count_Section from '../components/Home/Count_Section.vue'
import Footer from '../components/Home/Footer.vue'
import Service from '../components/Home/Service_Section.vue'

import Maker from '../components/Home/Maker.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Carousel,
    TopHeader,
    Card,
    // Count_Section,
    Footer,
    Service,
    Maker
  },
  
}
</script>
<style scoped>

</style>
