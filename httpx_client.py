import time
from config import settings
import httpx

client = httpx.Client(
    base_url=settings.gateway_http_client.client_url,
    timeout=settings.gateway_http_client.timeout,
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
