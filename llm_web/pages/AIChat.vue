<template>
  <div class="fit-eats">
    <h1>您的美食健康专家，快来试试吧!</h1>
    <MessageList :messages="messages" />
    <MessageInput @sendMessage="handleSendMessage" />
  </div>
</template>

<script>
	
import { mapState }  from "vuex";
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
		handleSendMessage(message) {
		  this.$store.commit('addMessage', message);
		}
	}
      // 处理表单提交
};
</script>

<style scoped>
.fit-eats {
  display: flex;
  flex-direction: column;
  height: 100%;
}

</style>
