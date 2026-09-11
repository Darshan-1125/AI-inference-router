class PathEvaluator:

    def evaluate(self, complexity, resources):

        ram = resources["ram_percent"]
        cpu = resources["cpu_percent"]
        bandwidth = resources["bandwidth_mbps"]
        cloud_quota = resources["cloud_quota_percent"]

        paths = {}

        # -------------------------
        # LOCAL
        # -------------------------

        local_quality = {
            "simple": 7,
            "medium": 7,
            "complex": 6
        }[complexity]

        local_cost = 1

        local_latency = 5

        local_resource_penalty = 0

        if ram > 80:
            local_resource_penalty += 4

        if cpu > 80:
            local_resource_penalty += 4

        paths["local"] = {
            "quality": local_quality,
            "cost": local_cost,
            "latency": local_latency,
            "resource_penalty": local_resource_penalty,
            "available": ram < 95 and cpu < 95
        }

        # -------------------------
        # CLOUD
        # -------------------------

        cloud_quality = {
            "simple": 8,
            "medium": 9,
            "complex": 10
        }[complexity]

        cloud_cost = 8

        cloud_latency = 7

        cloud_resource_penalty = 0

        if bandwidth < 20:
            cloud_resource_penalty += 5

        paths["cloud"] = {
            "quality": cloud_quality,
            "cost": cloud_cost,
            "latency": cloud_latency,
            "resource_penalty": cloud_resource_penalty,
            "available": cloud_quota > 0 and bandwidth > 0
        }

        # -------------------------
        # OFFLINE
        # -------------------------

        paths["offline"] = {
            "quality": 3,
            "cost": 0,
            "latency": 1,
            "resource_penalty": 0,
            "available": True
        }

        return paths