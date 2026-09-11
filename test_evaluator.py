from app.services.path_evaluator import PathEvaluator


evaluator = PathEvaluator()


resources = {
    "cpu_percent": 20,
    "ram_percent": 60,
    "bandwidth_mbps": 75,
    "cloud_quota_percent": 0
}


result = evaluator.evaluate(
    "complex",
    resources
)


for path, values in result.items():

    print(f"\n{path.upper()}")

    for key, value in values.items():
        print(f"{key}: {value}")