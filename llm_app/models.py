import datetime
from zhipuai import ZhipuAI
from pydantic import BaseModel
from typing import List, Dict
from fastapi import FastAPI, File, UploadFile
from oss2 import to_bytes, Bucket, Auth


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


class OSSBucket:
    def __init__(self, access_key_id: str, access_key_secret: str, bucket_name: str, endpoint: str):
        self.auth = Auth(access_key_id, access_key_secret)
        self.bucket = Bucket(self.auth, endpoint, bucket_name)

    def upload_file(self, file_content: bytes, object_name: str) -> str:
        
        self.bucket.put_object(object_name, to_bytes(file_content))
        print(f"Uploaded file_path to {object_name}")
        # 如果需要生成URL，可以使用下面的代码生成预签名URL
        return {"status": "success", "object_key": object_name }
    
    def get_image_url(self, object_name: str) -> str:
        # 设置预签名URL的过期时间
        expiration = datetime.datetime.now() + datetime.timedelta(minutes=30)
        expiration_timestamp = int(expiration.timestamp())
        return self.bucket.sign_url('GET', object_name,expiration_timestamp)