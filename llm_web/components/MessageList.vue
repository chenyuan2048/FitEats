<template>
  <view class="message-list">
    <view v-for="(message, index) in messages" :key="index" :class="['message', { 'user-message': message.isUser }]">
      <view v-if="message.type === 'text'" class="message-content">{{ message.content }}</view>
	  <view v-else-if="message.type === 'html'" class="message-content" v-html="message.content"></view>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 5px;
}

.message {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 10px;
}

.user-message {
  justify-content: flex-end;
}

.message-content {
  max-width: 70%;
  padding: 10px;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  word-break: break-word;
}

.user-message .message-content {
  background-color: #ffffff;
}
</style>