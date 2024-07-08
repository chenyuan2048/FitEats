from llm_app.models import GLM4Model, GLM4vModel
# from models import GLM4Model, GLM4vModel

class GLM4vService:
    def __init__(self,apikey):
        self.model = GLM4vModel(api_key = apikey)

    def predict(self, text: str, image_url: str):
        return self.model.predict(text, image_url)

class GLM4Service:
    def __init__(self,apikey):
        self.model = GLM4Model(api_key = apikey)

    def predict(self, text: str):
        return self.model.predict(text)


if __name__ == "__main__":
    # service = GLM4vService(apikey="379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk")
    # result = service.predict(text="图里有哪些食物，他们的营养成分为几何？", 
    #                          image_url="https://jeffreystorage.oss-cn-shenzhen.aliyuncs.com/c88ea91eeb434db5bd7f9c4e2b2fa416_2.png?Expires=1718455062&OSSAccessKeyId=TMP.3KhDe2HuDarctzYQnRrgFHoMQh1uPpZrgoKnS4EogFTb2C2pjgJEPqeyDGmRL6WGUVtNypp6pmpKHfJ1NHEm9MKMm9w75G&Signature=mlLrkVYifdiyBQnJ8Q6m%2FmnxuJM%3D")
    # print(result)
    # print(type(result))


    service = GLM4Service(apikey="379793e1782fc2d83dbad98b35311a70.71ZPhNbpa3TgSwKk")
    result = service.predict(text="图里有哪些食物，他们的营养成分为几何？")
    print(result)
    print(type(result))