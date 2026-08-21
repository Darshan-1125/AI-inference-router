from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class RouteRequest(BaseModel):
    query: str


@router.post("/route")
def route_request(request: RouteRequest):
    return {
        "query": request.query,
        "decision": "not_implemented"
    }