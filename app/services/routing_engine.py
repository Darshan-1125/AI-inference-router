from app.services.path_evaluator import PathEvaluator
from app.services.scoring import ScoringEngine


class RoutingEngine:

    def __init__(self):
        self.evaluator = PathEvaluator()
        self.scorer = ScoringEngine()

    def decide(self, complexity, resources):

        paths = self.evaluator.evaluate(
            complexity,
            resources
        )

        scores = {}

        for path, values in paths.items():

            if not values["available"]:
                continue

            score = self.scorer.calculate_score(
                quality=values["quality"],
                cost=values["cost"],
                latency=values["latency"],
                resource_penalty=values["resource_penalty"]
            )

            scores[path] = score

        # Nothing available except fallback
        if not scores:
            return {
                "decision": "offline",
                "reason": "No other execution path is currently available.",
                "scores": {},
                "paths": paths
            }

        # Find highest score
        best_path = max(
            scores,
            key=scores.get
        )

        best_score = scores[best_path]

        # Create explanation
        reason = (
            f"{best_path.capitalize()} was selected "
            f"because it achieved the highest score of {best_score} "
            f"among the available execution paths."
        )

        return {
            "decision": best_path,
            "reason": reason,
            "scores": scores,
            "paths": paths
        }