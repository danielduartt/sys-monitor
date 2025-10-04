import psutil

class Disk:
    @staticmethod
    def get_disk_info(max_partitions=2):
        """Retorna o uso das partições de disco."""
        partitions_info = []
        # all=False para pegar apenas discos físicos
        for part in psutil.disk_partitions(all=False)[:max_partitions]:
            try:
                usage = psutil.disk_usage(part.mountpoint)
                partitions_info.append({
                    "mountpoint": part.mountpoint,
                    "percent": usage.percent
                })
            except Exception:
                continue
        return partitions_info