<template>
    <div>
        <TopHeader></TopHeader>
        <Header ></Header> 
        <!-- <Progress></Progress> -->
        <Survey ></Survey>

    </div>
</template>

<script>
import Survey from "../components/Survey/Survey.vue"
import Header from "../components/Home/Header.vue"
import TopHeader from "../components/Home/TopHeader.vue"
// import Footer from "../components/Home/Footer2.vue"
// import Progress from "../components/Survey/Progress.vue"


export default {
    components: {
        Survey,
        // Progress,
        Header,
        TopHeader
        // Footer,
    }
}
</script>

<style >
</style>