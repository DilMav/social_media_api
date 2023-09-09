from fastapi import APIRouter


# Создать компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


# Запрос на вход аккаунт
@user_router.post('/post')
async def post_user():
    pass


# Запрос на регистрацию аккаунта
@user_router.put('/register_user')
async def register_user():
    pass


# Запрос на удаление поста
@user_router.put('/user')
async def change_user():
    pass

# Запрос на получение у другого пользователя
@user_router.get('/user')
async def get_user():
    pass

# Запрос на редакторивания комментария
@user_router.put('/delete_comment')
async def delete_comments():
    pass


# Запрос на удаление комментария
@user_router.delete('/delete_comment')
async def delete_comments():
    pass


# Запрос на получение rj==комментарие к определённой публикации
@user_router.get('/get_comments')
async def get_comments():
    pass