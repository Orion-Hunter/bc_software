from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index() -> Dict[str, str]:
    return {"API": "BC Software API", "VERSION": "1"}
