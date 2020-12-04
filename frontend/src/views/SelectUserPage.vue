<template>
<div>
    <TopHeader></TopHeader>
    <Header></Header>
    <SelectUser></SelectUser>
</div>
</template>

<script>
import SelectUser from '../components/User/SelectUser.vue'
import TopHeader from '../components/Home/TopHeader.vue'
import Header from '../components/Home/Header.vue'

export default {
    components:{
        SelectUser,
        TopHeader,
        Header
    }
}
</script>

<style>

</style>