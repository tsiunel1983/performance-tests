from api_client_issue_physical_card import accounts_gateway_client
from clients.http.gateway.cards.client import build_cards_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
cards_gateway_client = build_cards_gateway_http_client()
contract_documents_gateway_client = build_documents_gateway_http_client()
tariff_documents_gateway_client = build_documents_gateway_http_client()

create_user_response = users_gateway_client.create_user()
"""
Используем метод create_user
Создаем пользователя
"""
print("Create user response: ", create_user_response)

open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response["user"]["id"])
"""
Используем метод open_credit_card_account
Открываем кредитный счет
"""
print("Open credit card account response: ", open_credit_card_account_response)

get_tariff_document_response = tariff_documents_gateway_client.get_contract_document(
    account_id = open_credit_card_account_response["account"]["id"])
"""
Используем метод get_contract_document
Получаем документ о тарифе кредитного счета.
"""
print("Get tariff document response: ", get_tariff_document_response)

get_contract_document_response = contract_documents_gateway_client.get_contract_document(
    account_id = open_credit_card_account_response["account"]["id"])
"""
Используем метод get_contract_document
Получаем контракт об открытии кредитного счета.
"""
print("Get contract document response: ", get_contract_document_response)
