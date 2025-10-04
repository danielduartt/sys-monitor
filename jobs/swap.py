from psutil import swap_memory

class Swap:
    @staticmethod
    def get_swap_info():
        """Retorna informações de uso da memória swap."""
        swap = swap_memory()
        return {
            "total": swap.total,
            "used": swap.used, 
            "free": swap.free,
            "percent": swap.percent,
        } 