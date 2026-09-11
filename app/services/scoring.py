class ScoringEngine:

    def __init__(
        self,
        quality_weight=0.5,
        cost_weight=0.15,
        latency_weight=0.15,
        resource_weight=0.20
    ):
        self.quality_weight = quality_weight
        self.cost_weight = cost_weight
        self.latency_weight = latency_weight
        self.resource_weight = resource_weight

    def normalize_lower_is_better(self, value, maximum=10):
        """
        Converts a metric where lower is better
        into a score where higher is better.
        """

        value = max(0, min(value, maximum))

        return (maximum - value) / maximum

    def normalize_higher_is_better(self, value, maximum=10):
        """
        Converts a metric where higher is better
        into a 0-1 score.
        """

        value = max(0, min(value, maximum))

        return value / maximum

    def calculate_score(
        self,
        quality,
        cost,
        latency,
        resource_penalty
    ):

        quality_score = self.normalize_higher_is_better(
            quality
        )

        cost_score = self.normalize_lower_is_better(
            cost
        )

        latency_score = self.normalize_lower_is_better(
            latency
        )

        resource_score = self.normalize_lower_is_better(
            resource_penalty
        )

        score = (
            self.quality_weight * quality_score
            + self.cost_weight * cost_score
            + self.latency_weight * latency_score
            + self.resource_weight * resource_score
        )

        return round(score, 3)