import psutil

class CPU:
    @staticmethod
    def get_cpu_info():
        """Retorna o uso geral e por núcleo da CPU."""
        return {
            "geral": psutil.cpu_percent(interval=0.5),
            "por_nucleo": psutil.cpu_percent(percpu=True),
        }