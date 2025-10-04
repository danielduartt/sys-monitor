import psutil

class Processes:
    @staticmethod
    def get_processes_list(limit=10, sort_by='cpu'):
        """
        Retorna lista dos processos ordenados por uso de CPU ou memória.
        
        Args:
            limit: Número máximo de processos a retornar
            sort_by: 'cpu' ou 'memory' para ordenação
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                processes.append({
                    'pid': pinfo['pid'],
                    'name': pinfo['name'],
                    'cpu_percent': pinfo['cpu_percent'] or 0,
                    'memory_percent': pinfo['memory_percent'] or 0
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            
        if sort_by == 'cpu':
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        else:
            processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        
        return processes[:limit]
    
    @staticmethod
    def get_process_detail(pid):
        """
        Retorna detalhes de um processo específico por PID.
        
        Args:
            pid: ID do processo
        """
        try:
            proc = psutil.Process(pid)
            with proc.oneshot():
                return {
                    'pid': proc.pid,
                    'name': proc.name(),
                    'status': proc.status(),
                    'cpu_percent': proc.cpu_percent(),
                    'memory_percent': proc.memory_percent(),
                    'memory_info': proc.memory_info()._asdict(),
                    'num_threads': proc.num_threads(),
                    'username': proc.username() if hasattr(proc, 'username') else 'N/A',
                    'create_time': proc.create_time(),
                }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None
    
    @staticmethod
    def get_process_count():
        """Retorna o número total de processos em execução."""
        return len(psutil.pids())
