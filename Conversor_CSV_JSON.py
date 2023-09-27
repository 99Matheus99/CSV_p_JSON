import csv
chaves = ['Nome','Idade','Cidade','Email','CPF']
dicionario_itens = {}
lista_itens = []
with open('dados.csv', mode ='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv) # aqui ele não pega o cabeçalho
    items = list(leitor_csv) 
    #o objetivo é literalmente criar uma lista de dicionários  
    for linhas in items: 
        for c in range(0, len(linhas)):
            dicionario_itens[chaves[c]] = linhas[c]
    lista_itens.append(dicionario_itens)   
print(lista_itens)