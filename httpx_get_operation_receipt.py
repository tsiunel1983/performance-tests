import httpx
import time

create_user_payload = {
    "email": f" user.{time.time()}@gmail.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
    }

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

open_credit_card_account_payload = {
    "userId": create_user_response_data['user']['id'],
}
open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload)
open_credit_card_account_response_data = open_credit_card_account_response.json()

make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
    "category": "taxi",
  "cardId": open_credit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_credit_card_account_response_data['account']['id']
}
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload)

make_purchase_operation_response_data = make_purchase_operation_response.json()

print('UserId: ', create_user_response_data)
print("make_top_up_operation_response_data: ",make_purchase_operation_response_data)
print("make_top_up_operation_response: ",make_purchase_operation_response.status_code)

get_purchase_operation_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_response_data['operation']['id']}"
)
get_purchase_operation_response_data = get_purchase_operation_response.json()

print("get_purchase_operation_response_data: ",get_purchase_operation_response_data)
print("get_purchase_operation_status_code: ",get_purchase_operation_response.status_code)