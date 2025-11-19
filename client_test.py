import requests

url = "http://localhost:8002/generate"
payload = {
    "text": "뭐라 씨부리 쌌노?",  # 여기에 질문!!
    "user_id": "test_user",
    "use_rag": True,
    "use_memory": True
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
