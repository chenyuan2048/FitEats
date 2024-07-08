# -*- coding:utf-8 -*-
# author :jeffrey

import os
import logging

from fastapi import APIRouter, HTTPException
from llm_app.schemas import PredictionRequest, PredictionResponse
from llm_app.services import GLM4Service, GLM4vService
from zhipuai import ZhipuAI

from fastapi.responses import JSONResponse

from fastapi import FastAPI, File, UploadFile
from typing import Optional


logging.basicConfig(level=logging.DEBUG)


app = FastAPI()
router = APIRouter()
# 将 APIRouter 添加到 FastAPI 应用
app.include_router(router)

API_KEY = "379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk"

@router.get("/")
async def read_hello_world():
    try:
        # 可以在这里添加业务逻辑
        response_data = HelloWorldResponse(message="Hello FitEats")
        return HTTPException(status_code=200, detail=response_data.dict())
    except Exception as e:
        # 记录异常信息
        # 这里可以是日志记录
        raise HTTPException(status_code=500, detail={"error": str(e)})


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...))-> JSONResponse:
    try:
        # 读取文件内容
        contents = await file.read()
        # 将文件内容写入到服务器上的一个文件中
        with open("/home/cheny/codes/langchain_practice/fiteats_app/llm_app/image_data/data_file.txt", "wb") as f:
            f.write(contents)
        return JSONResponse(status_code=200, content={"filename":file.filename, "size": len(contents), 
            "message": "Image received and processed successfully"})
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
async def custom_exception_handler(request, exc):
    # 返回一个 JSON 响应
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "error": str(exc)}
    )