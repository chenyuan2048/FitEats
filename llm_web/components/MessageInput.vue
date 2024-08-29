<template>
  <view class="message-input">
  <button @click="chooseImage" class="upload-button">
      <i class="fas fa-upload"></i>
    </button>
    <input v-model="text" placeholder="输入消息..." class="input-text"/>
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
    chooseImage() {
      uni.chooseImage({
        count: 1, // 最多可以选择的图片数量
        sizeType: ['compressed'], // 可以指定是原图还是压缩图
        sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机
        success: (res) => {
          const tempFilePaths = res.tempFilePaths;
          if (tempFilePaths.length > 0) {
            this.uploadImage(tempFilePaths[0]);
          }
        }
      });
    },
	async uploadImage(filePath) {
		console.log("image path:", filePath);
		try{
			const uploadResult = await uni.uploadFile({
			  url: 'http://127.0.0.1:8000/api/v1/upload', // 图片上传的API地址
			  filePath: filePath,
			  name: 'file', // 文件对应的字段名称
			  formData: {}, // 可以添加额外的表单数据
			  header: { // 设置请求头，FastAPI可能需要这些头信息
						    'Content-Type': 'multipart/form-data',
						    'Accept': 'application/json'
						},
			  success: (res) => {
						// 注意：FastAPI默认返回JSON响应，所以res.data可能已经是解析后的对象
						// 尝试将响应数据转换为对象，如果已经是对象则直接使用
						const data = typeof res.data === 'string' ? JSON.parse(res.data) : res.data;
						// 如果服务器返回的是JSON字符串，你可能需要使用JSON.parse(res.data)来获取对象
						const imageUrl = res.data.image_url; // 如果已经是对象形式
						console.log("图片上传成功，", imageUrl );
							  // this.sendImageMessage(imageUrl);
							},
			  fail: (err) => {
			    console.error('图片上传失败:', err);
			  }
			});
		} catch (error) {
			console.error('图片上传失败', error);
			throw error;
		}
		},
	
    sendTextMessage() {
      if (this.text) {
        this.$emit('sendMessage', { type: 'text', content: this.text, isUser: true });
        this.text = '';
      }
    },

    sendImageMessage(imageURL) {
		console.log("分析图片中营养元素")
		try {
			const response = new Promise((resolve, reject) => {
			            uni.request({
			              url: 'http://120.25.255.19:8000/api/v1/predict/glm4v', // 分析图片的API端点
			              method: 'POST',
			              data: {
			                input_data: {
			                  text: "图里有哪些食物，他们的营养成分为几何？",
			                  image_url: imageURL
			                }
			              },
              success: (res) => resolve(res),
              fail: (err) => reject(err)
			  });
            });
			const reply = response.data.result;
			
        } catch (error) {
          console.error('图片营养元素分析错误', error);
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
.upload-button {
  padding: 10px;
  margin-right: 10px;
  background-color: #4caf50;
  color: #ffffff;
  border: none;
  border-radius: 50%;
  cursor: pointer;
}
.upload-button i {
  font-size: 16px;
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