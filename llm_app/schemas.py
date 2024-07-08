from pydantic import BaseModel
from typing import Dict

class PredictionRequest(BaseModel):
    input_data: Dict[str, str]  # 包含文本和图像 URL 的字典

class PredictionResponse(BaseModel):
    result: str

# 定义响应模型
class HelloWorldResponse(BaseModel):
    message: str
