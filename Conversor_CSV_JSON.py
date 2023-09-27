import csv
import json
chaves = ['Nome','Idade','Cidade','Email','CPF']
dicionario_itens = copia = {}
lista_itens = []
try:
    with open('dados.csv', mode ='r', encoding='utf-8') as arquivo:
        print(f'arquivo {arquivo.name} encontrado...')
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv) # aqui ele não pega o cabeçalho
        items = list(leitor_csv) 
        print(f'Processando {len(items)} registros...')
        # o objetivo é literalmente criar uma lista de dicionários  
        for linhas in items: 
            for c in range(0, len(linhas)):
                dicionario_itens[chaves[c]] = linhas[c]
            # aqui eu criei essa cópia do dicionário
            # isso ocorre pois, se eu alterar um valor do dicionário, mesmo já dentro da lista, ele altera todos os valores
            copia = dict(dicionario_itens)
            lista_itens.append(copia)    
except FileNotFoundError:
    print('Arquivo não encontrado')
with open('dados.json', mode ='w', encoding='utf-8') as arquivo_json: # aqui, caso o arquivo não exista, ele cria
    print(f'arquivo {arquivo_json.name} gerado com sucesso!')
    json.dump(lista_itens, arquivo_json, indent=2, ensure_ascii=False)