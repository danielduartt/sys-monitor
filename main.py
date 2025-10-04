"""
Sys Monitor - Monitor de Sistema em Tempo Real
Exibe informações sobre CPU, memória, disco, rede, processos e sensores.
"""

import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ui.display import Dashboard

def main():
    """Função principal que inicia o dashboard."""
    print("Iniciando Sys Monitor...")
    print("Pressione Ctrl+C para sair.\n")
    
    try:
        dashboard = Dashboard()
        dashboard.run()
    except Exception as e:
        print(f"\nErro ao iniciar o dashboard: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
