import json

def abrir_arquivo():
    try:
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []
    
def salvar_arquivo(lista):
    with open("dados.json", "w") as arquivo:
            json.dump(lista, arquivo)
