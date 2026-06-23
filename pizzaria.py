from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

import sys
import os
import ctypes

if sys.platform == "win32":
    # UTF-8 no terminal
    os.system("chcp 65001 > nul")
    sys.stdout.reconfigure(encoding="utf-8")
    # Habilita ANSI
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

console = Console(
    color_system="truecolor",
    force_terminal=True,
    legacy_windows=False,
    highlight=False,
)

COR_BORDA = "white"
COR_BORDA_FRACA = "bright_black"
FUNDO = "on black"

STATUS = ["Recebido", "Preparando", "Saiu para Entrega", "Entregue"]
STATUS_CORES = {
    "Recebido": "white",
    "Preparando": "yellow",
    "Saiu para Entrega": "green",
    "Entregue": "bright_black",
}

PIZZA_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠘⠃⢀⣴⠞⠛⠛⢛⠛⠳⠶⣦⣤⣀⡀⠀⠀⠓⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⠖⢋⡝⣿⠀⠀⢀⡞⢡⢂⢊⠔⡀⠐⠠⠀⡀⠀⠈⡙⠳⠶⣤⣀⡀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠈⠀⣼⢧⣶⣚⣹⠇⠀⡄⢸⡇⣇⣆⣎⣬⣴⣥⣮⣁⣒⠠⢄⡀⠀⠀⠀⢉⡛⠶⣤⣄⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣈⡁⠀⠀⣿⣿⣱⠴⠋⠀⠀⠀⢸⠿⠻⢿⡯⢭⣭⣍⣉⣙⡛⠻⠶⣬⣁⡀⢀⡒⠬⣑⠢⣉⠛⢶⣄⡀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢺⣭⣭⣹⣳⡀⣿⠉⠀⠀⠘⠃⠀⢠⡿⠈⠁⠈⠻⢦⣀⣀⠪⠭⠙⠻⢶⣤⣉⠛⠶⣬⣑⠦⢙⠢⢙⠢⠈⠛⢶⣄⠀⠀⠀⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡀⠀⠙⠿⠿⠛⠳⣿⡄⠠⣶⠄⠀⠀⣾⠁⣀⣤⠄⠀⣀⣀⣉⠉⠙⠓⠆⠀⢹⠉⡛⠶⣤⣉⠻⢦⣙⠢⣅⠀⠀⠀⠈⡻⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠠⠀⠀⠀⠸⠇⠀⠀⠀⠀⢸⠇⣸⠛⢀⣤⠟⣻⣿⢘⡻⢧⡄⠀⠃⢸⠀⢃⠀⠀⠻⢧⣄⡛⢧⣄⠣⠀⢀⡠⠘⢄⠻⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣯⣍⡛⠳⢦⡀⠀⠀⣀⠀⠀⠤⠀⠀⣠⡟⠀⡉⢠⡟⣁⠳⣛⣋⣼⡽⢂⠻⡄⠀⠸⣆⠀⠀⠂⠈⠒⠉⡻⣦⣍⠻⣮⡣⣙⠎⠂⠁⠈⠻⢦⡀⠀⠀
⠀⠀⠰⠆⠈⢻⣭⡟⡾⣦⣙⣦⠀⠀⣰⡄⠀⠀⣼⠋⡀⢋⠀⢸⣸⡇⠂⣹⣭⠟⠰⠿⠇⡇⠀⠀⠙⠳⠶⠄⠂⠰⠄⠀⢸⡏⠳⣌⠻⣦⡀⠌⢠⡐⡌⢎⣻⣦⠀
⠀⣤⣄⣀⠀⠀⠉⠛⠿⠷⠞⠻⡇⠀⢈⠀⠀⣸⠃⠴⢀⢠⠀⠘⣧⣉⣏⠥⣹⢸⣷⢀⡼⠁⠀⢈⣤⠶⠶⠶⢦⣄⠁⠀⢸⡇⠂⠈⠳⣌⠻⣦⡱⣙⣾⡿⠻⣻⡇
⠀⣿⣧⡍⣳⡄⠈⠁⠀⠴⠄⠀⢠⡄⠀⠀⣰⡏⠐⣁⣤⣤⡄⠰⢄⠙⠿⠿⡥⠶⠖⠋⠔⠀⣴⠏⢰⡶⣦⣴⢦⠈⢳⡄⠘⣇⠁⡀⠠⡈⠳⣌⡻⣿⢻⢀⣧⣿⠃
⠀⠹⣿⣻⣿⠇⣀⣤⣤⣄⣀⠀⠀⠀⠀⢀⡟⢀⡞⠉⠠⢀⣠⡤⢤⠤⣤⡀⠀⢀⡀⣤⠀⢸⡇⣿⣷⠉⣡⡉⢹⣿⡇⢷⠀⠘⢦⣅⠐⠬⠁⣹⠟⢻⣾⠿⠋⠁⠀
⠤⠀⠈⠉⢹⣾⣧⢶⣴⣾⡿⠀⠤⠀⢀⡾⡁⢸⡀⠈⣴⠿⡵⠃⠘⠛⣎⣻⣀⠈⠁⠀⡀⠸⣇⢩⡕⣶⢈⣐⢶⣾⢀⡟⠀⠀⠀⣉⣛⣠⣾⣯⠾⠋⠁⠀⠀⠀⣀
⠀⢀⣄⠀⠙⠁⠛⠿⠛⠋⠀⠀⠀⠀⣼⢃⠃⠀⠁⣸⣯⠓⡀⠿⣠⣞⠯⡉⣩⠻⣆⠀⢿⡀⠙⢧⣙⠁⢯⡿⢈⣥⠟⠀⡠⢂⡾⢋⣩⠾⠋⠁⠀⠀⠀⠘⠁⠀⠀
⢠⡟⢹⣦⡀⠀⠶⠀⢀⡀⠈⠁⠀⣸⠏⠀⠀⠀⡀⠸⣏⢶⠇⣼⢡⣻⡞⣧⠛⣠⣹⠀⠀⠛⠶⣤⡌⠉⠛⢉⠉⠔⣀⣤⡶⣿⡷⠟⠁⠠⠀⠀⣀⣤⣴⢶⣿⡿⠀
⢾⣄⠙⠾⠻⣄⠀⠀⠈⠀⠀⠀⢠⣏⣴⠖⠋⢉⢁⠀⠈⠙⠛⢿⠃⣰⠿⢏⡔⣢⡏⠀⣈⠀⠀⠠⠀⡄⡐⢡⡶⠞⣋⣴⠞⠉⠀⠀⠀⠀⢀⡾⠋⠀⣠⡾⣿⠃⠀
⠸⣿⣎⢆⢤⠙⢶⡀⠘⠁⠀⢀⣾⠋⠄⢀⣁⣀⣀⡀⠂⠀⠇⠘⠻⢤⣶⡿⠞⠋⢀⠀⢹⠄⠈⠡⠄⢐⣡⣿⣴⠞⠋⠀⠀⠀⠀⠰⠀⠀⠸⣇⣠⠾⢗⣾⡟⠀⢠
⠀⠙⠻⠾⠼⠶⠞⠋⠀⠀⣰⠟⡁⣠⠞⠋⣩⣯⢉⣟⠳⣄⠀⠀⣀⣀⡀⠠⠀⢀⣀⣡⠞⢀⡴⠖⢛⣻⠿⠋⠁⠀⠀⣀⣴⣆⡀⠀⠀⠀⠀⠙⠳⠿⠟⠋⠀⠀⠀
⠰⠂⠀⠀⠀⠀⠠⠄⠀⣰⡇⠄⢰⠿⣿⣻⠌⠛⠋⣴⢶⡽⣇⠈⠉⠍⠙⠳⠂⣀⡥⠤⠴⢟⣡⠶⠛⠁⠀⠀⠀⣴⠟⣩⠤⢬⡛⢷⣄⠈⠃⠀⠀⠀⠀⣀⠀⠐⠂
⠀⠀⠀⢠⣷⣆⠀⠀⢰⡟⠐⠀⢸⡀⣩⣭⡀⠿⠃⠛⠟⠁⣿⠀⡀⠠⠀⠐⣰⠏⢐⣠⡶⠋⠁⠀⠀⠴⠀⠀⢸⡇⡂⣇⢾⣴⡿⠀⣹⠃⠀⠸⠂⠀⠘⠛⠂⢠⠄
⠀⠈⠁⠀⠉⢀⠀⢠⡟⡀⢰⠃⠈⢧⡻⠾⢣⣟⡌⢿⠟⣼⠃⢀⡤⢒⣡⣶⣯⡶⠛⠁⠀⡄⠀⢠⣦⠀⠀⠀⠘⢷⡑⢌⣒⢚⠱⢣⡞⠃⠀⠀⠄⠀⢺⠖⠀⠀⠀
⠀⠀⠀⣀⠀⠀⢀⣾⠀⢃⡸⡄⠀⢈⠙⠦⢬⣭⣥⠴⠚⠁⣐⣡⣴⣿⠿⠋⠁⠀⠀⠀⠀⠀⢼⠄⠁⠀⢀⠀⠀⠀⠛⠓⢶⡶⠚⠋⠀⠀⠀⣠⣴⣲⢦⡀⠀⠀⠀
⠀⠀⠀⠁⠀⢰⡟⢡⠈⠀⢣⠙⣦⡄⠑⠀⠀⠀⡆⣥⣶⠛⣭⣿⠛⠁⠀⠀⠐⠂⠈⠁⣤⠀⠈⠀⠀⢰⣾⣧⡆⠀⠀⠀⠈⠁⠀⢠⡄⠀⢰⣯⡝⠁⠈⡇⠀⠀⠀
⠀⠀⠀⠀⢀⡟⢀⠋⠀⢀⠀⠂⠀⠉⠙⠁⣴⠟⠋⣩⡴⠞⠉⠀⠀⠀⠖⠀⠀⣀⡀⠀⠉⠀⠀⢀⡀⠐⢻⠟⠂⠀⠀⠒⠀⠀⠀⠈⠁⠀⣿⣾⡇⡴⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠊⠜⠀⠄⢠⡶⣛⣿⣦⢀⣯⡶⠛⠁⠀⠀⠀⠐⠀⢀⣤⠶⣻⠟⢿⡲⢦⡀⠀⠀⣠⠀⠀⠀⠀⠀⣀⣠⣴⡶⠾⣆⠀⢰⠏⠸⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡏⡘⢀⠒⠰⢀⡿⢋⣭⠶⣿⢀⡏⠀⠀⠀⠀⠈⠁⠀⣰⠟⠁⣼⠋⠀⠈⢯⡠⠙⣦⠀⠀⢠⣤⡶⣞⣋⣉⣡⣶⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡟⢀⣁⣈⣐⣡⣾⠿⠛⠁⠀⠙⠛⠁⠀⣤⣄⣤⡄⠀⠀⣿⢰⣻⣧⠀⠀⠀⡈⣿⣓⢹⡇⠀⠈⢧⡱⢌⣛⠓⢓⣫⠔⣼⠃⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⡿⢛⣽⠟⠛⠋⠀⠀⠀⠐⠆⠀⠀⠀⠀⣼⡿⣿⡄⠀⠀⠹⣦⣺⣧⡤⣀⣠⣱⣟⣢⡿⠁⠀⢤⠀⠙⠷⠮⠭⠥⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣽⣿⣿⣿⣿⡽⠋⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


pedidos = []
proximo_id = 1

#----------------------------------NEVES-------------------------------------

cardapio = {
    "1": {
        "nome": "Frango c/ catupiry",
        "valor": 35.00,
        "emoji": "🍗",
        "ingredientes": {
            "massa": 0.25,
            "molho": 0.10,
            "frango desfiado": 0.18,
            "catupiry": 0.08,
            "mussarela": 0.15,
            "oregano": 0.01,
        },
    },
    "2": {
        "nome": "Calabresa",
        "valor": 40.00,
        "emoji": "🌶️",
        "ingredientes": {
            "massa": 0.25,
            "molho": 0.10,
            "mussarela": 0.18,
            "calabresa": 0.15,
        },
    },
    "3": {
        "nome": "Quatro Queijos",
        "valor": 45.00,
        "emoji": "🧀",
        "ingredientes": {
            "massa": 0.25,
            "molho": 0.10,
            "mussarela": 0.12,
            "parmesao": 0.08,
            "catupiry": 0.08,
            "provolone": 0.08,
        },
    },
    "4": {
        "nome": "Vegetariana",
        "valor": 38.00,
        "emoji": "🍅",
        "ingredientes": {
            "massa": 0.25,
            "molho": 0.10,
            "mussarela": 0.15,
            "tomate": 0.08,
            "cebola": 0.05,
            "pimentao": 0.05,
        },
    },
    "5": {
        "nome": "Portuguesa",
        "valor": 42.00,
        "emoji": "🥚",
        "ingredientes": {
            "massa": 0.25,
            "molho": 0.10,
            "mussarela": 0.15,
            "presunto": 0.12,
            "ovo cozido": 0.10,
            "cebola": 0.05,
            "azeitona": 0.04,
            "palmito": 0.08,
        },
    },
    "6": {
        "nome": "Chocolate com morango",
        "valor": 39.75,
        "emoji": "🍓",
        "ingredientes": {
            "massa": 0.25,
            "chocolate derretido": 0.18,
            "pedacos de morango": 0.12,
            "granulado": 0.04,
        },
    },
}

#----------------------------------WANDER-------------------------------------

estoque = {

    "massa": 20.0,
    "molho": 10.0,
    "frango desfiado": 5.0,
    "catupiry": 10.0,
    "queijo": 14.0,
    "oregano": 3.0,
    "calabresa": 5.0,
    "mussarela": 13.0,
    "parmesao": 8.0,
    "provolone": 7.0,
    "tomate": 15.0,
    "cebola": 5.0,
    "pimentao": 2.0,
    "presunto": 5.0,
    "ovo cozido": 10.0,
    "azeitona": 3.0,
    "palmito": 2.0,
    "chocolate derretido": 3.0,
    "pedacos de morango": 2.0,
    "granulado": 0.06
}

#----------------------------------Funçoes-------------------------------------

def limpar():
    console.clear()


def pausar():
    console.print()
    Prompt.ask(
        "  Pressione [yellow]ENTER[/yellow] para continuar",
        default="",
        show_default=False,
        console=console,
    )


def separador(titulo=""):
    if titulo:
        console.print(Rule(f"[dim white] {titulo} [/dim white]", style=COR_BORDA_FRACA))
        return

    console.print(Rule(style=COR_BORDA_FRACA))


def cabecalho(subtitulo=""):
    conteudo = (
        "[bold white]🍕  Simulador de Pizzaria com [bold yellow]Controle de Pedidos[/bold yellow][/bold white]"
    )
    if subtitulo:
        conteudo += f"\n[dim white italic]{subtitulo}[/dim white italic]"

    return Panel(
        Align.center(conteudo),
        border_style=COR_BORDA,
        style=FUNDO,
        padding=(0, 1),
    )


def rodape():
    hora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    total = len(pedidos)
    ativos = sum(1 for pedido in pedidos if pedido["status"] != "Entregue")

    return Panel(
        f"[dim white]{hora}[/dim white]  │  "
        f"[dim white]Total de pedidos: [white]{total}[/white]  │  "
        f"Ativos: [yellow]{ativos}[/yellow][/dim white]",
        border_style=COR_BORDA_FRACA,
        style=FUNDO,
        padding=(0, 1),
    )


def nova_tabela(expand=True, estilo_box=box.SIMPLE_HEAD):
    return Table(
        box=estilo_box,
        border_style=COR_BORDA_FRACA,
        header_style="bold yellow",
        style=FUNDO,
        expand=expand,
    )


def painel(conteudo, titulo="", borda=COR_BORDA, altura=None):
    return Panel(
        conteudo,
        title=titulo,
        border_style=borda,
        style=FUNDO,
        padding=(1, 2),
        height=altura,
    )


def tabela_cardapio():
    tabela = nova_tabela()
    tabela.add_column("#", style="bold white", width=4)
    tabela.add_column("Pizza", style="bold white", min_width=22)
    tabela.add_column("Preço", style="bold yellow", justify="right", width=10)

    for codigo, pizza in cardapio.items():
        tabela.add_row(
            codigo,
            f"{pizza['emoji']}  {pizza['nome']}",
            f"R$ {pizza['valor']:.2f}",
        )

    return tabela


def buscar_pedido(id_pedido):
    return next((pedido for pedido in pedidos if pedido["id"] == id_pedido), None)


def pedir_id_pedido():
    try:
        return int(Prompt.ask("  [white]Número do pedido[/white]", console=console))
    except ValueError:
        console.print("\n  [bold red]✗[/bold red] ID inválido.")
        return None

#----------------------------------Telas-------------------------------------

def tela_menu():
    limpar()

    opcoes = [
        ("1", "Fazer Pedido", "Registra novo pedido"),
        ("2", "Consultar Pedidos", "Lista e filtra pedidos"),
        ("3", "Atualizar Status", "Muda status de um pedido"),
        ("4", "Ver Estoque", "Exibe ingredientes em estoque"),
        ("0", "Sair", "Encerra o sistema"),
    ]

    texto_menu = Text()
    texto_menu.append("\n  Escolha a opção\n\n", style="dim white italic")

    for codigo, nome, descricao in opcoes:
        texto_menu.append(f"  [{codigo}]", style="bold yellow")
        texto_menu.append(f"  {nome}\n", style="bold white")
        texto_menu.append(f"       {descricao}\n\n", style="dim white")

    altura_paineis = len(PIZZA_ART.strip("\n").splitlines()) + 4
    painel_menu = painel(
        texto_menu,
        titulo="[dim white]menu[/dim white]",
        altura=altura_paineis,
    )
    painel_arte = painel(
        Align.center(Text(PIZZA_ART, style="dim white"), vertical="middle"),
        titulo="[dim white]art[/dim white]",
        borda=COR_BORDA_FRACA,
        altura=altura_paineis,
    )
    layout = Table.grid(expand=True)
    layout.add_column(width=46)
    layout.add_column(ratio=1)
    layout.add_row(painel_menu, painel_arte)

    console.print(cabecalho())
    console.print(layout)
    console.print(rodape())
    console.print()

#-----------------------------------MARCELO------------------------------------

def tela_fazer_pedido():
    global proximo_id

    limpar()
    console.print(cabecalho("Novo Pedido"))
    separador()
    console.print(painel(tabela_cardapio(), titulo="[yellow]── Cardápio ──[/yellow]"))
    separador()

    nome_cliente = Prompt.ask("  [white]Nome do cliente[/white]", console=console).strip()
    if not nome_cliente:
        nome_cliente = f"Cliente{proximo_id}"

    telefone_cliente = Prompt.ask("  [white]Telefone[/white]", console=console).strip()
    if not telefone_cliente.isdigit():
        console.print("\n  [bold red]✗[/bold red] Telefone deve conter apenas digitos.")
        pausar()
        return

    endereco_cliente = Prompt.ask("  [white]Endereço[/white]", console=console).strip()
    if not endereco_cliente:
        console.print("\n  [bold red]✗[/bold red] Endereço é obrigatorio.")
        pausar()
        return        

    console.print("  [dim white]Digite os códigos das pizzas separados por vírgula. Ex: 1,3,2[/dim white]")
    escolha = Prompt.ask("  [white]Pizzas[/white]", console=console)
    
    codigos = []

    for codigo in escolha.split(","):
        codigo = codigo.strip()

        if codigo in cardapio:
            codigos.append(codigo)

    if not codigos:
        console.print("\n  [bold red]✗[/bold red] Nenhuma pizza válida selecionada.")
        pausar()
        return

    if len(codigos) > 10:
        console.print("\n  [bold red]✗[/bold red] Limite de 10 pizzas por pedido.")
        pausar()
        return 

#-----------------------------------LUCAS------------------------------------

    itens = []

    for codigo in codigos:
        pizza = cardapio[codigo]
        itens.append(pizza)

#----------valida estoque------------

    necessario = {}

    for item in itens:
        for ingrediente, qtd in item["ingredientes"].items():
            if ingrediente not in necessario:
                necessario[ingrediente] = 0.0

            necessario[ingrediente] += qtd

    for ingrediente, qtd in necessario.items():
        if estoque.get(ingrediente, 0.0) < qtd:
            console.print(f"[red]Estoque insuficiente de {ingrediente}[/red]")
            pausar()
            return

#-----------------------------------

    valor_bruto = 0

    for item in itens:
        valor_bruto += item["valor"]

    desconto = 0
    if len(itens) == 2:
        desconto = 0.05
    elif len(itens) >= 3:
        desconto = 0.10

    valor_total = valor_bruto * (1.0 - desconto)
    valor_total = round(valor_total, 2)

    if valor_total < 20:
        console.print("\n  [bold red]✗[/bold red] Valor minimo para pedido: R$20.")
        pausar()
        return     

    pedido = {
        "id": proximo_id,
        "cliente": nome_cliente,
        "telefone": telefone_cliente,
        "endereco": endereco_cliente,
        "itens": itens,
        "total": valor_total,
        "status": "Recebido",
        "hora": datetime.now().strftime("%H:%M"),
    }

    pedidos.append(pedido)
    proximo_id += 1

#-----------------------------

    for ingrediente, qtd in necessario.items():
        estoque[ingrediente] -= qtd

#-----------------------------

    resumo = nova_tabela(expand=False, estilo_box=box.MINIMAL)
    resumo.add_column("Campo", style="dim white", width=14)
    resumo.add_column("Valor", style="bold white")
    resumo.add_row("Pedido #", str(pedido["id"]))
    resumo.add_row("Cliente", pedido["cliente"])
    resumo.add_row("Telefone", pedido["telefone"])
    resumo.add_row("Endereço", pedido["endereco"])
    resumo.add_row("Itens", ", ".join(item["nome"] for item in itens))
    resumo.add_row("Total", f"[bold yellow]R$ {valor_total:.2f}[/bold yellow]")
    resumo.add_row("Status", f"[yellow]{pedido['status']}[/yellow]")
    resumo.add_row("Hora", pedido["hora"])

    separador()
    console.print(painel(resumo, titulo="[green]✓ Pedido Registrado[/green]", borda="green"))
    pausar()

#---------------------------

def tela_consultar_pedidos():
    limpar()
    console.print(cabecalho("Consultar Pedidos"))
    separador()

    if not pedidos:
        console.print("\n  [dim white]Nenhum pedido registrado ainda.[/dim white]\n")
        pausar()
        return

    console.print("  [dim white]Filtrar por status, ou deixe em branco para todos:[/dim white]")
    for status, cor in STATUS_CORES.items():
        console.print(f"    [{cor}]{status}[/{cor}]", end="   ")
    console.print()

    filtro = Prompt.ask("\n  [white]Status[/white]", default="", show_default=False, console=console)
    pedidos_filtrados = [
        pedido
        for pedido in pedidos
        if not filtro or pedido["status"].lower() == filtro.lower()
    ]

    if not pedidos_filtrados:
        console.print(f"\n  [dim white]Nenhum pedido com status '[white]{filtro}[/white]'.[/dim white]\n")
        pausar()
        return

    tabela = nova_tabela()
    tabela.add_column("#", style="bold white", width=5, justify="right")
    tabela.add_column("Cliente", style="white", min_width=14)
    tabela.add_column("Pizzas", style="dim white", min_width=22)
    tabela.add_column("Total", style="yellow", width=10, justify="right")
    tabela.add_column("Status", width=12, justify="center")
    tabela.add_column("Hora", style="dim white", width=7, justify="center")

    for pedido in pedidos_filtrados:
        cor = STATUS_CORES.get(pedido["status"], "white")
        tabela.add_row(
            str(pedido["id"]),
            pedido["cliente"],
            ", ".join(item["nome"] for item in pedido["itens"]),
            f"R$ {pedido['total']:.2f}",
            f"[{cor}]{pedido['status']}[/{cor}]",
            pedido["hora"],
        )

    console.print(tabela)
    separador()
    console.print(f"  [dim white]{len(pedidos_filtrados)} pedido(s) encontrado(s).[/dim white]")
    pausar()

#-----------------------------------------------------------------------

def tela_atualizar_status():
    limpar()
    console.print(cabecalho("Atualizar Status"))
    separador()

    pedidos_ativos = [pedido for pedido in pedidos if pedido["status"] != "Entregue"]
    if not pedidos_ativos:
        console.print("\n  [dim white]Nenhum pedido em aberto.[/dim white]\n")
        pausar()
        return

    tabela = nova_tabela(expand=False, estilo_box=box.SIMPLE)
    tabela.add_column("#", style="bold white", width=5)
    tabela.add_column("Cliente", style="white", width=18)
    tabela.add_column("Status", width=12)

    for pedido in pedidos_ativos:
        cor = STATUS_CORES.get(pedido["status"], "white")
        tabela.add_row(str(pedido["id"]), pedido["cliente"], f"[{cor}]{pedido['status']}[/{cor}]")

    console.print(tabela)
    separador()

    id_pedido = pedir_id_pedido()
    if id_pedido is None:
        pausar()
        return

    pedido = buscar_pedido(id_pedido)
    if not pedido:
        console.print(f"\n  [bold red]✗[/bold red] Pedido #{id_pedido} não encontrado.")
        pausar()
        return

    cor_atual = STATUS_CORES[pedido["status"]]
    console.print(f"\n  Pedido [yellow]#{pedido['id']}[/yellow] — {pedido['cliente']}")
    console.print(f"  Status atual: [{cor_atual}]{pedido['status']}[/{cor_atual}]\n")

    console.print("  [dim white]Novos status disponíveis:[/dim white]")
    for numero, status in enumerate(STATUS, start=1):
        cor = STATUS_CORES[status]
        console.print(f"    [{numero}] [{cor}]{status}[/{cor}]")

    escolha = Prompt.ask("\n  [white]Novo status[/white] (número)", console=console)
    novo_status = None

    if escolha.isdigit() and 1 <= int(escolha) <= len(STATUS):
        novo_status = STATUS[int(escolha) - 1]


    if not novo_status:
        console.print("\n  [bold red]✗[/bold red] Status inválido.")
        pausar()
        return

    status_antigo = pedido["status"]

    if(
        (status_antigo == "Recebido" and novo_status == "Preparando") or
        (status_antigo == "Preparando" and novo_status == "Saiu para Entrega") or
        (status_antigo == "Saiu para Entrega" and novo_status == "Entregue")
    ):
        pedido["status"] = novo_status
        cor_nova = STATUS_CORES[novo_status]

        console.print(
            f"\n  [green]✓[/green] Pedido [yellow]#{pedido['id']}[/yellow]  "
            f"[dim white]{status_antigo}[/dim white]  →  [{cor_nova}]{novo_status}[/{cor_nova}]"
        )
        pausar()
    else:
        console.print("\n  [bold red]✗[/bold red] Transição de status inválida.")
        pausar()
        return

#-----------------------------------------------------------------------

def tela_estoque():
    limpar()
    console.print(cabecalho("Estoque de Ingredientes"))
    separador()

    tabela = nova_tabela()
    tabela.add_column("Ingrediente", style="white",      min_width=22)
    tabela.add_column("Qtd",         style="bold white", width=8,  justify="right")
    tabela.add_column("Situação",    width=10,                     justify="center")
    tabela.add_column("Visual",      min_width=22)

    for ingrediente, quantidade in sorted(estoque.items()):
        if quantidade >= 10.0:
            situacao, cor, barra_cor = "OK",      "green",  "green"
        elif quantidade >= 3.0:
            situacao, cor, barra_cor = "Atenção", "yellow", "yellow"
        else:
            situacao, cor, barra_cor = "Crítico", "red",    "red"

        blocos = max(0, min(20, int((quantidade / 20.0) * 20)))
        barra = (
            f"[{barra_cor}]{'█' * blocos}[/{barra_cor}]"
            f"[dim white]{'░' * (20 - blocos)}[/dim white]"
        )

        tabela.add_row(
            ingrediente,
            f"{quantidade:.2f}",
            f"[{cor}]{situacao}[/{cor}]",
            barra,
        )

    console.print(tabela)
    separador()

    legenda = Text()
    legenda.append("  ■ ", style="green");  legenda.append("OK (≥10)    ",     style="dim white")
    legenda.append("■ ",  style="yellow"); legenda.append("Atenção (≥5)    ", style="dim white")
    legenda.append("■ ",  style="red");    legenda.append("Crítico (<3)",     style="dim white")
    console.print(legenda)
    pausar()


def sair():
    limpar()
    console.print(
        Panel(
            Align.center(
                "[bold yellow]Obrigado! Até logo. 🍕[/bold yellow]\n"
                "[dim white]Controle de Pedidos[/dim white]"
            ),
            border_style="yellow",
            style=FUNDO,
            padding=(1, 4),
        )
    )
    console.print()


def main():

    while True:
        tela_menu()

        try:
            opcao = int(Prompt.ask(
            "  [bold yellow]›[/bold yellow] Opção",
            console=console,
            ))

            match opcao:
                case 1:
                    tela_fazer_pedido()
                case 2:
                    tela_consultar_pedidos()
                case 3:
                    tela_atualizar_status()
                case 4:
                    tela_estoque()
                case 0:
                    sair()
                    break
                case _:
                    console.print("\n  [bold red]✗[/bold red] Opção não disponivel.")
                    pausar()
        except:
            console.print("\n  [bold red]✗[/bold red] Digite o numero da tela.")
            pausar()




main()
