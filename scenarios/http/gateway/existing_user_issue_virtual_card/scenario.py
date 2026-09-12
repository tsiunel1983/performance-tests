from locust import events, task
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import (
    ExistingUserIssueVirtualCardSeedsScenario,
)
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenarios = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenarios.build()

    # environment.seeds = seeds_scenarios.load()
    setattr(environment, "seeds", seeds_scenarios.load())  # noqa: B010


class IssueVirtualCardTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        # Получаем случайного пользователя из подготовленного списка
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(2)
    def get_accounts(self):
        # Получаем список счетов пользователя
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)


    @task(1)
    def issue_virtual_card(self):
        # Выполняем операцию открытия виртуальной карты
        self.issue_virtual_card_response = (
            self.cards_gateway_client.issue_virtual_card(
                user_id=self.seed_user.user_id,
                account_id=self.seed_user.debit_card_accounts[0].account_id
            )
        )

class IssueVirtualCardScenarioUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]
