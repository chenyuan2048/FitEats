<template>
  <view class="record-list">
    <view class="record-item" 
		  v-for="record in records" 
		  :key="record.title"
		  @click="() => handleRecordClick(record.title)">
      <image :src="record.image" class="record-image" />
      <view class="record-text">
        <text class="record-title">{{ record.title }}</text>
        <text class="record-desc">{{ record.description }}</text>
      </view>
    </view>
  </view>
</template>

<script>
import { reactive } from 'vue';

export default {
  data() {
    return {
      records: [
        {
          image: '/static/home/image/饮食记录.jpg',
          title: '每日饮食',
          description: '记录每天的饮食情况，健康饮食从我做起'
        },
		{
		  image: '/static/home/image/健身.jpg',
		  title: '健康监测',
		  description: '记录每天的运动情况，健康生活从运动开始'
		},
        {
          image: '/static/home/image/水果.jpg',
          title: 'AI营养分析师',
          description: '美食健康大模型，你想了解的知识它都知道'
        },

      ]
    }
  },
  methods: {
	  handleRecordClick(title) {
		  switch (title) {
			case "AI营养分析师":
			  uni.navigateTo({
				  url: '/pages/AIChat'
			  });
			  break;
			case "每日饮食":
			  uni.navigateTo({
				  url: '/pages/record/record'
			  });
			  break;
			case '健康监测':
			  uni.navigateTo({
				  url: '/pages/discover/discover'
			  });
			  break;
			  // 可以继续添加更多的CASE分支
			default:
			  console.warn('Unhandled title: ${title}')
		  }
	  }
  }
}
</script>

<style scoped>
.record-list {
  display: flex;
  flex-direction: column;
}
.record-item {
  display: flex;
  margin-bottom: 20px;
}
.record-image {
  width: 90px;
  height: 90px;
  margin-right: 10px;
}
.record-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.record-title {
  font-size: 22px;
  font-weight: bold;
}
.record-desc {
  font-size: 16px;
  color: #666;
}
</style>
