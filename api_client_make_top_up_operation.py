from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.operations.client import build_operation_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
create_accounts_gateway_client = build_accounts_gateway_http_client()
operation_gateway_client = build_operation_gateway_http_client()

create_user_response = users_gateway_client.create_user()
"""
Используем метод create_user
Создаем пользователя
"""
print("Create user response: ", create_user_response)

account_response = create_accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response["user"]["id"])
"""
Используем метод open_debit_card_account
Открываем дебетовый счет
"""
print("Open debit card account response: ", account_response)

make_top_up_operation_response = (operation_gateway_client.make_top_up_operation
    (
        account_id=account_response['account']['id'],
        card_id=account_response['account']['cards'][0]['id']
    )
)
"""
Используем метод make_top_up_operation
Операция пополнения карты
"""
print('Make top up operation response:', make_top_up_operation_response)