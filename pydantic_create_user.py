from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError


class UserSchema(BaseModel):
    """
    модель данных пользователя
    """
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName", default="Имя")
    first_name: str = Field(alias="firstName", default="Фамилия")
    middle_name: str = Field(alias="middleName", default="Отчество")
    phone_number: str = Field(alias="phoneNumber", default="*-***-***-**-**")


class CreateUserRequestSchema(BaseModel):
    """
    запрос на создание пользователя
    """
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName", default="Имя")
    first_name: str = Field(alias="firstName", default="Фамилия")
    middle_name: str = Field(alias="middleName", default="Отчество")
    phone_number: str = Field(alias="phoneNumber", default="*-***-***-**-**")


class CreateUserResponseSchema(BaseModel):
    """
    ответ с данными созданного пользователя
    """
    user: list[UserSchema] = Field(default_factory=list)


try:
    create_user_request_schema = CreateUserRequestSchema(
        email="yura-tsiune@example.com",
        lastName="Yuriy",
        firstName="Tsiunel",
        middleName="Nikolaevich",
        phoneNumber="89*********"
    )
except ValidationError as error:
    print(error)
    print(error.errors())


create_user_response_schema = CreateUserResponseSchema(
    user=[UserSchema(
        id="1",
        email="yura-tsiune@example.com",
        lastName="Yuriy1",
        firstName="Tsiunel1",
        middleName="Nikolaevich1",
        phoneNumber="89********3"
    )
    ]
)

print("create_user_request_schema: ", create_user_request_schema)
print("create_user_response_schema: ", create_user_response_schema)
