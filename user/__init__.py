from pydantic import BaseModel


# Валидатор для входа в аккаунт
class LoginUserModel(BaseModel):
    email: str
    passwors: str


# Валидатор регистрации пользователя
class RegisterUserModel(BaseModel):
    name = str
    surname = str
    email = str
    phone_number = str
    city = str
    password = str


# Валидатор изменения данных пользователя
class EditUserModel(BaseModel):
    user_id: int
    edit_data: str
    new_data: str


