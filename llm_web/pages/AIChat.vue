<template>
  <view class="chat-page">
<!--  <view class="header">
      <text>ChatEats,您的美食健康专家，快来试试吧!</text>
    </view> -->
    <!-- <h3>您的美食健康专家，快来试试吧!</h3> -->
    <MessageList :messages="messages" />
    <MessageInput @sendMessage="handleSendMessage" />
  </view>
</template>

<script>
	
import { mapState, mapMutations } from 'vuex';
import MessageList from '@/components/MessageList.vue';
import MessageInput from '@/components/MessageInput.vue';
	
export default {
  components: {
    MessageList,
    MessageInput
  },
  computed: {
    ...mapState(['messages'])
  },
  methods: {
    ...mapMutations(['addMessage']),
    async handleSendMessage(message) {
      this.addMessage(message);

      if (message.isUser) {
        // 显示"正在处理中"的提示信息
        this.addMessage({
          type: 'text',
          content: '正在处理中，请稍候...',
          isUser: false
        });

        try {
          const response = await new Promise((resolve, reject) => {
            uni.request({
              url: 'http://127.0.0.1:8000/api/v1/predict/glm4',
              method: 'POST',
              data: {
                input_data: {
                  text: message.content,
                  image_url: "unknown"
                }
              },
              success: (res) => resolve(res),
              fail: (err) => reject(err)
            });
          });

          const reply = response.data.result;

          // 移除“正在处理中”的提示信息
          this.messages.pop();

          // 添加API回复的内容
          this.addMessage({
            type: 'text',
            content: reply,
            isUser: false
          });
        } catch (error) {
          // 移除“正在处理中”的提示信息
          this.messages.pop();

          this.addMessage({
            type: 'text',
            content: 'fitEats回复出错，请稍后重试。',
            isUser: false
          });
        }
      }
    }
  }
};
</script>

<style scoped>
.chat-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #dcffc0;
}

.header {
  padding: 10px;
  background-color: #ffffff;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  border-bottom: 1px solid #eee;
}

.header text:nth-child(2) {
  font-size: 14px;
  font-weight: normal;
}

.message-list {
  flex: 1;
  overflow-y: auto;
}

.message-input {
  padding: 10px;
  background-color: #ffffff;
  border-top: 1px solid #eee;
}
</style>
