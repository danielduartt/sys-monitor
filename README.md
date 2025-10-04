# PsSauro - Dashboard de Monitoramento de Sistema

**Um dashboard web para monitorar os sinais vitais do seu computador em tempo real, com o poder do Python e a agilidade do py-dashing.**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![license](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📝 Descrição

**PsSauro** transforma os dados complexos do seu sistema operacional em um dashboard web elegante e fácil de entender. Usando `psutil` para extrair informações precisas e `py-dashing` para criar widgets interativos, este projeto oferece uma visão clara e contínua do desempenho do seu hardware.

Este projeto foi desenvolvido como requisito avaliativo para a disciplina **Sistemas Operacionais**, ministrada pela Profa. Alana Oliveira no curso de Engenharia da Computação da Universidade Federal do Maranhão (UFMA).

*(Imagem de exemplo do seu dashboard pode ser inserida aqui quando estiver pronto)*
`![Exemplo do Dashboard](link_para_sua_imagem.png)`

---

## ✨ Funcionalidades

O dashboard exibe os seguintes widgets em tempo real:

-   💻 **CPU**: Gráfico com o uso percentual de cada núcleo.
-   🧠 **Memória**: Medidor (gauge) mostrando o percentual de memória RAM utilizada.
-   📈 **Processos**: Lista com os principais processos por consumo de CPU ou memória.
-   🔋 **Bateria**: Widget que exibe o nível da bateria e se está carregando.
-   📊 **Informações Gerais**: Um quadro com dados estáticos, como nome do sistema, total de núcleos e memória total.

---

## 🛠️ Tecnologias Utilizadas

-   **[Python 3](https.www.python.org/)**: Linguagem base para o backend de coleta de dados.
-   **[psutil](https.pypi.org/project/psutil/)**: Biblioteca para obter informações do sistema.
-   **[py-dashing](https://pypi.org/project/py-dashing/)**: Framework para a criação do dashboard.
-   **[Flask](https://flask.palletsprojects.com/)**: Servidor web que o `py-dashing` utiliza por baixo dos panos.

---

## 🚀 Instalação e Execução

Siga os passos abaixo para executar o dashboard em sua máquina local.

**Pré-requisitos:**
* [Python 3.8](https.www.python.org/downloads/) ou superior.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/PsSauro.git](https://github.com/SEU-USUARIO/PsSauro.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd PsSauro
    ```

3.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux / macOS
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Inicie o dashboard:**
    ```bash
    dashing start
    ```

6.  **Acesse o dashboard no seu navegador:**
    Abra o navegador e acesse [http://localhost:8050](http://localhost:8050).

---

## 📂 Estrutura do Projeto (Sugestão para `py-dashing`)

`py-dashing` utiliza uma estrutura de pastas específica para organizar os jobs (coleta de dados) e os widgets.

```
PsSauro/
├── ui/
│   └── display.py       
├── jobs/
│   ├── cpu.py          \# Job para coletar dados da CPU
│   ├── memory.py       \# Job para coletar dados da memória
│   └── ...             \# Outros jobs
├── requirements.txt    \# Lista de dependências
└── README.md           \# Este arquivo
```
---

## 👨‍💻 Autor

-   **[SEU NOME AQUI]** - [seu-linkedin](https://linkedin.com/in/...) | [seu-github](https://github.com/...)

---

## 📄 Licença

Este projeto está sob a licença MIT.
```
