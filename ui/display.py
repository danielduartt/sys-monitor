import sys
import os

try:
    from dashing import HSplit, VSplit, Text, HGauge, VGauge
except ModuleNotFoundError:
    print("Missing required package 'dashing' (py-dashing).\nInstall dependencies with: pip install -r requirements.txt")
    sys.exit(1)

from time import sleep

try:
    from jobs.cpu import CPU
    from jobs.memory import Memory
    from jobs.disk import Disk
    from jobs.network import Network
    from jobs.swap import Swap
    from jobs.sensores import Sensors
    
except ModuleNotFoundError:
    project_root = os.path.dirname(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    try:
        from jobs.cpu import CPU
        from jobs.memory import Memory
        from jobs.disk import Disk
        from jobs.network import Network
        from jobs.swap import Swap
        from jobs.sensores import Sensors
    except ModuleNotFoundError as e:
        print(f"Erro na Importação dos Módulos: {e}")
        raise

def bytes_para_human(n, sufixo='B/s'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(n) < 1024.0:
            return f"{n:3.1f} {unit}{sufixo}"
        n /= 1024.0
    return f"{n:.1f} Y{sufixo}"

class Dashboard:
    def __init__(self):
        self.network_monitor = Network()


        self.cpu_chart_hist = VGauge(title="CPU (%)", border_color=5, color=5)
        self.cpu_chart_cores = VSplit(
            HGauge(title="CPU 1 (%)", border_color=7, color=7),
            HGauge(title="CPU 2 (%)", border_color=7, color=7),
            HGauge(title="CPU 3 (%)", border_color=7, color=7),
            HGauge(title="CPU 4 (%)", border_color=7, color=7),
            HGauge(title="CPU 5 (%)", border_color=7, color=7),
            HGauge(title="CPU 6 (%)", border_color=7, color=7),
            title="Uso por Núcleo", border_color=7
            )

        self.mem_chart_hist = VGauge(border_color=3, color=3)
        self.swap_chart = VGauge(title="Uso de Swap (%)", border_color=6, color=6)
        self.memory_window = VSplit(self.mem_chart_hist, self.swap_chart, title="Memória", border_color=3)

        self.battery_chart = HGauge(title="Informações da Bateria: ", border_color=4, color=4)
        self.ventilador_chart = HGauge(title="Informações do Ventilador: ", border_color=4, color=4)

        self.sensors_window = VSplit(self.battery_chart, self.ventilador_chart, title="Sensores", border_color=4)

        
        
        self.net_text = Text("Calculando...", title="Velocidade da Rede", border_color=2)
        self.disk_text = Text("Coletando...", title="Uso de Disco", border_color=6)
        

        self.ui = HSplit(
            VSplit(self.cpu_chart_hist, self.cpu_chart_cores, title="CPU Info", border_color=5),
            VSplit(self.memory_window, self.sensors_window, title="Memória & Sensores", border_color=3),
            VSplit(self.battery_chart, self.net_text, self.disk_text, title="Bateria, Rede & Disco", border_color=4),
            title="Sys Monitor - Pressione Ctrl+C para sair"
        )

    def _update_ui(self, cpu_data, mem_data, swap_data, disk_data, net_data, sensors_data):
        """Método privado para atualizar todos os widgets com novos dados."""

        #== Memória Updates==
        self.mem_chart_hist.value = mem_data['percent']
        self.mem_chart_hist.title = f"Uso de RAM: {mem_data['percent']}%)"

        self.swap_chart.value = swap_data['percent']
        self.swap_chart.title = f"Uso de Swap: {swap_data['percent']}%)"

        # == CPU Updates==
        self.cpu_chart_hist.value = cpu_data['geral']
        self.cpu_chart_hist.title = f"Uso de CPU: {cpu_data['geral']}%)"

        for i, (core, value) in enumerate(zip(self.cpu_chart_cores.items, cpu_data['por_nucleo'])):
            core.value = value
            core.title = f"CPU {i+1}: {value}%)"
        # == Sensores Updates==
        self.battery_chart.value = sensors_data['battery']['percent'] if sensors_data['battery']['percent'] is not None else 0
        if sensors_data['battery']['percent'] is not None:
            self.battery_chart.title = f"Bateria: {sensors_data['battery']['percent']}% - {'Carregando' if sensors_data['battery']['power_plugged'] else 'Descarregando'}"
        else:
            self.battery_chart.title = "Bateria: Não disponível"
        self.ventilador_chart.value = max(sensors_data['fans'].values()) if sensors_data['fans'] else 0
        if sensors_data['fans']:
            self.ventilador_chart.title = f"Ventilador: {', '.join([f'{name}: {speed} RPM' for name, speed in sensors_data['fans'].items()])}"  
        else:
            self.ventilador_chart.title = "Ventilador: Não disponível"  
        # == Disco Updates==


    def run(self):
        """Inicia o loop principal do dashboard."""
        try:
            while True:
                cpu_data = CPU.get_cpu_info()
                mem_data = Memory.get_memory_info()
                disk_data = Disk.get_disk_info()
                net_data = self.network_monitor.get_network_speed()
                swap_data = Swap.get_swap_info()
                sensors_data = Sensors.get_sensors_info()
                self._update_ui(cpu_data, mem_data, swap_data, disk_data, net_data, sensors_data)
                self.ui.display()
                sleep(1)
        except KeyboardInterrupt:
            print("\nSaindo do dashboard...")

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()