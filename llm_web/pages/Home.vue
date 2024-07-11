<template>
  <view class="container">
    <Header />
    <NavBar />
    <RecordList />
  </view>
</template>

<script>
import Header from '@/components/Header.vue'
import NavBar from '@/components/NavBar.vue'
import RecordList from '@/components/RecordList.vue'

export default {
  components: {
    Header,
    NavBar,
    RecordList
  }
}
</script>

<style>
.container {
  padding: 10px;
}
</style>
