class RoutingEngine:

    def decide(self, complexity, resources):

        ram = resources["ram_percent"]
        cpu = resources["cpu_percent"]
        bandwidth = resources["bandwidth_mbps"]
        cloud_quota = resources["cloud_quota_percent"]

        # Very limited local resources
        if ram > 85 or cpu > 90:
            if cloud_quota > 10:
                return "cloud"

            return "offline"

        # Simple requests should prefer local processing
        if complexity == "simple":
            return "local"

        # Medium requests
        if complexity == "medium":
            if ram < 75 and cpu < 80:
                return "local"

            if cloud_quota > 10:
                return "cloud"

            return "offline"

        # Complex requests
        if complexity == "complex":
            if cloud_quota > 10 and bandwidth > 10:
                return "cloud"

            if ram < 70 and cpu < 75:
                return "local"

            return "offline"

        return "offline"