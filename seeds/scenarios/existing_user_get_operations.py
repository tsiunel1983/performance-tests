from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedAccountsPlan, SeedCardsPlan, SeedOperationsPlan, SeedsPlan, SeedUsersPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для сценария получения информации об операциях.
    Создаём 300 пользователей, каждому из которых открываются кредитный счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Количество пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Количество счётов на пользователя
                    physical_cards=SeedCardsPlan(count=1),  # Количество физических карт
                    purchase_operations=SeedOperationsPlan(count=5), # 5 операций покупки.
                    top_up_operations=SeedOperationsPlan(count=1), # 1 операция пополнения счёта.
                    cash_withdrawal_operations=SeedOperationsPlan(count=1) # 1 операция снятия наличных.
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга
