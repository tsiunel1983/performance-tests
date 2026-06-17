import httpx
import time

client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=50,
    headers={"Authorization": "Bearer..."}
)

payload = {
    "email": f" user.{time.time()}@gmail.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
    }

response1 = client.post("/api/v1/users", json=payload)
response2 = client.post("/api/v1/users", json=payload)

print("response1",response1.text)
print("response2",response2.request.headers)