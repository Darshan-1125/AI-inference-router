from fastapi import APIRouter
from pydantic import BaseModel

from app.services.resource_monitor import ResourceMonitor
from app.services.cache import RedisCache
from app.services.ollama import OllamaService
from app.services.complexity import ComplexityEstimator
from app.services.routing_engine import RoutingEngine


router = APIRouter()

monitor = ResourceMonitor()
cache = RedisCache()
ollama = OllamaService()
complexity_estimator = ComplexityEstimator()
routing_engine = RoutingEngine()


class RouteRequest(BaseModel):
    query: str


@router.post("/route")
def route_request(request: RouteRequest):

    # 1. Check cache first
    cached_response = cache.get(request.query)

    if cached_response is not None:
        return {
            "query": request.query,
            "decision": "cache",
            "cache_status": "HIT",
            "response": cached_response
        }

    # 2. Get current resources
    resources = monitor.get_snapshot()

    # 3. Estimate query complexity
    complexity = complexity_estimator.estimate(request.query)

    # 4. Decide where to route
    decision = routing_engine.decide(
        complexity,
        resources
    )

    # 5. Execute based on routing decision
    if decision == "local":

        response = ollama.generate(request.query)

        # Store successful local response
        cache.set(request.query, response)

        return {
            "query": request.query,
            "complexity": complexity,
            "decision": "local",
            "cache_status": "MISS",
            "resources": resources,
            "response": response
        }

    elif decision == "cloud":

        # Cloud is simulated for now
        response = f"Simulated cloud response for: {request.query}"

        cache.set(request.query, response)

        return {
            "query": request.query,
            "complexity": complexity,
            "decision": "cloud",
            "cache_status": "MISS",
            "resources": resources,
            "response": response
        }

    else:

        # Offline fallback
        response = "Offline mode: Unable to process this request right now."

        return {
            "query": request.query,
            "complexity": complexity,
            "decision": "offline",
            "cache_status": "MISS",
            "resources": resources,
            "response": response
        }


@router.get("/resource-status")
def resource_status():
    return monitor.get_snapshot()