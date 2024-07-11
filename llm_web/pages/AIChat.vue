<template>
  <div class="fit-eats">
    <h1>您的美食健康专家，快来试试吧!</h1>
    <input type="file" accept="image/*" @change="handleImageUpload" />
    <div v-if="preview" class="preview-container">
      <img :src="preview" alt="预览" />
    </div>
    <input 
      type="text" 
      placeholder="输入您的问题..." 
      v-model="input" 
    />
    <button @click="handleSubmit">发送</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: null,
      preview: null,
      input: ''
    };
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.image = file;
        this.preview = URL.createObjectURL(file);
      }
    },
    handleSubmit() {
      if (!this.image || !this.input) {
        alert('请上传图片并填写输入框');
        return;
      }
      // 处理表单提交
      console.log('Image:', this.image);
      console.log('Input:', this.input);
    }
  }
};
</script>

<style scoped>
.fit-eats {
  text-align: center;
  margin: 20px;
}

input[type="file"] {
  margin: 20px 0;
}

.preview-container {
  margin: 10px 0;
}

img {
  max-width: 100%;
  height: auto;
}

input[type="text"] {
  width: calc(100% - 22px);
  padding: 10px;
  margin: 10px 0;
  box-sizing: border-box;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
