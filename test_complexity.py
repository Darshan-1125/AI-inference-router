from app.services.complexity import ComplexityEstimator


estimator = ComplexityEstimator()

queries = [
    "What is RAM?",
    "Explain how Redis caching works in FastAPI",
    "Design a distributed AI inference system with dynamic resource-aware routing"
]

for query in queries:
    complexity = estimator.estimate(query)

    print(f"Query: {query}")
    print(f"Complexity: {complexity}")
    print()