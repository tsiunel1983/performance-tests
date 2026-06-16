import time
import httpx

# Создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

try:
    create_user_response = httpx.post(
        "http://localhost:8003/api/v1/users",
        json=create_user_payload,
        timeout=30.0
    )

    print("Create user status code:", create_user_response.status_code)
    print("Create user response:", create_user_response.text)

    create_user_response.raise_for_status()

    create_user_response_data = create_user_response.json()
    user_id = create_user_response_data["user"]["id"]

    print("Created user id:", user_id)

except httpx.HTTPError as e:
    print(f"Ошибка при создании пользователя: {e}")
    raise SystemExit(1)

# Открытие депозитного счёта
create_deposit_payload = {
    "userId": user_id
}

try:
    create_deposit_response = httpx.post(
        "http://localhost:8003/api/v1/accounts/open-deposit-account",
        json=create_deposit_payload,
        timeout=30.0
    )

    print("\nCreate deposit status code:", create_deposit_response.status_code)
    print("Create deposit response:", create_deposit_response.text)

    create_deposit_response.raise_for_status()

    create_deposit_response_data = create_deposit_response.json()
    print("Deposit account created:", create_deposit_response_data)

except httpx.ReadTimeout:
    print("Ошибка: сервер не ответил за 30 секунд.")