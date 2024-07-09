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
    # service = GLM4vService(apikey="")
    # result = service.predict(text="图里有哪些食物，他们的营养成分为几何？", 
    #                          image_url=""
    # print(type(result))

    service = GLM4Service(apikey="")
    result = service.predict(text="图里有哪些食物，他们的营养成分为几何？")
    print(result)
    print(type(result))