from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient


class CreateCardRequestDict(TypedDict):
    """
    Структура данных для создания новой карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards/issue-virtual-card сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request: CreateCardRequestDict)->Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с новой виртуальной картой.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card",json=request)

        """
        Клиент для взаимодействия с /api/v1/cards/issue-physical-card сервиса http-gateway.
        """
    def issue_physical_card_api(self, request: CreateCardRequestDict)->Response:
        """
        Создание новой физической карты.

        :param request: Словарь с новой физической картой.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card",json=request)