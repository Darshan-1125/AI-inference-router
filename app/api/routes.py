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

    # 3. Estimate complexity
    complexity = complexity_estimator.estimate(request.query)

    # 4. Ask routing engine for the best path
    routing_result = routing_engine.decide(
        complexity,
        resources
    )

    decision = routing_result["decision"]

    # 5. Execute selected path

    if decision == "local":

        response = ollama.generate(request.query)

        cache.set(request.query, response)

    elif decision == "cloud":

        # Simulated cloud for now
        response = f"Simulated cloud response for: {request.query}"

        cache.set(request.query, response)

    else:

        response = "Offline mode: Unable to process this request right now."

    # 6. Return complete routing information
    return {
        "query": request.query,
        "complexity": complexity,
        "decision": decision,
        "cache_status": "MISS",
        "resources": resources,
        "scores": routing_result["scores"],
        "response": response
    }

@router.get("/resource-status")
def resource_status():
    return monitor.get_snapshot()