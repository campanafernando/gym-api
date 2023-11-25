from fastapi import APIRouter

router = APIRouter()

@router.get("/users", status_code=200)
def create_role():
    return "users"
