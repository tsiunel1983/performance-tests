from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address  # Вложенная модель

user = User(id=1, name="Alice", email="yuriy@example.ru", address={"city": "New York", "zip_code": "10001"})
print(user) # все методы
print(user.address)  # "New York"




name = input()
name2 = input()
name3 = input()
print (name3)
print(name2)
print(name)

