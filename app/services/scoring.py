class ScoringEngine:

    def __init__(
        self,
        quality_weight=0.4,
        cost_weight=0.2,
        latency_weight=0.2,
        resource_weight=0.2
    ):
        self.quality_weight = quality_weight
        self.cost_weight = cost_weight
        self.latency_weight = latency_weight
        self.resource_weight = resource_weight

    def calculate_score(
        self,
        quality,
        cost,
        latency,
        resource_penalty
    ):
        score = (
            self.quality_weight * quality
            - self.cost_weight * cost
            - self.latency_weight * latency
            - self.resource_weight * resource_penalty
        )

        return round(score, 3)