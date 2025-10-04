# jobs/system.py
import psutil
from datetime import datetime

class System:
    @staticmethod
    def get_cpu_count():
        """Retorna a quantidade de núcleos físicos e lógicos."""
        return {
            'physical': psutil.cpu_count(logical=False),
            'logical': psutil.cpu_count(logical=True)
        }
    
    @staticmethod
    def get_cpu_freq():
        """Retorna a frequência atual, mínima e máxima da CPU."""
        freq = psutil.cpu_freq()
        if freq:
            return {
                'current': freq.current,
                'min': freq.min,
                'max': freq.max
            }
        return None
    
    @staticmethod
    def get_boot_time():
        """Retorna o tempo de boot do sistema."""
        boot_time = psutil.boot_time()
        return datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_uptime():
        """Retorna o tempo que o sistema está ligado em segundos."""
        boot_time = psutil.boot_time()
        uptime = datetime.now().timestamp() - boot_time
        return uptime
