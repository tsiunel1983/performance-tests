from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, RootModel

app = FastAPI()

# Создаём роутер с общим префиксом и тегом для Swagger
courses_router = APIRouter(
    prefix="/api/v1/courses",  # Добавляет /api/v1/courses ко всем путям в этом роутере
    tags=["courses-service"]  # Группирует маршруты под тегом "courses-service" в документации
)


class CourseIn(BaseModel):
    """
    Модель для приёма входных данных (создание и обновление курса).
    """
    email: EmailStr  # Валидация email-адреса
    username: str  # Логин пользователя


class CourseOut(CourseIn):
    """
    Модель для отдачи данных о курсе, включая его ID.
    """
    id: int  # Уникальный идентификатор пользователя


class CourseStore(RootModel):
    """
    In-memory хранилище курсов вместо реальной БД.
    """
    root: list[CourseOut]  # Список всех пользователей

    def find(self, user_id: int) -> CourseOut | None:
        """
        Находит пользователя по ID.
        Возвращает UserOut или None, если не найден.
        """
        return next(filter(lambda user: user.id == user_id, self.root), None)

    def create(self, user_in: CourseIn) -> CourseOut:
        """
        Создаёт нового пользователя, генерируя для него следующий ID.
        """
        user = CourseOut(id=len(self.root) + 1, **user_in.model_dump())
        self.root.append(user)
        return user

    def update(self, user_id: int, user_in: CourseIn) -> CourseOut:
        """
        Обновляет существующего пользователя по ID.
        """
        # Находим индекс существующей записи
        index = next(index for index, user in enumerate(self.root) if user.id == user_id)
        # Создаём новый объект с тем же ID и обновлёнными полями
        updated = CourseOut(id=user_id, **user_in.model_dump())
        # Заменяем в списке
        self.root[index] = updated
        return updated

    def delete(self, user_id: int) -> None:
        """
        Удаляет пользователя по ID, фильтруя список.
        """
        self.root = [user for user in self.root if user.id != user_id]


# Инициализируем хранилище пустым списком
store = CourseStore(root=[])


@courses_router.get("/{user_id}", response_model=CourseOut)
async def get_user(user_id: int):
    """
    GET /api/v1/course/{user_id}
    Возвращает пользователя по ID или 404, если не найден.
    """
    if not (user := store.find(user_id)):
        raise HTTPException(
            detail=f"Course with id {user_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return user


@courses_router.get("", response_model=list[CourseOut])
async def get_course():
    """
    GET /api/v1/course
    Возвращает список всех пользователей.
    """
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: CourseIn):
    """
    POST /api/v1/course
    Создаёт нового пользователя и возвращает его данные с ID.
    """
    return store.create(user)


@courses_router.put("/{user_id}", response_model=CourseOut)
async def update_user(user_id: int, user: CourseIn):
    """
    PUT /api/v1/course/{user_id}
    Обновляет данные пользователя по ID или возвращает 404, если не существует.
    """
    if not store.find(user_id):
        raise HTTPException(
            detail=f"Course with id {user_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return store.update(user_id, user)


@courses_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """
    DELETE /api/v1/course/{user_id}
    Удаляет пользователя по ID или возвращает 404, если не существует.
    """
    if not store.find(user_id):
        raise HTTPException(
            detail=f"Course with id {user_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    store.delete(user_id)
    # При status_code=204 тело ответа пустое


# Подключаем роутер к основному приложению
app.include_router(courses_router)
