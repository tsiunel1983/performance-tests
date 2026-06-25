from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsAccountRequestDict(TypedDict):
    """
    Получение списка операций для определенного счета.
    """
    accountId: str

class GetOperationsSummaryAccountRequestDict(TypedDict):
    """
    Получение статистики по операциям для определенного счета.
    """
    accountId: str

class GetOperationsReceiptAccountRequestDict(TypedDict):
    """
    Получение чека по операции по operation_id.
    """
    operationId: str

class GetOperationsOperationRequestDict(TypedDict):
    """
    Получение информации об операции по operation_id.
    """
    operationId: str

class MakeFreeOperationRequestDict(TypedDict):
    """
    Создание операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Создание операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Создание операции кэшбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationRequestDict(TypedDict):
    """
    Создание операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Создание операции покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Создание операции оплаты по счету.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Создание операции снятия наличных денег.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsAccountRequestDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о, операциях.
        """
        return self.get(f"/api/v1/operations",params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryAccountRequestDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о, операциях.
        """
        return self.get(f"/api/v1/operations/operations-summary",params=QueryParams(**query))

    def get_operation_receipt_api(self, query: GetOperationsReceiptAccountRequestDict) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param query: Словарь с параметрами запроса, например: {'operationId': '123'}.
        :return: Объект httpx.Response с данными о, операциях.
        """
        return self.get(f"/api/v1/operations/operation-receipt/",params=QueryParams(**query))

    def get_operation_api(self, query: GetOperationsOperationRequestDict) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.

        :param query: Словарь с параметрами запроса, например: {'operationId': '123'}.
        :return: Объект httpx.Response с данными о, операциях.
        """
        return self.get(f"/api/v1/operations/",params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFreeOperationRequestDict)->Response:
        """
        Создание операции комиссии.

        :param request: Словарь с операцией комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation",json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict)->Response:
        """
        Создание операции пополнения.

        :param request: Словарь с операцией пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation",json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict)->Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с операцией кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation",json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict)->Response:
        """
        Создание операции перевода.

        :param request: Словарь с операцией перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation",json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict)->Response:
        """
        Создание  операции покупки.

        :param request: Словарь с операцией покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation",json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict)->Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с операцией оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation",json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict)->Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с операцией снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation",json=request)

def build_operation_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
"""
Функция создает экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.
 return: Готовый к использованию OperationsGatewayHTTPClient.
"""