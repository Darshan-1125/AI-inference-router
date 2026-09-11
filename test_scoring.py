from app.services.scoring import ScoringEngine


engine = ScoringEngine()


local_score = engine.calculate_score(
    quality=7,
    cost=1,
    latency=5,
    resource_penalty=2
)

cloud_score = engine.calculate_score(
    quality=9,
    cost=8,
    latency=7,
    resource_penalty=1
)

offline_score = engine.calculate_score(
    quality=3,
    cost=0,
    latency=1,
    resource_penalty=0
)


print("Local score:", local_score)
print("Cloud score:", cloud_score)
print("Offline score:", offline_score)