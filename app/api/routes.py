from fastapi import APIRouter
from pydantic import BaseModel

from app.services.resource_monitor import ResourceMonitor


router = APIRouter()

monitor = ResourceMonitor()


class RouteRequest(BaseModel):
    query: str


@router.post("/route")
def route_request(request: RouteRequest):
    return {
        "query": request.query,
        "decision": "not_implemented"
    }


@router.get("/resource-status")
def resource_status():
    return monitor.get_snapshot()