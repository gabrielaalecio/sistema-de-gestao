"""1. Gerenciamento de Alunos
    ○ Adicionar alunos ao sistema com os seguintes dados:
        ■ Nome completo
        ■ Matrícula (única para cada aluno)
        ■ Data de nascimento
        ■ Notas em no mínimo 3 disciplinas (de 0 a 10)
        ■ Total de faltas
    ○ Remover alunos do sistema com base na matrícula.
    ○ Listar todos os alunos cadastrados, mostrando nome, matrícula, notas e total de
    faltas"""
from gerenciador_arquivos import *
from gerenciador_dados import *
from gerador_relatorios import *
from rich.console import Console
from rich.panel import Panel
import os
from time import sleep

console =  Console()

def main():
    lista_alunos = abrir_arquivo()
    while True:
        menu = Panel("1. Adicionar Aluno.\n2. Remover Aluno.\n3. Exibir Alunos.\n4. Gerar Relatório Individual.", title="MENU", style='bold blue')
        console.print(menu)
        try:
            op =  int(input("Digite a opção desejada: "))
            os.system("cls")
            match op:
                case 1:
                    if add_alunos(lista_alunos):
                        console.print("[bold green]Aluno adicionado com sucesso![/bold green]")
                        sleep(2)
                case 2:
                    if remover_aluno(lista_alunos):
                        console.print("[bold green]Aluno removido com sucesso![/bold green]")
                        sleep(2)
                case 3:
                    listar_alunos(lista_alunos)
                    console.input()
                case 8:
                    with console.status("[bold green]Saindo...[/bold green]") as status:
                        sleep(3)
                    exit()
                case 4:
                    op_relatorio = Panel("1. Gerar relatório individual.\n2. Gerar relatório coletivo.\n3. Sair.", title="MENU", style='bold blue')
                    console.print(op_relatorio)
                    op_rel = console.input("Digite sua opção: ")
                    if 1 <= op_rel <= 2:
                        if gerar_rel(lista_alunos, op_rel):
                            console.print("[bold green]Relatório gerado com sucesso![/bold green]")
                        else:
                            console.print("[bold green]Relatório gerado com sucesso![/bold green]") #não gerado!
                    else:
                        console.print("")
                case _:
                    console.print("Digite uma opção válida!")
        except ValueError:
            print("Tipo da opção inválida!")
        salvar_arquivo(lista_alunos)
        os.system("cls")

main()