from fastapi import APIRouter


# Создать компонент
comment_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


# Запрос на публикацию поста
@user_router.post('/public_post')
async def public_post():
    pass


# Запрос на изменение поста
@user_router.put('/change_post')
async def change_post():
    pass


# Запрос на удаление публикаций
@user_router.delete('/delete_post')
async def delete_post():
    pass

# Запрос на получение публикаций
@user_router.get('/get_all_posts')
async def get_all_posts():
    pass


# Запрос на добавление фото для публикаций
@photo_router.post('/add-photo')
async def add_user_photo():
    pass

# Удалить фото
@photo_router.delete('/delete-photo')
async def delete_photo():
    pass
