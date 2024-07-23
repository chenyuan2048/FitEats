<template>
  <view class="nav-bar">
    <button v-for="item in navItems" :key="item.text" class="nav-item" @click="navigate(item)">
      <image :src="item.icon" class="nav-icon"/>
      <text>{{ item.text }}</text>
    </button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      navItems: [
        { icon: '/static/home/icons/每日饮食.png', text: '每日饮食' },
        { icon: '/static/home/icons/健康食谱.png', text: '健康食谱' },
		{ icon: '/static/home/icons/饮食习惯.png', text: '食物碘含量' ,  page: 'iodine' },
        { icon: '/static/home/icons/习惯打卡.png', text: '其它' },
		// { icon: '/static/home/icons/科学记录.png', text: '其它，' },
		// { icon: '/static/home/icons/科学记录.png', text: '科学记录' },
		// { icon: '/static/home/icons/饮食习惯.png', text: '饮食习惯' },
		// { icon: '/static/home/icons/科学记录.png', text: '科学记录' }
      ]
    };
  },
  methods: {
    navigate(item) {
      if (item.page) {
        uni.navigateTo({
          url: `/pages/tools/${item.page}`
        });
      }
    }
  }
}
</script>

<style scoped>
.nav-bar {
  display: flex;
  flex-wrap: wrap; /* 自动换行 */
  justify-content: space-around;
  margin-bottom: 10px;
}
.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 5px; /* 调整元素间距 */
  width: calc(25% - 5px); /* 使每行显示4个元素，考虑间距 */
  max-width: 110px; /* 控制每个按钮的最大宽度 */
  font-size: 13px; /* 调整标题字体大小 */
  margin-top: 8px; /* 调整标题与图标的间距 */
}
.nav-icon {
  width: 64px;
  height: 64px;
}
</style>
