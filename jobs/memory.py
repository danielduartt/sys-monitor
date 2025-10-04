from psutil import virtual_memory

class Memory:
    @staticmethod
    def get_memory_info():
        """Retorna informações de uso da memória RAM."""
        mem = virtual_memory()
        return {
            "percent": mem.percent,
        }