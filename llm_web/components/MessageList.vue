<template>
  <view class="message-list">
    <view v-for="(message, index) in messages" :key="index" class="message">
      <text :class="{'user-message': message.isUser, 'bot-message': !message.isUser}">
        {{ message.content }}
      </text>
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
}

.message {
  padding: 10px;
}

.user-message {
  background-color: #dcffc0;
  text-align: right;
}

.bot-message {
  background-color: #ffffff;
  text-align: left;
}
</style>