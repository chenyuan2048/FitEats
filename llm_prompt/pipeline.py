#-*- coding:utf-8 -*-
#author: chenyuan

import requests
import base64
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.json import SimpleJsonOutputParser
from zhipuai import ZhipuAI

# 定义一个调用多模态模型接口的模块
# glm4v_api = APICallModule(endpoint="http://120.25.255.19:8000/api/v1/predict/glm4v", method="POST")


#第一步，调用OSS服务器，拿到图片的url
def load_picture(image_url):
        # 在实际应用中，这里可以调用一个文档检索系统
        # 示例中简单返回一个文档列表
    with open(image_url, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        # 将base64编码的字节串转换为字符串
        base64_image_string = encoded_string.decode('utf-8')
        # print(base64_image_string)
    return base64_image_string


#第二步，从url中识别元素的因素，
def get_netural_content(image_url):
        # 构造输入数据
        input_data = {
            "text": f"图里有哪些食物，他们的营养成分为几何？",
            "image_url": image_url
        }
        # 执行LangChain流水线，调用ChatGLM
        client = ZhipuAI(api_key = "379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk")
        response =  client.chat.completions.create(
            model = "glm-4v",
            messages=[
                {   
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"作为一位营养学专家，请帮助我分析附图中的食物，列出它们的名称和主要营养成分。考虑到我患有痛风和甲状腺癌，您能告诉我图中的这些食物是否适合我食用吗？请解释原因并提供相关的饮食建议。",
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
        answer = response.choices[0].message.content
        # print(answer)
        # 返回预测结果
        return answer


def decision(text):
    ## 用户需要进行知识问答
    prompt = '用户询问：' + text
    client = ZhipuAI(api_key = "379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk")
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[{"role": "system", "content": "你是一个智能对话体的决策部分，你将接收到用户询问作为输入，判断是否需要获取视觉信息。视觉信息是聊天中的重要部分问题，只有当问及一些常识问题或者知识时你才不需要视觉信息，当用户未发出询问时你需要获取视觉信息。你的输出只有'need photo'或者'no photo'.例如你觉得这次对话需要视觉信息，则只需要输出'need photo'，反之则只需要输出'no photo'."}, 
                  {"role": "user", "content": prompt}],
        temperature=0.95,
        tool_choice = None,
        max_tokens=50,

    )             
    return(response.choices[0].message.content)


def conversation(history,text,visual):
    '''历史问答部分：通过缓存和历史信息得到当下的数据'''
    prompt = '历史对话:'+ history + '用户询问：' + text + '视觉信息：' + visual
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[{"role": "system", "content": "你是一个智能对话体，所以你的思维和说话方式与人类相似。你将接收到以下部分作为输入：历史对话，用户询问，视觉信息。历史对话是你与用户聊天历史记录中与本次对话相关内容的摘要，作为你的记忆，选择性使用。用户询问是用户想聊的话题或者问题，若为未发出询问则需要你通过视觉信息或者历史纪录中你感兴趣的点发起谈话。视觉信息是你和用户聊天时你观察到的用户或者用户周围环境文字描述，在你觉得必要时请利用好视觉信息与用户聊天，若为空则说明视觉信息包含在了历史对话之中。不要输出冗余信息，输出格式为：' '。"}, 
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.95
    )
    return(response.choices[0].message.content)




# 第三步，串联结果，增加一些记录
def get_nutrient_content(question):
    client = ZhipuAI(api_key = "379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk")
    prompt_template = PromptTemplate(
        input_variables=["key_info"],
        template="根据以下关键信息生成答案：\n{key_info}\n答案：",
    )


    image_url = f"/home/cheny/codes/langchain_practice/fiteats_app/test/picture1.jpg"
    #创建知识流水线
    picture_loading = load_picture(image_url)
    image_content = get_netural_content(picture_loading)

    return image_content
    


if __name__ == "__main__":
    # 运行图片识别流水线
    question = "请识别如下图片中的营养成份。"
    answer = get_nutrient_content(question)
    print(answer)
