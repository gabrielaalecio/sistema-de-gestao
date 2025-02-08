from docx import Document
from openpyxl import Workbook

def gerar_rel(lista, op):
    if op == 1:
        matricula = input("Matricula: ")
        for aluno in lista:
            if matricula == aluno['matricula']:
                media = sum(aluno['notas'])/3
                situacao = 'reprovado'
                if media >= 7 and aluno['total-faltas'] < 50:
                    situacao = 'aprovado'
                doc = Document()
                doc.add_paragraph(f"Nome: {aluno['nome']}")
                doc.add_paragraph(f"Matrícula: {matricula}")
                doc.add_paragraph(f"Data de Nascimento: {aluno['data-nasc']}")
                doc.add_paragraph(f"Média: {media}")
                doc.add_paragraph(f"Aluno {situacao}!")
                doc.save(f"relatorio-{aluno['nome']}.docx")
                return True
            else:
                return False
    elif op == 2:
        for aluno in lista:
            media = sum(aluno['notas'])/3
            situacao = 'reprovado'
            if media >= 7 and aluno['total-faltas'] < 50:
                situacao = 'aprovado'
            doc = Document()
            doc.add_heading(f"Nome: {aluno['nome']}")
            doc.add_paragraph(f"Matrícula: {matricula}")
            doc.add_paragraph(f"Data de Nascimento: {aluno['data-nasc']}")
            doc.add_paragraph(f"Média: {media}")
            doc.add_paragraph(f"Aluno {situacao}!\n")
        doc.save("relatorio-geral.docx")

def gerar_planilha(lista):
    wb = Workbook()
    ws = wb.active
    ws.title = "Planilha Alunos"
    ws.append(['Nome', 'Matricula', 'Data de nascimento', 
               'Notas', 'Média', 'Total de faltas', 
               'Status de aprovação'])
    media = sum(aluno['notas'])/3
    situacao = 'reprovado'
    if media >= 7 and aluno['total-faltas'] < 50:
        situacao = 'aprovado'
    for aluno in lista:
        ws.append([aluno['nome'], aluno['matricula'], 
                   aluno['data-nasc'], aluno['notas'],
                   media, aluno['total-faltas'],
                   situacao])
    wb.save('planilha-alunos.xlsx')