import psutil


class ResourceMonitor:

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)

    def get_ram_usage(self):
        return psutil.virtual_memory().percent

    def get_bandwidth(self):
        # Simulated for now
        return 75.0

    def get_cloud_quota(self):
        # Simulated for now
        return 80.0

    def get_snapshot(self):
        return {
            "cpu_percent": self.get_cpu_usage(),
            "ram_percent": self.get_ram_usage(),
            "bandwidth_mbps": self.get_bandwidth(),
            "cloud_quota_percent": self.get_cloud_quota()
        }