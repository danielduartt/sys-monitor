import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_module(name, func, *args):
    """Testa um módulo e exibe resultado"""
    try:
        result = func(*args)
        print(f"✅ {name}: OK")
        return True
    except Exception as e:
        print(f"❌ {name}: ERRO - {e}")
        return False

def main():
    print("=" * 60)
    print("TESTE DE MÓDULOS - Sys Monitor")
    print("=" * 60)
    print()
    
    success_count = 0
    total_count = 0
    
    # Testa CPU
    total_count += 1
    try:
        from jobs.cpu import CPU
        if test_module("CPU.get_cpu_info()", CPU.get_cpu_info):
            success_count += 1
    except ImportError as e:
        print(f"❌ CPU: Erro de importação - {e}")
    
    # Testa Memory
    total_count += 1
    try:
        from jobs.memory import Memory
        if test_module("Memory.get_memory_info()", Memory.get_memory_info):
            success_count += 1
    except ImportError as e:
        print(f"❌ Memory: Erro de importação - {e}")
    
    # Testa Disk
    total_count += 1
    try:
        from jobs.disk import Disk
        if test_module("Disk.get_disk_info()", Disk.get_disk_info):
            success_count += 1
    except ImportError as e:
        print(f"❌ Disk: Erro de importação - {e}")
    
    # Testa Network
    total_count += 1
    try:
        from jobs.network import Network
        net = Network()
        if test_module("Network.get_network_speed()", net.get_network_speed):
            success_count += 1
    except ImportError as e:
        print(f"❌ Network: Erro de importação - {e}")
    
    # Testa Swap
    total_count += 1
    try:
        from jobs.swap import Swap
        if test_module("Swap.get_swap_info()", Swap.get_swap_info):
            success_count += 1
    except ImportError as e:
        print(f"❌ Swap: Erro de importação - {e}")
    
    # Testa Sensores
    total_count += 1
    try:
        from jobs.sensores import Sensors
        if test_module("Sensors.get_sensors_info()", Sensors.get_sensors_info):
            success_count += 1
    except ImportError as e:
        print(f"❌ Sensors: Erro de importação - {e}")
    
    # Testa Processes
    total_count += 1
    try:
        from jobs.processes import Processes
        if test_module("Processes.get_processes_list()", Processes.get_processes_list, 5):
            success_count += 1
    except ImportError as e:
        print(f"❌ Processes: Erro de importação - {e}")
    
    total_count += 1
    try:
        from jobs.processes import Processes
        if test_module("Processes.get_process_count()", Processes.get_process_count):
            success_count += 1
    except ImportError as e:
        print(f"❌ Processes.get_process_count: Erro de importação - {e}")
    
    # Testa System
    total_count += 1
    try:
        from jobs.system import System
        if test_module("System.get_cpu_count()", System.get_cpu_count):
            success_count += 1
    except ImportError as e:
        print(f"❌ System.get_cpu_count: Erro de importação - {e}")
    
    total_count += 1
    try:
        from jobs.system import System
        if test_module("System.get_cpu_freq()", System.get_cpu_freq):
            success_count += 1
    except ImportError as e:
        print(f"❌ System.get_cpu_freq: Erro de importação - {e}")
    
    total_count += 1
    try:
        from jobs.system import System
        if test_module("System.get_boot_time()", System.get_boot_time):
            success_count += 1
    except ImportError as e:
        print(f"❌ System.get_boot_time: Erro de importação - {e}")
    
    total_count += 1
    try:
        from jobs.system import System
        if test_module("System.get_uptime()", System.get_uptime):
            success_count += 1
    except ImportError as e:
        print(f"❌ System.get_uptime: Erro de importação - {e}")
    
    print()
    print("=" * 60)
    print(f"RESULTADO: {success_count}/{total_count} testes passaram")
    print("=" * 60)
    
    if success_count == total_count:
        print("✅ Todos os módulos estão funcionando corretamente!")
        print()
        print("Execute 'python main.py' para iniciar o monitor.")
    else:
        print("⚠️ Alguns módulos falharam. Verifique as mensagens acima.")
        print()
        print("Certifique-se de instalar as dependências:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()
