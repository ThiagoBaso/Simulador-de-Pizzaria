# 🍕 Simulador de Pizzaria

Sistema de controle de pedidos para pizzaria desenvolvido em Python, com interface de terminal rica e interativa usando a biblioteca **Rich**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-TUI-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📋 Sobre o Projeto

Aplicação CLI (Command-Line Interface) que simula o fluxo operacional de uma pizzaria, desde o recebimento de pedidos até a entrega. O projeto demonstra conceitos de estruturação de dados em Python, controle de fluxo, validação de entradas e construção de interfaces ricas no terminal.

Desenvolvido como projeto acadêmico em equipe, com divisão clara de responsabilidades entre os membros.

---

## ✨ Funcionalidades

- **Fazer pedido** — cadastro completo com nome, telefone, endereço e seleção de pizzas
- **Controle de estoque** — desconto automático de ingredientes ao confirmar cada pedido
- **Desconto progressivo** — 5% para 2 pizzas, 10% para 3 ou mais
- **Consulta de pedidos** — listagem com filtro por status
- **Atualização de status** — fluxo sequencial: `Recebido → Preparando → Saiu para Entrega → Entregue`
- **Visualização de estoque** — barra visual com alertas de nível crítico, atenção e OK
- **Interface TUI** — painéis, tabelas e cores via Rich, com suporte a truecolor

---

## 🗂️ Estrutura do Código

```
pizzaria.py
├── Configuração do console (UTF-8, ANSI no Windows)
├── Constantes de tema (cores, status)
├── Cardápio (6 pizzas com ingredientes e preços)
├── Estoque inicial de ingredientes
├── Funções utilitárias (limpar, pausar, separador, tabelas...)
└── Telas
    ├── tela_menu()
    ├── tela_fazer_pedido()
    ├── tela_consultar_pedidos()
    ├── tela_atualizar_status()
    └── tela_estoque()
```

---

## 🍕 Cardápio

| # | Pizza | Preço |
|---|-------|-------|
| 1 | 🍗 Frango c/ Catupiry | R$ 35,00 |
| 2 | 🌶️ Calabresa | R$ 40,00 |
| 3 | 🧀 Quatro Queijos | R$ 45,00 |
| 4 | 🍅 Vegetariana | R$ 38,00 |
| 5 | 🥚 Portuguesa | R$ 42,00 |
| 6 | 🍓 Chocolate com Morango | R$ 39,75 |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/simulador-pizzaria.git
cd simulador-pizzaria

# Instale a dependência
pip install rich

# Execute
python pizzaria.py
```

> **Windows:** O sistema configura automaticamente o encoding UTF-8 e habilita suporte a ANSI para exibir cores corretamente.

---

## 🖥️ Demonstração

```
╭─────────────────────────────────────────────────────────────╮
│       🍕  Simulador de Pizzaria com Controle de Pedidos      │
╰─────────────────────────────────────────────────────────────╯

╭── menu ───────────────────╮  ╭── art ────────────────────╮
│                           │  │                           │
│  Escolha a opção          │  │     (ASCII art da pizza)  │
│                           │  │                           │
│  [1]  Fazer Pedido        │  │                           │
│  [2]  Consultar Pedidos   │  │                           │
│  [3]  Atualizar Status    │  │                           │
│  [4]  Ver Estoque         │  │                           │
│  [0]  Sair                │  │                           │
╰───────────────────────────╯  ╰───────────────────────────╯
```

---

## ⚙️ Regras de Negócio

| Regra | Detalhe |
|-------|---------|
| Pedido mínimo | R$ 20,00 |
| Limite por pedido | Até 10 pizzas |
| Desconto (2 pizzas) | 5% sobre o total |
| Desconto (3+ pizzas) | 10% sobre o total |
| Transição de status | Apenas sequencial (sem pular etapas) |
| Validação de estoque | Pedido bloqueado se ingredientes insuficientes |
| Telefone | Apenas dígitos numéricos |
| Endereço | Campo obrigatório |

---

## 📦 Dependências

| Biblioteca | Uso |
|------------|-----|
| [`rich`](https://github.com/Textualize/rich) | Renderização de tabelas, painéis, cores e prompts no terminal |
| `datetime` | Registro de horário dos pedidos |
| `sys`, `os`, `ctypes` | Configuração de encoding e ANSI no Windows |

---

## 📚 Conceitos Aplicados

- Manipulação de dicionários e listas em Python
- Validação de entrada do usuário
- Controle de fluxo com `match/case` (Python 3.10+)
- Interface de terminal com a biblioteca Rich (TUI)
- Separação de responsabilidades entre funções
- Trabalho colaborativo com divisão de tarefas

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
