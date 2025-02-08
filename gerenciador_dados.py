from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console =  Console()

def add_alunos(lista): #se retorna True exibir ALUNO MATRICULADO COM SUCESSO!
    try:
        notas = []
        nome = input("Nome: ")
        if not nome.replace(" ", "").isalpha():
            print("Digite um nome válido!")
            return
        if len(lista) > 9:
            matricula = '2025' + str(len(lista)+1)
        else:
            matricula = '20250' + str(len(lista)+1)
        data = input("Data de nascimento (XX/XX/XXXX): ")
        data = datetime.strptime(data, "%d/%m/%Y")
        data = '{}/{}/{}'.format(data.day, data.month, data.year) #verificar data de nasc
        for i in range(3):
            nota = float(input(f"Nota {i+1}: ")) #verificar se a nota <= 10
            if nota < 0:
                print("Não existe nota negativa!")
                return
            notas.append(nota)
        total_faltas =  int(input("Total de faltas: "))
        situacao_matricula = 'ativo'
        if total_faltas < 0:
            print("Digite um número inteiro positivo!")
            return    
        aluno = {'nome': nome,
                 'matricula': matricula,
                 'data-nasc': data,
                 'notas': notas,
                 'total-faltas': total_faltas,
                 'situacao-matricula': situacao_matricula
                 }
        lista.append(aluno)
        return True
    except ValueError:
        print("Digite um tipo válido!")
        return
    
def listar_alunos(lista): #terminar
    if len(lista) > 0:
        for aluno in lista:
            if aluno['situacao-matricula'] == 'ativa':
                painel_aluno = Panel(f"Matricula: {aluno['matricula']}\nData de nascimento: {aluno['data-nasc']}\nTotal de faltas: {aluno['total-faltas']}", title=aluno['nome']) #usar o panel? talvez
                console.print(painel_aluno)
        return True
    else:
        return False
    
def remover_aluno(lista):
    listar_alunos(lista)
    matricula = input("Matricula: ")
    if matricula.isdigit:
        for aluno in lista:
            if aluno['matricula'] == matricula:
                aluno['nome'] = ''
                aluno['data-nasc'] = ''
                aluno['notas'] = []
                aluno['total-faltas'] = 0
                aluno['situacao-matricula'] = 'excluida'
                return True
        return False

    
