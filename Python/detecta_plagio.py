import re


def main():
    assinaturaReferencia = le_assinatura()
    textos = le_textos()
    provavelCopia = avalia_textos(textos, assinaturaReferencia)
    print ("O autor do texto %d está infectado com COH-PIAH" %(provavelCopia))
    teste_calcula_assinatura()
    
    
def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser 
    # comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    # A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
    nas assinaturas.'''
    diferencas = []
    similaridade = 0
    diferencaTotal = 0
    for i in range(len(as_a)):
        diferencas.append(abs(as_b[i] - as_a[i]))        
    
    for diferenca in diferencas:
        diferencaTotal += diferenca
        
    similaridade = diferencaTotal / 6
    
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_de_palavras = separa_palavras(texto)
    char = ":,\';.\"![)(]?"
    for item in lista_de_palavras:
        for i in range(0,len(char)):
            item = item.replace(char[i],"")

    n_total_palavras = len(lista_de_palavras)

    tamanho_palavras = 0
    for i in range (n_total_palavras):
        #soma do tamanho de todas as palavras
        tamanho_palavras += len(lista_de_palavras[i])
    
    tamanho_medio_palavra = tamanho_palavras/n_total_palavras
    
    type_token = n_palavras_diferentes(texto)/n_total_palavras
    
    hapax_legomana = n_palavras_unicas(texto)/n_total_palavras

    n_total_sentencas = len(separa_sentencas(texto))

    n_total_frases = len(separa_frases(texto))
    
    tamanho_medio_sentenca = tamanho_palavras/n_total_sentencas
    
    complexidade_sentenca = n_total_frases/n_total_sentencas
    
    tamanho_medio_frase = tamanho_palavras/n_total_frases

    assinatura = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e
    deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    
    comparacoes = []
    for assinatura in assinaturas:
        comparacoes.append(compara_assinatura(ass_cp, assinatura))

    maiorSimilaridade = min(comparacoes)
    if maiorSimilaridade in comparacoes:
        indexador = comparacoes.index(maiorSimilaridade)

    provavelCopia = indexador + 1

    return provavelCopia

def teste_calcula_assinatura():
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    calculado = calcula_assinatura(texto)
    print(calculado)
    esperado = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
    
    print(esperado)
    #if esperado == calculado:
    #    print("Passou no teste")
    #else:
    #    print("Deu Ruim")    

main()