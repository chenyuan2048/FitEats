<template>
  <view class="container">
    <view class="header">您的美食健康专家，快来试试吧！</view>
    
    <!-- 图片上传部分 -->
    <view class="upload-section">
      <button @click="chooseImage">上传图片</button>
      <image v-if="imageSrc" :src="imageSrc" mode="widthFix" class="uploaded-image"></image>
      <view class="result-section" v-if="result">
        <text class="result-title">美食健康结果：</text>
        <view class="result-item" v-for="(value, key) in result" :key="key">
          <text>{{ key }}: {{ value }}</text>
        </view>
      </view>
    </view>

    <!-- 对话部分 -->
    <view class="chat-section">
      <scroll-view scroll-y="true" class="chat-window">
        <view v-for="(message, index) in chatHistory" :key="index" :class="{'user-message': message.sender === 'user', 'model-message': message.sender === 'model'}">
          <text>{{ message.text }}</text>
        </view>
      </scroll-view>
      <view class="input-section">
        <input v-model="userInput" placeholder="输入您的问题..." class="input-box"/>
        <button @click="sendMessage">发送</button>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      imageSrc: '',
      result: null,
      userInput: '',
      chatHistory: []
    }
  },
  methods: {
    chooseImage() {
      uni.chooseImage({
        count: 1,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success: (res) => {
          this.imageSrc = res.tempFilePaths[0];
          this.uploadImage(res.tempFilePaths[0]);
        }
      });
    },
    uploadImage(filePath) {
      uni.uploadFile({
        url: 'http://127.0.0.1:8000/api/v1/upload/', // 替换为你的后端接口地址
        filePath: filePath,
        name: 'file',
        success: (uploadFileRes) => {
          const data = JSON.parse(uploadFileRes.data);
          this.result = data;
        },
        fail: (err) => {
          uni.showToast({
            title: '上传失败',
            icon: 'none'
          });
        }
      });
    },
    sendMessage() {
      if (this.userInput.trim() === '') return;

      // 添加用户消息到聊天记录
      this.chatHistory.push({ sender: 'user', text: this.userInput });

      // 调用后端API处理用户输入
      uni.request({
        url: 'http://localhost:8000/api/v1/predict/glm4', // 替换为你的后端文本分析接口地址
        method: 'POST',
        data: { text: this.userInput },
        success: (res) => {
          // 添加模型回复到聊天记录
          this.chatHistory.push({ sender: 'model', text: res.data.reply });
        },
        fail: (err) => {
          uni.showToast({
            title: '发送失败',
            icon: 'none'
          });
        }
      });

      // 清空输入框
      this.userInput = '';
    }
  }
}
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.header {
  font-size: 24px;
  margin-bottom: 20px;
}
.upload-section {
  margin-bottom: 20px;
}
.uploaded-image {
  width: 100%;
  margin-top: 10px;
}
.result-section {
  width: 100%;
}
.result-title {
  font-size: 20px;
  margin-bottom: 10px;
}
.result-item {
  font-size: 16px;
  margin-bottom: 5px;
}
.chat-section {
  width: 100%;
  max-width: 600px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.chat-window {
  flex: 1;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  overflow-y: auto;
}
.user-message {
  text-align: right;
  color: blue;
}
.model-message {
  text-align: left;
  color: green;
}
.input-section {
  display: flex;
}
.input-box {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  margin-right: 10px;
}
</style>
