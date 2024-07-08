from zhipuai import ZhipuAI
from pydantic import BaseModel

class GLM4vModel:
    def __init__(self, api_key:str):
        self.client = ZhipuAI(api_key = api_key)

    def predict(self, text:str, image_url:str):
        response = self.client.chat.completions.create(
            model="glm-4v",
            messages=[
                {
                    "role": "user",
                    "content": [
                                        {
                    "type": "text",
                    "text": text
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
                    ]
                }
            ],
        )
        data =response.choices[0].message.content
        print(f"GLM-4v model prediction for {data}")
        return data

class GLM4Model:
    def __init__(self, api_key: str):
        self.client = ZhipuAI(api_key=api_key)

    def predict(self, text: str):
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "system", 
                    "content": "你是一个智能对话体，所以你的思维和说话方式与人类相似。你将接收到以下部分作为输入：历史对话，用户询问，视觉信息。 您的回答格式如下：' '。"}, 
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text},
                    ]
                }
            ],
        )
        data = response.choices[0].message.content
        print(f"GLM-4 model prediction for {data}")
        return data

