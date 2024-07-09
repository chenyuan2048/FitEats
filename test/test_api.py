import httpx

response = httpx.post("http://127.0.0.1:8000/api/v1/predict/glm4", verify=False)
