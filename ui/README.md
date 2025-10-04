# 🎨 UI - Interface do Dashboard

## 📂 Estrutura

### `display.py`
Módulo principal da interface do usuário que cria e gerencia o dashboard visual.

## 🎯 Componentes

### Classe `Dashboard`

#### Widgets Implementados:

1. **CPU Section**
   - `cpu_chart_hist`: Gráfico de uso geral da CPU (VGauge)
   - `cpu_chart_cores`: Gráficos individuais por núcleo (6x HGauge)
   - `cpu_info_text`: Informações detalhadas da CPU

2. **Memory Section**
   - `mem_chart_hist`: Medidor de uso de RAM (VGauge)
   - `swap_chart`: Medidor de uso de Swap (VGauge)

3. **Sensors Section**
   - `battery_chart`: Indicador de bateria (HGauge)
   - `ventilador_chart`: Status dos ventiladores (HGauge)

4. **Network & Disk Section**
   - `net_text`: Velocidades de rede (Text)
   - `disk_text`: Uso de discos (Text)

5. **Processes Section**
   - `processes_text`: Lista top processos (Text)
   - `system_info_text`: Informações do sistema (Text)

## 🔄 Métodos

### `__init__()`
Inicializa todos os widgets e monta o layout do dashboard.

### `_update_ui(...)`
Atualiza todos os widgets com novos dados do sistema.

**Parâmetros:**
- `cpu_data`: Dados da CPU
- `mem_data`: Dados de memória
- `swap_data`: Dados de swap
- `disk_data`: Dados de disco
- `net_data`: Dados de rede
- `sensors_data`: Dados de sensores
- `processes_data`: Lista de processos
- `system_data`: Informações do sistema
- `cpu_info`: Informações da CPU

### `run()`
Loop principal que coleta dados e atualiza o dashboard a cada segundo.

## 🎨 Layout

```
HSplit (Vertical)
├── VSplit - CPU Info
│   ├── VGauge - Uso Geral
│   ├── VSplit - Núcleos individuais
│   └── Text - Info CPU
│
├── VSplit - Memória & Sensores
│   ├── VSplit - Memória
│   │   ├── VGauge - RAM
│   │   └── VGauge - Swap
│   └── VSplit - Sensores
│       ├── HGauge - Bateria
│       └── HGauge - Ventiladores
│
├── VSplit - Rede, Disco & CPU
│   ├── Text - Velocidade Rede
│   ├── Text - Uso Disco
│   └── Text - Info CPU
│
└── VSplit - Processos & Sistema
    ├── Text - Top Processos
    └── Text - Info Sistema
```

## 🎨 Cores

- **5 (Azul)**: CPU
- **3 (Ciano)**: Memória
- **6 (Amarelo)**: Swap/Disco
- **7 (Branco)**: Núcleos CPU
- **4 (Magenta)**: Sensores
- **2 (Verde)**: Rede
- **1 (Vermelho)**: Processos

## 🔧 Funções Auxiliares

### `bytes_para_human(n, sufixo='B/s')`
Converte bytes para formato legível (KB, MB, GB, etc.)

### `bytes_para_gb(n)`
Converte bytes para GB

### `segundos_para_tempo(seconds)`
Converte segundos em formato "Xh Ym"

## 🚀 Uso

```python
from ui.display import Dashboard

dashboard = Dashboard()
dashboard.run()  # Inicia o loop
```

## 📦 Dependências

- `dashing`: Framework de dashboard
- Todos os módulos `jobs/*`

## ⚡ Performance

- Atualização: 1 segundo
- Uso de CPU: Baixo (~1-2%)
- Uso de Memória: ~50-100 MB

## 🎯 Recursos

- ✅ Atualização em tempo real
- ✅ Gráficos visuais
- ✅ Cores customizadas
- ✅ Layout responsivo
- ✅ Tratamento de erros
- ✅ Multi-plataforma
