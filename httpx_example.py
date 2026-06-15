import httpx

# from httpx import get
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "новая задача",
#     "completed" : False,
#     "userID": 1
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos")
#
# print(response.status_code)
# print(response.json())
#
# headers = {"Authorization":"Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers = headers)

# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)

# print(response.status_code)
# print(response.json())

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers= {"Authorization":"Bearer my_secret_token"})
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")

print(response1.json())
print(response2.json())