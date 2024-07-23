<template>
  <view class="container">
    <scroll-view scroll-y style="height: 100vh;">
      <view class="image-item" v-for="(image, index) in imageList" :key="index">
        <image :src="image.url" mode="widthFix" class="full-width-image"></image>
      </view>
    </scroll-view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      imageList: [
        { url: '/static/images/碘1.jpg' },
        { url: '/static/images/碘2.jpg' },
        { url: '/static/images/碘3.jpg' },
        { url: '/static/images/碘4.jpg' },
        { url: '/static/images/碘5.jpg' },
        { url: '/static/images/碘6.jpg' },
        { url: '/static/images/碘7.jpg' },
        { url: '/static/images/碘8.jpg' },
		{ url: '/static/images/碘9.jpg' },
      ]
    };
  }
}
</script>

<style>
.container {
  padding: 0;
}
.scroll-view {
  height: 100vh;
}
.image-item {
  width: 100%;
  margin-bottom: 20px;
}
.full-width-image {
  width: 100%;
}
</style>