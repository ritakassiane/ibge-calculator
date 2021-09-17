###############################################################################################################################################################
# Autor: Rita Kassiane Santos dos Santos                                                                                                                                        #
# Componente Curricular: Algoritmos I                                                                                                                         #
# Concluido em: 15/08/2019                                                                                                                                    #
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor,                   #
# tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de outra autoria que                  #
# não a minha está destacado com uma citação para o autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.#
###############################################################################################################################################################
import pandas as pd
import os
def menuDesign(x): #Essa função existe para deixar o programa visualmente mais agradável
    print("-------------------------------")
    print(x)
    print("-------------------------------")





def abreArquivo(file): #essa função irá abrir um arquivo txt e criar uma lista com ele. Ou seja, cada linha do arquivo vira uma linha
    arquivo = open(file, 'r')
    lista = arquivo.readlines()
    return lista
def fazMatrizCompleta(lista): # faz uma lista, outras listas dentro. Tirando o "\n" e o ";"
    listaGerada = []
    for i in lista:
        i = i.strip('\n')
        i = i.split(';')
        listaGerada += [i]
    return listaGerada
def matrizPandas(lista): # essa funcao cria uma matriz mais organizada
    df = pd.DataFrame(lista)
    return df
def moldaLista(listaTotal, numColuna): # essa função pega uma lista e transforma ela em outra lista, apenas com os elementos desejados. [forma uma matriz apenas com a coluna desejada]
    novaLista = [] #lista com apenas a 'coluna' desejada
    for i in listaTotal:
        i = i.strip('\n')
        i = i.split(';')
        novaLista += [i[numColuna]]
    return novaLista
#Usa-se essa função com listas criadas e não tratadas. Ou seja, listas que "acabaram de sair da função 'AbreArquivo'#
def moldaListaPronta(listaTotal,numColuna): #essa função faz essencialmente o mesmo que a de cima, o que muda é que aqui a lista ja vai ta tratada
    novaLista = []
    for i in listaTotal:
        novaLista += [i[numColuna]]
    return novaLista
def VerificaFluxo (x): #Essa função verifica o fluxo de respostas.
    if (str(x[3]) == '1'):
        if ((x[4]) != '-') and ((x[5]) != '-'):
            if (x[6]) == '0':
                if (x[7]) == '1':
                    if ((x[8]) != '-') and ((x[9]) != '-') and ((x[10]) != '-'):
                        if (x[11]) == '1':
                            if (x[12]) != '-':
                                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif (x[11]) == '2' or '3':
                            if (x[12]) == '-':
                                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                elif (x[7]) == '2':
                    if (x[8]) == '-' and ((x[9]) != '-') and ((x[10]) != '-'):
                        if (x[11]) == '1':
                            if (x[12]) != '-':
                                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif (x[11]) == '2' or '3':
                            if (x[12]) == '-':
                                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                        return True
                                    else:
                                        return False

                    else:
                        return False
            elif (x[6]) != ('0'):
                if (x[7]) == '-':
                    if ((x[8]) != '-') and ((x[9]) != '-') and ((x[10]) != '-'):
                        if (x[11]) == '1':
                            if (x[12]) != '-':
                                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif (x[11]) == '2' or (x[11]) == '3':
                            if (x[12] == '-') and ((x[13]) != '-') and ((x[14]) != '-') and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                                if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                    return True


                    else:
                        return False
                else:
                    return False
            else:
                return False
    elif (x[3]) == '5':
        if (x[4]) != '-':
            if (x[5] and x[6] and x[7] and x[8] and x[9] and x[10] and x[11] and x[12]) == '-':
                if (x[13]) != '-' and (x[14]) != '-' and (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                    if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif x[3] == '6':
        if (x[4]) != '-':
            if (x[5] and x[6] and x[7] and x[8] and x[9] and x[10] and x[11] and x[12]) == '-':
                if x[13] != '-':
                    if x[14] == '-':
                        if (x[15]) != '-' and (x[16]) != '-' and (x[17]) != '-':
                            if (x[18]) != '-' and (x[19]) != '-' and (x[20]) != '-':
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def verificandoTecnicoRegiao(colunaDaMatricula, cadastroTec, cadastroIBGE, matrizRespostas): #essa função verifica o tecnico e a região, e posteriormente o fluxo de respostas
    matrizVerificada = []
    matrizTecN = []
    matrizRegN = []
    matrizFN = []
    for i in range (len(colunaDaMatricula)):
        salvarposicao = i
        i = colunaDaMatricula[i]
        verificaTecnico = str(i) in str(cadastroTec) #cadastro é a coluna da matriz que tem apenas o numero de matricula dos tecnicos cadastrados
        if verificaTecnico == True:
            verificaRegiao = ((matrizRespostas[salvarposicao])[1]) in cadastroIBGE
            if verificaRegiao == True:
                vFluxo = VerificaFluxo(matrizRespostas[salvarposicao])
                if vFluxo == True:
                    matrizVerificada += [matrizRespostas[salvarposicao]]
                else:
                    print(" ")
                    #matrizFN += [matrizRespostas[salvarposicao]]
                    #print(pd.DataFrame(matrizFN))

            else:
                print(" ")
                #matrizRegN += [matrizRespostas[salvarposicao]]
                #print(pd.DataFrame(matrizRegN))

        else:
            print(" ")
            #matrizTecN += [matrizRespostas[salvarposicao]]
            #print(pd.DataFrame(matrizTecN))
    return matrizVerificada
listaRegioes = fazMatrizCompleta(abreArquivo('regioes.txt')) #
def estatistica1(matriz): #calculo da quantidade de domicilios, a qual é exatamente a quantidada de elementos da lista verificada
    QntdDeDomicilios = (len(matriz))
    return QntdDeDomicilios
def estatistica2(matrizGeral): #calculo da estatistica 2 que pede a quantidade de domiclios pagos, pagando e alugados
    pagos = 0
    pagando = 0
    alugados = 0
    for l in range(len(matrizGeral)):
        if matrizGeral[l][5] == '1':
            pagos += 1
        elif matrizGeral[l][5] == '2':
            pagando += 1
        elif matrizGeral[l][5] == '3':
            alugados += 1

    resultado2 = ('''                   
                                            -----------------------------
                                            |   PAGOS  |      {}        |            
                                            |  PAGANDO |      {}        |            
                                            |  ALUGADOS|      {}        |            
                                            -----------------------------  

        '''.format(pagos, pagando, alugados))
    return resultado2
def IBGEtoNAME(elemento,regioes):  # funcao que pega uma lista qualquer(so com o codigo ibge), muda o codigo ibge para nome
    nomeDaCidade = ''
    for i in range(len(regioes)):
        i = regioes[i]
        if i[2] == elemento:
            nomeDaCidade = i[1]
    return nomeDaCidade
# Essa função etorna uma lista que tem dentro outras duas listas. Onde a lista 1 é o nome das cidades e a lista dois a quantidade de domicilios com banheiro
def estatistica3(listaCodIBGE,
                 listaPesquisa):  # listaCodIBGE é uma lista com apenas o cidigoIBGE das cidades validadas #listaPesquisa é a lista que tem as respostas validadas da pesquisa
    contadorCom = [0]
    contadorSem = [0]

    for i in range(len(listaCodIBGE)):
        contadorCom += [0]
        contadorSem += [0]
    listaTotal = [listaCodIBGE, contadorCom, contadorSem]
    for j in range(len(listaPesquisa)):
        j = listaPesquisa[j]
        if j[6] != '-' and j[6] == '0':
            for k in range(len(listaTotal[0])):
                s = k
                k = listaTotal[0][k]
                if k == j[1]:
                    listaTotal[2][s] += 1
                    listaTotal[0][s] = IBGEtoNAME(listaTotal[0][s], listaRegioes)
        elif j[6] != '-' and j[6] != '0':
            for k in range(len(listaTotal[0])):
                s = k
                k = listaTotal[0][k]
                if k == j[1]:
                    listaTotal[1][s] += 1
                    listaTotal[0][s] = IBGEtoNAME(listaTotal[0][s], listaRegioes)
        elif j[6] == '-':
            for k in range(len(listaTotal[0])):
                s = k
                k = listaTotal[0][k]
                if k == j[1]:
                    listaTotal[1][s] += 0
                    listaTotal[0][s] = IBGEtoNAME(listaTotal[0][s], listaRegioes)
    listaTotal[0][0] = 'Cidades:'
    listaTotal[1][0] = 'Dom. c/ Banheiro:'
    listaTotal[2][0] = 'Dom. s/ banheiro:'
    return listaTotal
def estatistitca4(codIBGE):
    c = 0  # variavel que guardará o numero do tipo de abastecimento
    #contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # posicao 1 equivale a primeira forma de abastecimento
    listaCont = [codIBGE[1:], 0]
    k = [0]

    for i in range(len(codIBGE[1:])):
        k += [0]
    listaCont = [codIBGE,k]
    return listaCont
def estatistica5(listaCodIBGE, listaPesquisa):

    semEnergia = [0]
    domicilios = [0]
    for j in range(len(listaCodIBGE)):
        semEnergia += [0]
        domicilios += [0]
    listaTotal = [listaCodIBGE, semEnergia, domicilios]
    for i in range(len(listaPesquisa)):
        if listaPesquisa[i][11] == '3':
            listaTotal[1][i] += 1
            listaTotal[2][i] += 1
            listaTotal[0][i] = IBGEtoNAME(listaTotal[0][i], listaRegioes)
        elif listaPesquisa[i][11] == '-' or listaPesquisa[i][11] != '3':
            listaTotal[1][i] += 0
            listaTotal[2][i] += 1
            listaTotal[0][i] = IBGEtoNAME(listaTotal[0][i], listaRegioes)
    listaTotal = [listaCodIBGE, semEnergia, domicilios]

    for k in range(len(listaTotal[1])):
        p = semEnergia[k]
        q = domicilios[k]
        if q != 0:
            s = (p*100)/q
            semEnergia[k] = [s]
    listaTotal[0][0] = 'Cidades:'
    listaTotal[1][0] = 'Porcentagem:'
    listaTotal[2][0] = 'Qntd. de Domicílios:'

    return listaTotal
def estatistica6(matrizGeral):
    branco = 0
    preto = 0
    amarelo = 0
    parda = 0
    indigena = 0
    for i in range(len(matrizGeral)):
        if matrizGeral[i][18] == '1':
            branco += 1
        elif matrizGeral[i][18] == '2':
            preto += 1
        elif matrizGeral[i][18] == '3':
            amarelo += 1
        elif matrizGeral[i][18] == '4':
            parda += 1
        elif matrizGeral[i][18] == '5':
            indigena += 1
    brancoPorcent = (100*branco)/len(matrizGeral)
    pretoPorcent = (100*preto)/len(matrizGeral)
    amareloPorcent = (100*amarelo)/len(matrizGeral)
    pardaPorcent = (100*parda)/len(matrizGeral)
    indigenaPorcent = (100*indigena)/len(matrizGeral)
    porcentagem = ("""                       
                                              COR/RAÇA   |   PORCENTAGEM
                                            -----------------------------
                                              BRANCOS    |      {:.2f}%                 
                                              PRETOS     |      {:.2f}%                 
                                              AMARELO    |      {:.2f}%     
                                               PARDA     |      {:.2f}%     
                                              INDIGENA   |      {:.2f}%        
                                            -----------------------------           


    """.format(brancoPorcent, pretoPorcent, amareloPorcent, pardaPorcent, indigenaPorcent))
    return porcentagem
def estatistica7(listaPesquisa):
    norte = 0
    sul = 0
    sudeste = 0
    nordeste = 0
    centroeste = 0
    listaReg = [0,0,0,0,0]
    contador = 0
    for i in range(len(listaPesquisa)):
        i = listaPesquisa[i]
        if i[1][0] == '1':
            norte += 1

        elif i[1][0] == '2':
            nordeste += 1

        elif i[1][0] == '3':
            sudeste += 1

        elif i[1][0] == '4':
            sul += 1

        elif i[1][0] == '5':
            centroeste += 1

    listaReg[0] = norte
    listaReg[1] = nordeste
    listaReg[2] = sudeste
    listaReg[3] = centroeste
    listaReg[4] = sul


    for j in range(len(listaReg)):
        if j == 0:
            contador = 0
            if listaReg[j] > contador:
                contador = j
        else:
            if listaReg[j] > contador:
                contador = j
    #print(contador)
    if contador == 0:
        print('+ A região com maior número de municípios pesquisados é Norte')
    elif contador == 1:
       print('+ A região com maior número de municípios pesquisados é Nordeste')
    elif contador == 2:
        print('+ A região com maior número de municípios pesquisados é Sudeste')
    elif contador == 3:
        print('+ A região com maior número de municípios pesquisados é Centro-oeste')
    elif contador == 4:
        print('+ A região com maior número de municípios pesquisados é Sul')

#abrindo arquivos e fazendo matriz como eles (lista dentro de lista)
print("CARREGANDO....")
print(" ")
pesquisa = fazMatrizCompleta(abreArquivo('Pesquisa.txt'))
cadastroTec = fazMatrizCompleta(abreArquivo('tecnicosIBGE.txt'))

apenasTecnicos = moldaLista(abreArquivo('Pesquisa.txt'),0) #fazendo uma lista apenas com a matricula dos tecnicos do arquivo pesquisa
listaTec = moldaLista(abreArquivo('tecnicosIBGE.txt'),0) # fazendo uma lista apenas com a matricula dos tecnicos do arquivo tecnicosIBGE
listaCodIBGE = moldaLista(abreArquivo('regioes.txt'),2)

#Fazendo verificação do tecnicos, região e fluxo de respostas, respectivamente:

listaValidada = verificandoTecnicoRegiao(apenasTecnicos,listaTec,listaCodIBGE,pesquisa)

#MENU
def menu(x):  # Da ao usuário a opção de escolher o modo de exibição
    if x == '1':
        print('+ O número de domicílios utilizados para a coleta: {}'.format(estatistica1(listaValidada)))
        print(" ")
        print(" ")
        print("""
            + Número de domicílios particulares que ja estão pagos, quantos estão pagando e alugados:

             {}""".format(estatistica2(listaValidada)))
        print(" ")
        print(" ")
        print(matrizPandas(estatistica3(moldaListaPronta(listaValidada, 1), listaValidada)))
        print(" ")
        print(" ")
        print(matrizPandas(estatistica5(moldaListaPronta(listaValidada, 1), listaValidada)))
        print(" ")
        print(" ")
        print(matrizPandas(estatistitca4(moldaListaPronta(listaValidada, 1))))
        print("""
            + Percentual de moradores que participaram da entrevista por cor ou raça:
            {}""".format(estatistica6(listaValidada)))
        print(" ")
        print(" ")
        print(estatistica7(listaValidada))

    elif x == '2':
        n = '0'
        while n == '0':
            print('+ O número de domicílios utilizados para a coleta: {}'.format(estatistica1(listaValidada)))
            print(" ")
            print(" ")
            print("""
                + Número de domicílios particulares que ja estão pagos, quantos estão pagando e alugados:

                 {}""".format(estatistica2(listaValidada)))
            n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
            if n == '0':
                print(" ")
                print(" ")
                print(matrizPandas(estatistica3(moldaListaPronta(listaValidada, 1), listaValidada)))
                print(" ")
                print(" ")
                n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
                if n == '0':
                    print(matrizPandas(estatistica5(moldaListaPronta(listaValidada, 1), listaValidada)))
                    print(" ")
                    print(" ")
                    print("""
                        + Percentual de moradores que participaram da entrevista por cor ou raça:
                        {}""".format(estatistica6(listaValidada)))
                    n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
                    if n == '0':
                        print(" ")
                        print(" ")
                        print(estatistica7(listaValidada))
## FUNCOES DE EXIBIÇÃO AO USUÁRIO
def inicio():
    print("""
      1. Exibir todas as estatísticas de uma só vez
      2. Exibir estatísticas uma por vez
    """)



def exibicao(x):  # Da ao usuário a opção de escolher o modo de exibição
    if x == '1':

        print('+ O número de domicílios utilizados para a coleta: {}'.format(estatistica1(listaValidada)))
        print(" ")
        print(" ")
        print("""
            + Número de domicílios particulares que ja estão pagos, quantos estão pagando e alugados:

             {}""".format(estatistica2(listaValidada)))
        print(" ")
        print(" ")
        print(matrizPandas(estatistica3(moldaListaPronta(listaValidada, 1), listaValidada)))
        print(" ")
        print(" ")
        print(matrizPandas(estatistica5(moldaListaPronta(listaValidada, 1), listaValidada)))
        print(" ")
        print(" ")
        
        print("""
            + Percentual de moradores que participaram da entrevista por cor ou raça:
            {}""".format(estatistica6(listaValidada)))
        print(" ")
        print(" ")
        print(estatistica7(listaValidada))

    elif x == '2':
        n = '0'
        while n == '0':

            print('+ O número de domicílios utilizados para a coleta: {}'.format(estatistica1(listaValidada)))
            print(" ")
            print(" ")
            print("""
                + Número de domicílios particulares que ja estão pagos, quantos estão pagando e alugados:

                 {}""".format(estatistica2(listaValidada)))
            n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
            if n == '0':
                print(" ")
                print(" ")
                print(matrizPandas(estatistica3(moldaListaPronta(listaValidada, 1), listaValidada)))
                print(" ")
                print(" ")
                n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
                if n == '0':
                    print(matrizPandas(estatistica5(moldaListaPronta(listaValidada, 1), listaValidada)))
                    print(" ")
                    print(" ")
                    print("""
                        + Percentual de moradores que participaram da entrevista por cor ou raça:
                        {}""".format(estatistica6(listaValidada)))
                    n = input('Digite 0 para passar para a proxima estatística e 1 para sair:')
                    if n == '0':
                        print(" ")
                        print(" ")
                        print(estatistica7(listaValidada))

y = """
################################################           C A L C U L A D O R A  E S T A T I S T I C A      ######################################################## 
                                                            Universidade Estadual de Feira de Santana
                                                                 RITA KASSIANE SANTOS DOS SANTOS 
 """
print(menu(y))
inicio()
x = input('Digite o número correspondente ao modo de exibição:')
print(exibicao(x))
os.system('pause')

