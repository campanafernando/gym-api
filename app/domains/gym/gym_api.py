from fastapi import APIRouter

router = APIRouter()

@router.get("/gym", status_code=200)
def create_role():
    return "gym"
