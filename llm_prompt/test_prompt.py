import os
import io
import base64
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.json import SimpleJsonOutputParser
from zhipuai import ZhipuAI


#创建提示词模板
template = """
问题1：每日饮食辅助
背景描述：您是一位营养学专家，精通营养学、病理饮食学和内科疾病等。

任务描述：
* 请查看附图中的食物。
* 列出图中每种食物的名称和主要营养成分（例如：蛋白质、脂肪、碳水化合物、维生素和矿物质等）。
提示词示例：
"作为一位营养学专家，请帮助我分析附图中的食物，列出它们的名称和主要营养成分。"

问题2：饮食建议
背景描述：我患有痛风和甲状腺癌。

任务描述：
*根据我的健康状况，评估附图中的食物是否适合我食用。
*提供理由和相关的饮食建议。
提示词示例：
"考虑到我患有痛风和甲状腺癌，您能告诉我图中的这些食物是否适合我食用吗？请解释原因并提供相关的饮食建议。"

"""

print(template)

def load_picture(image_url: str):
    "从阿里云OSS服务器加载图片"
    # 读取图像文件
    with io.open(image_url, 'rb') as image_file:
        content = image_file.read()
        encoded_string = base64.b64encode(content)
        # 将base64编码的字节串转换为字符串
        base64_image_string = encoded_string.decode('utf-8')
    return base64_image_string



# 识别图像中的元素
def get_netural_content(image_url):
        # 构造输入数据
        input_data = {
            "text": f"问题1：您是一位营养学专家，您会营养学、病理饮食学，内科疾病等,请辅助我来每日饮食, 图里有哪些食物，他们的营养成分为几何？问题2：具有痛风和甲状腺癌疾病的我能吃这个食物吗？",
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
                            "text": "作为一位营养学专家，请帮助我分析附图中的食物，列出它们的名称和主要营养成分。考虑到我患有痛风和甲状腺癌，您能告诉我图中的这些食物是否适合我食用吗？请解释原因并提供相关的饮食建议。" ,
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
            # stream=True,
        )
        answer = response.choices[0].message
        ## 流式输出
        # for chunk in response:
        #     answer = chunk.choices[0].delta
        #     print(answer)
        # 返回预测结果
        return answer

if __name__ == "__main__":
    image_url = f"/home/cheny/codes/langchain_practice/fiteats_app/test/东北美食.jpg"
    #创建知识流水线
    picture_loading = load_picture(image_url)
    image_content = get_netural_content(picture_loading)
    print(image_content)