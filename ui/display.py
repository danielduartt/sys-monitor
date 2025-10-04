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
    from jobs.processes import Processes
    from jobs.system import System
    
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
        from jobs.processes import Processes
        from jobs.system import System
    except ModuleNotFoundError as e:
        print(f"Erro na Importação dos Módulos: {e}")
        raise

def bytes_para_human(n, sufixo='B/s'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(n) < 1024.0:
            return f"{n:3.1f} {unit}{sufixo}"
        n /= 1024.0
    return f"{n:.1f} Y{sufixo}"

def bytes_para_gb(n):
    """Converte bytes para GB."""
    return n / (1024**3)

def segundos_para_tempo(seconds):
    """Converte segundos em formato legível."""
    if seconds < 0:
        return "N/A"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}m"

class Dashboard:
    def __init__(self):
        self.network_monitor = Network()

        # === CPU Section ===
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
        self.cpu_info_text = Text("Carregando...", title="Info da CPU", border_color=5)

        # === Memory Section ===
        self.mem_chart_hist = VGauge(border_color=3, color=3)
        self.swap_chart = VGauge(title="Uso de Swap (%)", border_color=6, color=6)
        self.memory_window = VSplit(self.mem_chart_hist, self.swap_chart, title="Memória", border_color=3)

        # === Battery & Sensors Section ===
        self.battery_chart = HGauge(title="Informações da Bateria: ", border_color=4, color=4)
        self.ventilador_chart = HGauge(title="Informações do Ventilador: ", border_color=4, color=4)
        self.sensors_window = VSplit(self.battery_chart, self.ventilador_chart, title="Sensores", border_color=4)

        # === Network & Disk Section ===
        self.net_text = Text("Calculando...", title="Velocidade da Rede", border_color=2)
        self.disk_text = Text("Coletando...", title="Uso de Disco", border_color=6)
        
        # === Processes Section ===
        self.processes_text = Text("Carregando processos...", title="Top Processos (CPU)", border_color=1)
        self.system_info_text = Text("Carregando info do sistema...", title="Info do Sistema", border_color=5)

        # === UI Layout ===
        self.ui = HSplit(
            VSplit(
                self.cpu_chart_hist, 
                self.cpu_chart_cores, 
                title="CPU Info", 
                border_color=5
            ),
            VSplit(
                self.memory_window, 
                self.sensors_window, 
                title="Memória & Sensores", 
                border_color=3
            ),
            VSplit(
                self.net_text, 
                self.disk_text, 
                self.cpu_info_text,
                title="Rede, Disco & CPU", 
                border_color=4
            ),
            VSplit(
                self.processes_text,
                self.system_info_text,
                title="Processos & Sistema",
                border_color=1
            ),
            title="Sys Monitor - Pressione Ctrl+C para sair"
        )

    def _update_ui(self, cpu_data, mem_data, swap_data, disk_data, net_data, sensors_data, processes_data, system_data, cpu_info):
        """Método privado para atualizar todos os widgets com novos dados."""

        # === Memória Updates ===
        self.mem_chart_hist.value = mem_data['percent']
        self.mem_chart_hist.title = f"Uso de RAM: {mem_data['percent']}%"

        self.swap_chart.value = swap_data['percent']
        self.swap_chart.title = f"Uso de Swap: {swap_data['percent']}%"

        # === CPU Updates ===
        self.cpu_chart_hist.value = cpu_data['geral']
        self.cpu_chart_hist.title = f"Uso de CPU: {cpu_data['geral']}%"

        for i, (core, value) in enumerate(zip(self.cpu_chart_cores.items, cpu_data['por_nucleo'])):
            core.value = value
            core.title = f"CPU {i+1}: {value}%"
        
        # CPU Info Text
        cpu_count = system_data['cpu_count']
        cpu_freq = system_data['cpu_freq']
        freq_text = f"Freq: {cpu_freq['current']:.0f} MHz" if cpu_freq else "Freq: N/A"
        self.cpu_info_text.text = (
            f"Núcleos Físicos: {cpu_count['physical']}\n"
            f"Núcleos Lógicos: {cpu_count['logical']}\n"
            f"{freq_text}\n"
            f"Processos Ativos: {system_data['process_count']}"
        )

        # === Sensores Updates ===
        self.battery_chart.value = sensors_data['battery']['percent'] if sensors_data['battery']['percent'] is not None else 0
        if sensors_data['battery']['percent'] is not None:
            status = 'Carregando' if sensors_data['battery']['power_plugged'] else 'Descarregando'
            self.battery_chart.title = f"Bateria: {sensors_data['battery']['percent']}% - {status}"
        else:
            self.battery_chart.title = "Bateria: Não disponível"
        
        self.ventilador_chart.value = max(sensors_data['fans'].values()) if sensors_data['fans'] else 0
        if sensors_data['fans']:
            fan_info = ', '.join([f'{name}: {speed:.0f} RPM' for name, speed in list(sensors_data['fans'].items())[:2]])
            self.ventilador_chart.title = f"Ventilador: {fan_info}"
        else:
            self.ventilador_chart.title = "Ventilador: Não disponível"

        # === Disco Updates ===
        disk_lines = []
        for disk in disk_data:
            disk_lines.append(f"{disk['mountpoint']}: {disk['percent']:.1f}% usado")
        self.disk_text.text = "\n".join(disk_lines) if disk_lines else "Sem discos detectados"

        # === Network Updates ===
        down_speed = bytes_para_human(net_data['download'])
        up_speed = bytes_para_human(net_data['upload'])
        self.net_text.text = f"↓ Download: {down_speed}\n↑ Upload: {up_speed}"

        # === Processes Updates ===
        proc_lines = []
        for i, proc in enumerate(processes_data[:8], 1):
            proc_lines.append(
                f"{i}. {proc['name'][:20]:20s} | "
                f"PID: {proc['pid']:6d} | "
                f"CPU: {proc['cpu_percent']:5.1f}% | "
                f"MEM: {proc['memory_percent']:5.1f}%"
            )
        self.processes_text.text = "\n".join(proc_lines) if proc_lines else "Nenhum processo encontrado"

        # === System Info Updates ===
        uptime = segundos_para_tempo(system_data['uptime'])
        self.system_info_text.text = (
            f"Boot Time: {system_data['boot_time']}\n"
            f"Uptime: {uptime}\n"
            f"Total de Processos: {system_data['process_count']}"
        )


    def run(self):
        """Inicia o loop principal do dashboard."""
        try:
            while True:
                # Coleta todos os dados
                cpu_data = CPU.get_cpu_info()
                mem_data = Memory.get_memory_info()
                disk_data = Disk.get_disk_info()
                net_data = self.network_monitor.get_network_speed()
                swap_data = Swap.get_swap_info()
                sensors_data = Sensors.get_sensors_info()
                processes_data = Processes.get_processes_list(limit=10, sort_by='cpu')
                
                # Dados do sistema
                system_data = {
                    'cpu_count': System.get_cpu_count(),
                    'cpu_freq': System.get_cpu_freq(),
                    'boot_time': System.get_boot_time(),
                    'uptime': System.get_uptime(),
                    'process_count': Processes.get_process_count()
                }
                
                cpu_info = System.get_cpu_freq()
                
                # Atualiza UI com todos os dados
                self._update_ui(
                    cpu_data, 
                    mem_data, 
                    swap_data, 
                    disk_data, 
                    net_data, 
                    sensors_data,
                    processes_data,
                    system_data,
                    cpu_info
                )
                
                self.ui.display()
                sleep(1)
        except KeyboardInterrupt:
            print("\nSaindo do dashboard...")

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()