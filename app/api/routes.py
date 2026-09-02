from fastapi import APIRouter
from pydantic import BaseModel

from app.services.resource_monitor import ResourceMonitor
from app.services.cache import SimpleCache


router = APIRouter()

monitor = ResourceMonitor()
cache = SimpleCache()


class RouteRequest(BaseModel):
    query: str


@router.post("/route")
def route_request(request: RouteRequest):

    cached_response = cache.get(request.query)

    if cached_response is not None:
        return {
            "query": request.query,
            "decision": "cache",
            "cache_status": "HIT",
            "response": cached_response
        }

    response = f"Simulated AI response for: {request.query}"

    cache.set(request.query, response)

    return {
        "query": request.query,
        "decision": "ai",
        "cache_status": "MISS",
        "response": response
    }


@router.get("/resource-status")
def resource_status():
    return monitor.get_snapshot()