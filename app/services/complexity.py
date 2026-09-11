class ComplexityEstimator:

    def estimate(self, query):
        word_count = len(query.split())
        query_lower = query.lower()

        # Complex indicators
        complex_keywords = [
            "design",
            "architecture",
            "distributed",
            "optimize",
            "algorithm",
            "implementation",
            "compare",
            "analyze",
            "debug",
            "develop",
            "explain in detail"
        ]

        # Medium indicators
        medium_keywords = [
            "explain",
            "how",
            "difference",
            "why",
            "example",
            "describe"
        ]

        # Check complex keywords first
        if any(keyword in query_lower for keyword in complex_keywords):
            return "complex"

        # Then medium keywords
        if any(keyword in query_lower for keyword in medium_keywords):
            return "medium"

        # Finally use length
        if word_count <= 5:
            return "simple"

        return "medium"