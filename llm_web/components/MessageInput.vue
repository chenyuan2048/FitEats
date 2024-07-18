<template>
  <view class="message-input">
    <input v-model="text" placeholder="输入消息..." class="input-text"/>
    <input type="file" @change="sendImageMessage" class="input-file" />
    <button @click="sendTextMessage" class="send-button">发送</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      text: ''
    }
  },
  
  methods: {
    sendTextMessage() {
      if (this.text) {
        this.$emit('sendMessage', { type: 'text', content: this.text, isUser: true });
        this.text = '';
      }
    },
    sendImageMessage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.$emit('sendMessage', { type: 'image', content: e.target.result });
        };
        reader.readAsDataURL(file);
      }
    }
  }
}
</script>


<style scoped>
.message-input {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #ffffff;
  border-top: 1px solid #eee;
}
.input-text {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}
.input-file {
  display: none;
}
.send-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>