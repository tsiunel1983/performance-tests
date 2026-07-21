from grpc import Channel
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, \
    GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, \
    GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, \
    MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, \
    MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, \
    MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, \
    MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, \
    MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, \
    MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import \
    MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse



class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для работы с документами.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetContractOperation через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода ContractOperationsReceipt через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetContractOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetContractOperationsSummary через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperations через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными операции контракта.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получение информации об операции по operation_id.

        :return: Ответ с информацией об операции.
        """
        request = GetOperationRequest(peration_id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получение чека по операции по operation_id.
        :param operation_id: Идентификатор операции.
        :return: Ответ с информацией об операции.
        """
        request = GetOperationReceiptRequest(peration_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получение списка операций для определенного счета.
        :param operation_id: Идентификатор операции.
        :return: Ответ с информацией об операции.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получение статистики по операциям для определенного счета.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
         Создание операции комиссии.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
         Создание операции пополнения.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
         Создание операции кэшбэка.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
         Создание операции перевода.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
         Создание операции покупки.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
         Создание операции оплаты по счету.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
          Создание операции снятия наличных денег.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с информацией об операции.
        """
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())
