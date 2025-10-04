import psutil
import time

class Network:
    def __init__(self):
        """Inicializa com os valores atuais para a primeira medição."""
        self.last_io = psutil.net_io_counters()
        self.last_time = time.time()

    def get_network_speed(self):
        """Calcula e retorna a velocidade de download e upload."""
        current_io = psutil.net_io_counters()
        current_time = time.time()
        
        time_delta = current_time - self.last_time
        if time_delta == 0:
            return {"download": 0, "upload": 0}

        bytes_sent = current_io.bytes_sent - self.last_io.bytes_sent
        bytes_recv = current_io.bytes_recv - self.last_io.bytes_recv
        
        upload_speed = bytes_sent / time_delta
        download_speed = bytes_recv / time_delta
        
        # Atualiza o estado para a próxima chamada
        self.last_io = current_io
        self.last_time = current_time
        
        return {"download": download_speed, "upload": upload_speed}