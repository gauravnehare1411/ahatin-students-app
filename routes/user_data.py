from fastapi import APIRouter, Depends
from typing import Annotated
from models.auth_models import User
from schemas.auth_schema import get_current_user

router = APIRouter()

@router.get('/user', response_model=User)
async def get_user_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user