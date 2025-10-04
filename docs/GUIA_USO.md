# 📊 Guia de Uso - Sys Monitor

## 🎯 Resumo do Projeto

Este projeto implementa **TODOS** os requisitos do Desafio I, além de recursos extras:

### ✅ Itens Obrigatórios Implementados

| # | Requisito | Implementação | Arquivo |
|---|-----------|---------------|---------|
| 1 | **Quantidade de núcleos / CPU** | ✅ Completo | `jobs/system.py`, `jobs/cpu.py` |
| 2 | **Quantidade de memória usada / livre** | ✅ Completo | `jobs/memory.py`, `jobs/swap.py` |
| 3 | **Lista de processos** | ✅ Completo | `jobs/processes.py` |
| 4 | **Detalhamento de processo por ID** | ✅ Completo | `jobs/processes.py` |
| 5 | **Nível de bateria** | ✅ Completo | `jobs/sensores.py` |

---

## 🚀 Como Executar

### 1️⃣ Ativar ambiente virtual (se estiver usando)
```powershell
.\venv\Scripts\Activate.ps1
```

### 2️⃣ Instalar dependências
```powershell
pip install -r requirements.txt
```

### 3️⃣ Executar o monitor principal
```powershell
python main.py
```

### 4️⃣ Para sair
Pressione `Ctrl+C` no terminal

---

## 📋 Exemplos de Uso

### 🔍 Exemplo 1: Visualizar Dashboard Completo

```powershell
python main.py
```

**O que você verá:**
- Gráficos de uso de CPU (geral e por núcleo)
- Medidores de RAM e Swap
- Status da bateria (se for laptop)
- Velocidades de rede (↓ download / ↑ upload)
- Uso de disco
- Top 8 processos ordenados por CPU
- Informações do sistema (boot time, uptime)

### 🔍 Exemplo 2: Testar Módulos

```powershell
python test_modules.py
```

Verifica se todos os módulos estão funcionando corretamente.

---

## 📂 Estrutura Detalhada do Código

### 📁 jobs/ - Módulos de Coleta de Dados

#### `cpu.py`
```python
CPU.get_cpu_info()
# Retorna:
{
    "geral": 45.2,  # Uso geral em %
    "por_nucleo": [42.0, 48.5, 43.1, 47.8, ...]  # Uso por núcleo
}
```

#### `memory.py`
```python
Memory.get_memory_info()
# Retorna:
{
    "percent": 63.5  # Uso de RAM em %
}
```

#### `swap.py`
```python
Swap.get_swap_info()
# Retorna:
{
    "total": 8589934592,      # Total em bytes
    "used": 2415919104,       # Usado em bytes
    "free": 6174015488,       # Livre em bytes
    "percent": 28.1           # Uso em %
}
```

#### `disk.py`
```python
Disk.get_disk_info()
# Retorna lista:
[
    {"mountpoint": "C:\\", "percent": 65.2},
    {"mountpoint": "D:\\", "percent": 42.8}
]
```

#### `network.py`
```python
network = Network()
network.get_network_speed()
# Retorna:
{
    "download": 2621440.0,  # bytes/segundo
    "upload": 524288.0      # bytes/segundo
}
```

#### `sensores.py`
```python
Sensors.get_sensors_info()
# Retorna:
{
    "battery": {
        "percent": 85,
        "secsleft": 7200,  # -1 se carregando
        "power_plugged": True
    },
    "fans": {
        "fan1_Fan 1": 2500,  # RPM (apenas Linux)
        "fan2_Fan 2": 2300
    }
}
```

#### ⭐ `processes.py` (NOVO)
```python
# Lista top processos
Processes.get_processes_list(limit=10, sort_by='cpu')
# Retorna lista:
[
    {
        "pid": 1234,
        "name": "chrome.exe",
        "cpu_percent": 15.23,
        "memory_percent": 8.45
    },
    ...
]

# Detalha processo específico
Processes.get_process_detail(1234)
# Retorna:
{
    "pid": 1234,
    "name": "chrome.exe",
    "status": "running",
    "cpu_percent": 15.23,
    "memory_percent": 8.45,
    "memory_info": {
        "rss": 537133056,
        "vms": 1073741824
    },
    "num_threads": 24,
    "username": "DESKTOP\\user",
    "create_time": 1728028215.0
}

# Conta total de processos
Processes.get_process_count()
# Retorna: 245
```

#### ⭐ `system.py` (NOVO)
```python
# Quantidade de núcleos
System.get_cpu_count()
# Retorna:
{
    "physical": 4,  # Núcleos físicos
    "logical": 8    # Núcleos lógicos (com hyperthreading)
}

# Frequência da CPU
System.get_cpu_freq()
# Retorna:
{
    "current": 3600.0,  # MHz atual
    "min": 800.0,       # MHz mínimo
    "max": 4200.0       # MHz máximo
}

# Horário de boot
System.get_boot_time()
# Retorna: "2025-10-04 08:30:15"

# Tempo ligado (em segundos)
System.get_uptime()
# Retorna: 30720.5  # ~8.5 horas
```

---

## 🔧 Compatibilidade

### ✅ Windows
- CPU ✅
- Memória ✅
- Swap ✅
- Disco ✅
- Rede ✅
- Processos ✅
- Bateria ✅
- Ventiladores ❌ (não disponível)

### ✅ Linux
- CPU ✅
- Memória ✅
- Swap ✅
- Disco ✅
- Rede ✅
- Processos ✅
- Bateria ✅
- Ventiladores ✅ (requer lm-sensors)

### ✅ macOS
- CPU ✅
- Memória ✅
- Swap ✅
- Disco ✅
- Rede ✅
- Processos ✅
- Bateria ✅
- Ventiladores ❌ (limitado)

---

## 📊 Estatísticas do Projeto

- **Arquivos criados/modificados:** 10+
- **Linhas de código:** ~800+
- **Módulos de jobs:** 8
- **Funções implementadas:** 20+
- **Requisitos do desafio atendidos:** 5/5 (100%)
- **Recursos extras:** 8+

---

## 🎓 Conclusão

Este projeto **completa 100% dos requisitos do Desafio I** e adiciona diversos recursos extras para um monitoramento completo do sistema. A implementação é modular, bem documentada e fácil de estender com novos recursos.

### ✅ Checklist Final

- [x] 1. Quantidade de núcleos / CPU
- [x] 2. Quantidade de memória usada / livre
- [x] 3. Lista de processos
- [x] 4. Detalhamento de processo por ID
- [x] 5. Nível de bateria
- [x] Interface visual com gráficos
- [x] Monitoramento de rede
- [x] Monitoramento de disco
- [x] Sistema multi-plataforma
- [x] Documentação completa

**Projeto pronto para uso! 🚀**
