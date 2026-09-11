from app.services.routing_engine import RoutingEngine


engine = RoutingEngine()


resources = {
    "cpu_percent": 20,
    "ram_percent": 60,
    "bandwidth_mbps": 75,
    "cloud_quota_percent": 80
}


queries = [
    ("What is RAM?", "simple"),
    ("Explain how Redis caching works in FastAPI", "medium"),
    ("Design a distributed AI inference system", "complex")
]


for query, complexity in queries:

    decision = engine.decide(complexity, resources)

    print(f"Query: {query}")
    print(f"Complexity: {complexity}")
    print(f"Decision: {decision}")
    print()