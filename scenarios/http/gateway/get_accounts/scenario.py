from locust import task

# Импортируем схемы ответов, чтобы типизировать shared state
from clients.http.gateway.accounts.schema import OpenDepositAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):

    create_user_response: CreateUserResponseSchema | None = None
    open_deposit_account_response: OpenDepositAccountResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем аккаунт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """
        if not self.create_user_response:
            return  # Если пользователь не был создан, нет смысла продолжать

        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем аккаунт, если счёт был успешно открыт.
        """
        if not self.create_user_response:
            return  # Если пользователь не создан, запрос аккаунта невозможен

        self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения акаунта.
    """
    tasks = [GetAccountsTaskSet]

