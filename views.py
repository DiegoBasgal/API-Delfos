from fastapi import APIRouter
from services import UserService


user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create')
async def create_user():
    try:
        await UserService.create_user(name='name..')
    except:
        pass