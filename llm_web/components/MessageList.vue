<template>
  <div class="message-list">
    <div v-for="message in messages" :key="message.id" class="message-item">
      <div v-if="message.type === 'text'">{{ message.content }}</div>
      <img v-if="message.type === 'image'" :src="message.content" />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      required: true
    }
  }
}
</script>

<style>
.message-list {
  flex: 1;
  overflow-y: auto;
}

.message-item {
  margin: 10px;
}
</style>