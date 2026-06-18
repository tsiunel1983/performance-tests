from clients.http.client import HTTPClient
from httpx import Response

class DocumentsGatewayHTTPTClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self,accounts_id: str) -> Response:
        """
        Получить тариф по счету.
        :param accounts_id: Идентификатор счета
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{accounts_id}")

    def get_contract_document_api(self,accounts_id: str) -> Response:
        """
        Получить контракт по счету.

        :param accounts_id: Идентификатор счета
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{accounts_id}")