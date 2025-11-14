import requests

url = "http://localhost:8002/generate"
payload = {
    "text": "내가 사려고 했던게 뭐지?",  # 여기에 질문!!
    "user_id": "test_user",
    "use_rag": True,
    "use_memory": True
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
