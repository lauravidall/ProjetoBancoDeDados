import os; os.system('cls')
import datetime
import random
import string


def retornar(txt, cont = 99999999999999, tipo = int):
    while True:
        try:
            x = tipo(input(txt))
        except(TypeError, ValueError):
            print('\nERRO!')
            continue
        if x > cont or x < 1:
            print('\nERRO!')
        else:
            break
    return x


def retornardata(txt, erro, cont = 99999999999999):
    while True:
        try:
            x = int(input(txt))
        except(TypeError, ValueError):
            print(erro)
            continue
        if x > cont or x < 1:
            print(erro)
        else:
            break
    return x


def gerarid():
    characters = string.ascii_letters + string.digits 
    while True:
        random_string = ''.join(random.choice(characters) for i in range(10))
        with open('banco.csv', 'r', encoding='utf-8') as arq:
            x = []
            linhas = arq.readlines()
            for linha in linhas:
                colunas = linha.strip().split(',')
                x.append(colunas[7])
            if random_string not in x:
                id = random_string
                break
    return id


def despesa_receita(desrec, p):
    print('-'*45)
    nome = input(f'Nome da {desrec}: ').capitalize()
    print('-'*45)
    categoria = input(f'Digite a categoria da {desrec}: ')
    print('-'*45)
    valor = retornar(f'Digite o valor da {desrec}: ', tipo=float)
    print('-'*45)
    rep = input(f'Deseja repetir essa {desrec}[S/N]: ').upper()
    
    parcelas = 0
    
    fp = 'Única'


    while rep not in 'SN':
        print('\nEscolha uma das opções mostradas')
        rep = input(f'\nDeseja repetir essa {desrec}[S/N]: ').upper()
    if rep == 'S':
        print('-'*45)
        print('Data da Repetição')
        dia = retornardata('\nDia: ', '\nERRO! Escolha um dia do mês', 31)
        mes = retornardata('\nMês: ', '\nERRO! Escolha um mês do ano', 12)
        ano = retornardata('\nAno: ', '\nERRO! Escolha um ano')
        print('-'*45)

        datastr = f'{dia}/{mes}/{ano}'
        data = datetime.datetime.strptime(datastr, '%d/%m/%Y').date()

        fp = input(f'\nÉ uma {desrec} fixa ou parcelada: ').upper()
        while fp != 'PARCELADA' and fp != 'FIXA':
            print('\nERRO! Digite uma das opçoes citadas')
            fp = input(f'\nÉ uma {desrec} fixa ou parcelada: ').upper()
        
        if fp == 'PARCELADA':
            print('-'*45)
            tipop = retornar('\nTipos:\n1 - Mensal\n2 - Quinzenal\n3 - Bimestral\n4 - Trimestral\n5 - Semestral\n6 - Anual\n\nTipo da parcela: ', 6)
            print('-'*45)
            parcelas = retornar('\nQuantidade de parcelas: ')
        else:
            print('-'*45)
            tipop = retornar('\nTipos:\n1 - Mensal\n2 - Quinzenal\n3 - Bimestral\n4 - Trimestral\n5 - Semestral\n6 - Anual\n\nTipo da despesa: ', 6)
        
    
        tipos = ['Tipos', 'Mensal', 'Quinzenal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual']
    else:
        data = 'None'

    id = gerarid()
    if p != 4:
        if desrec == 'Despesa':
            if fp != 'Única':
                with open('banco.csv', 'a', encoding='utf-8') as arq:
                    linha = f'{nome}, {categoria}, {valor*(-1)}, {fp}, {tipos[tipop]}, {data}, {parcelas}, {id}\n'
                    arq.write(linha)
                
            else:
                with open('banco.csv', 'a', encoding='utf-8') as arq:
                    linha = f'{nome}, {categoria}, {valor*(-1)}, {fp}, {0}, {data}, {parcelas}, {id}\n'
                    arq.write(linha)
        else:
            if fp != 'Única':
                with open('banco.csv', 'a', encoding='utf-8') as arq:
                    linha = f'{nome}, {categoria}, {valor}, {fp}, {tipos[tipop]}, {data}, {parcelas}, {id}\n'
                    arq.write(linha)
            
            else:
                with open('banco.csv', 'a', encoding='utf-8') as arq:
                    linha = f'{nome}, {categoria}, {valor}, {fp}, {0}, {data}, {parcelas}, {id}\n'
                    arq.write(linha)
    
    
    else:
        if desrec == 'Despesa':
            if fp != 'Única':
                linhas.insert(idx, f'{nome}, {categoria}, {valor*(-1)}, {fp}, {tipos[tipop]},{data}, {parcelas}, {id}\n')
                linhas.pop(idx+1)
            else:
                linhas.insert(idx, f'{nome}, {categoria}, {valor*(-1)}, {fp}, {0},{data}, {parcelas}, {id}\n')
                linhas.pop(idx+1)

        else:
            if fp != 'Única':
                linhas.insert(idx, f'{nome}, {categoria}, {valor}, {fp}, {tipos[tipop]},{data}, {parcelas}, {id}\n')
                linhas.pop(idx+1)
            else:
                linhas.insert(idx, f'{nome}, {categoria}, {valor}, {fp}, {0},{data}, {parcelas}, {id}\n')
                linhas.pop(idx+1)
        
        with open('banco.csv', 'w', encoding='utf-8') as arq:
            for linha in linhas:
                arq.write(linha)


hoje = datetime.datetime.today().date()

tipos = ['Tipos', 'Mensal', 'Quinzenal', 'Bimestral', 
         'Trimestral', 'Semestral', 'Anual']


print(f'{"Rastreamento de Despesas Pessoais":^45}')
print('-'*45)

opc = retornar(f'''\nOpções:
1 - Ver Saldo
2 - Registrar Despesa
3 - Registrar Receita
4 - Alterar ou deletar
{"-"*45}
Escolha uma das opçoes: ''', 4)

y= []

rd = ['Despesa', 'Receita']

if opc ==1:
    saldo = 0
    
    with open('saldo.csv', 'r', encoding='utf-8') as sld:
        linhass = sld.readlines()
        if len(linhass) > 0:
            for linhax in linhass:
                coluna = linhax.strip().split(',')
                y.append(coluna[1].strip())
    
    with open('banco.csv','r', encoding='utf-8') as arq:
        linhas = arq.readlines()
        for linha in linhas:
            colunas = linha.strip().split(',')
            if colunas[5].strip() != 'data de repetição' and colunas[5].strip() != 'None':
                strdata = f'{colunas[5].strip()[8:]}/{colunas[5].strip()[5:7]}/{colunas[5].strip()[:4]}'
                data = datetime.datetime.strptime(strdata, '%d/%m/%Y').date()
                diferenca = hoje - data
                meses = diferenca.days//30
                c = 0
                if data < hoje:
                    
                    def parcelas(n):
                        c = 0
                        with open('saldo.csv', 'a', encoding='utf-8') as sld:
                            if colunas[7].strip() not in y:
                                if colunas[3].strip() != 'PARCELADA':
                                    linhasld = f'{colunas[2]}, {colunas[7].strip()}\n'.lstrip()
                                    while c <= meses:
                                        sld.write(linhasld)
                                        c+=n
                                else:
                                    linhasld = f'{float(colunas[2].strip())/float(colunas[6].strip()):.2f}, {colunas[7].strip()}\n'.lstrip()
                                    qtd_parcelas = float(colunas[6].strip())
                                    while qtd_parcelas > 0 and c <=meses:
                                        sld.write(linhasld)
                                        c+=n
                                        qtd_parcelas -=1
                    
                    
                    
                    if colunas[4].strip() == 'Mensal':
                        parcelas(1)
                            
                                
                    elif colunas[4].strip() == 'Bimestral':
                        parcelas(2)
                                

                    elif colunas[4].strip() == 'Trimestral':
                        parcelas(3)


                    elif colunas[4].strip() == 'Semestral': 
                        parcelas(6)


                    elif colunas[4].strip() == 'Anual':
                        parcelas(12)


                    elif colunas[4].strip() == 'Quinzenal':
                        with open('saldo.csv', 'a', encoding='utf-8') as sld:
                            if colunas[7].strip() not in y:
                                if colunas[3].strip() != 'PARCELADA':
                                    linhasld = f'{colunas[2]}, {colunas[7].strip()}\n'.lstrip()
                                    while c <= diferenca.days:
                                        sld.write(linhasld)
                                        c+=15
                                else:
                                    linhasld = f'{float(colunas[2].strip())/float(colunas[6].strip()):.2f}, {colunas[7].strip()}\n'.lstrip()
                                    qtd_parcelas = float(colunas[6].strip())
                                    while qtd_parcelas >0 and c <=diferenca.days:
                                        sld.write(linhasld)
                                        c+=15
                                        qtd_parcelas -=1

                        

            if colunas[5].strip() == 'None' and colunas[7].strip() not in y:
                with open('saldo.csv', 'a', encoding='utf-8') as sld:
                    sld.write(f'{colunas[2].strip()}, {colunas[7].strip()}')   
                    

    with open('saldo.csv', 'r', encoding='utf-8') as sld:
        linhas = sld.readlines()
        for linha in linhas:
            colunas = linha.strip().split(',')
            saldo += float(colunas[0].strip())
    
    print('-'*45)
    print(f'Saldo(R$): {saldo:.2f}'.replace('.', ','))




elif opc == 2:
    despesa_receita(rd[0], 2)
    


elif opc ==3:
    despesa_receita(rd[1], 3)


elif opc == 4:
    print('-'*45) 
    ud = retornar('\nOpções:\n\n[1] Alterar\n[2] Deletar\n\nAlterar ou remover despesa/receita: ', cont=2)
    print('-'*45)
    cont = 0
    with open('banco.csv', 'r', encoding='utf-8') as arq:
        linhas  = arq.readlines()
        for linha in linhas:
            colunas = linha.strip().split(',')
            for c in range(7):
                if c == 0 and cont!=0:
                    print(f'{cont} - {colunas[c]:<20}', end=' ')
                else:
                    print(f'{colunas[c]:<23}', end=' ')
            cont+=1
            print()

    
    if ud == 2:
        z = []
        idx  = retornar('\nQual linha você deseja remover: ', cont=len(linhas)-1)
        z.append(linhas[idx].strip().split(',')[7].strip())
        linhas.pop(idx)
        with open('banco.csv', 'w', encoding='utf-8') as arq:
            for linha in linhas:
                arq.write(linha)
    

        
       
    else:
        idx = retornar('\nQUal linha você deseja alterar: ', cont=len(linhas)-1)
        print('\nNovos valores')
        
        dr = input('\nAdicionar Despesa ou Receita: ').capitalize()
        despesa_receita(dr, 4)