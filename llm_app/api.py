# -*- coding:utf-8 -*-
# author :jeffrey

import os
import logging

from fastapi import APIRouter, HTTPException
from llm_app.schemas import PredictionRequest, PredictionResponse,HelloWorldResponse
from llm_app.services import GLM4Service, GLM4vService
from llm_app.models import OSSBucket
from zhipuai import ZhipuAI

from fastapi.responses import JSONResponse
from fastapi import FastAPI,File, UploadFile
from typing import Optional


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("uvicorn")

app = FastAPI()
router = APIRouter()
# 将 APIRouter 添加到 FastAPI 应用
app.include_router(router)

# 配置API KEY
API_KEY = "379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk"
# 阿里云OSS的配置信息
ENDPOINT = 'oss-cn-shenzhen.aliyuncs.com' # 替换为OSS服务的endpoint
ACCESS_KEY_ID = 'LTAI5tEwpqK59tqc52xLp9Bx' #你的AccessKeyId
ACCESS_KEY_SECRET = '2Zsg1UwjsEwSv4ZxATgicSPEwe3yJn' #你的AccessKeySecret
BUCKET_NAME = 'fiteats-oss'

@router.get("/")
async def read_hello_world():
    try:
        # 可以在这里添加业务逻辑
        response_data = HelloWorldResponse(message="Hello FitEats, your food health assistant.")
        return HTTPException(status_code=200, detail=response_data.model_dump())
    except Exception as e:
        # 记录异常信息
        raise HTTPException(status_code=500, detail={"error": str(e)})


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...))-> JSONResponse:
    try:
        # 读取文件内容
        filename = file.filename # 获取文件名
        oss_name = f'foods/{filename}' # oss中存放的文件名称
         # 将上传的文件保存到服务器上的临时路径
        # 读取文件内容为二进制
        file_content = await file.read()
        print(type(file_content))

        bucket = OSSBucket(ACCESS_KEY_ID, ACCESS_KEY_SECRET, BUCKET_NAME, ENDPOINT)
        result = bucket.upload_file(file_content,oss_name)
        if result["status"] == "success":
            image_url = bucket.get_image_url(oss_name)
            return JSONResponse(
                status_code=200,
                content={
                    "filename": filename,
                    "image_url": image_url,
                    "message": "File uploaded to OSS successfully"
                }
            )
        else:
            return JSONResponse(
                status_code=500,
                content={"error": "Failed to upload file to OSS"}
            )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.post("/predict/glm4", response_model=PredictionResponse)
async def predict_glm4(request: PredictionRequest):
    try:
        service = GLM4Service(API_KEY)
        prediction = service.predict(request.input_data["text"])
        return PredictionResponse(result=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/predict/glm4v", response_model=PredictionResponse)
async def predict_glm4v(request: PredictionRequest):
    try:
        service = GLM4vService(API_KEY)
        prediction = service.predict(request.input_data["text"], request.input_data["image_url"])
        return PredictionResponse(result=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 全局异常处理器
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    # 返回一个 JSON 响应
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "error": str(exc)}
    )