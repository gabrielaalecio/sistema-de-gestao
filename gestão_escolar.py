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
        os.system("cls")
        menu = Panel("1. Adicionar Aluno.\n2. Remover Aluno.\n3. Exibir Alunos.\n4. Gerar Relatórios.\n5. Gerar Planilha.\n6. Sair.", title="MENU", style='bold blue')
        console.print(menu)
        try:
            op = int(input("Digite a opção desejada: "))
            os.system("cls")
            match op:
                case 1: #adicionar aluno
                    if add_alunos(lista_alunos):
                        console.print("[bold green]Aluno adicionado com sucesso![/bold green]")
                        sleep(2)
                case 2: #remover aluno
                    if len(lista_alunos) > 0:
                        if remover_aluno(lista_alunos):
                            console.print("[bold green]Aluno removido com sucesso![/bold green]")
                        else:
                            console.print("[bold red]A matricula não foi encontrada![/bold red]")
                    else:
                        console.print("[bold red]Não tem alunos cadastrados![/bold red]")
                case 3: #listar alunos
                    if listar_alunos(lista_alunos):
                        console.input("Digite qualquer tecla para voltar ao menu: ")
                    else:
                        console.print("[bold red]Não tem alunos cadastrados![/bold red]")
                case 4: #gerar relatorio
                    if len(lista_alunos) > 0:
                        op_relatorio = Panel("1. Gerar relatório individual.\n2. Gerar relatório coletivo.\n3. Sair.", title="MENU", style='bold blue')
                        console.print(op_relatorio)
                        op_rel = int(console.input("Digite sua opção: "))
                        if 1 <= op_rel <= 2:
                            if gerar_rel(lista_alunos, op_rel):
                                console.print("[bold green]Relatório gerado com sucesso![/bold green]")
                            else:
                                console.print("[bold red]Matricula não encontrada![/bold red]") #não gerado!
                        else:
                            console.print("Opção errada!")
                    else:
                        console.print("[bold red]Não tem alunos cadastrados![/bold red]")
                case 5:  #gerar planilha
                    if len(lista_alunos) > 0:
                        if gerar_planilha(lista_alunos):
                            console.print("[bold green]Relatório gerado com sucesso![/bold green]")
                        else:
                            console.print("[bold red]Matricula não encontrada![/bold red]")
                    else:
                        console.print("[bold red]Não tem alunos cadastrados![/bold red]")
                case 6: #sair
                    with console.status("[bold green]Saindo...[/bold green]") as status:
                        sleep(3)
                    exit()
                case _:
                    console.print("[bold red]Digite uma opção válida![/bold red]")
                    sleep(3)
        except ValueError:
            console.print("[bold red]Tipo da opção inválida![/bold red]")
        salvar_arquivo(lista_alunos)
        sleep(3)

main()