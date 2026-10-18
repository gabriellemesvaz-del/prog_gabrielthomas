"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    if len(lista) == 0:
        return 0

    total = 0
    for numero in lista:
        total += numero

    return total / len(lista)
  



def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    if not lista:
        return []

    maior = max(lista)
    encontrado = False
    nova_lista = []
    for elemento in lista:
        if elemento == maior and not encontrado:
            encontrado = True
            continue
        nova_lista.append(elemento)
    return nova_lista

def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    if not lista:
        return []

    nova_lista = [lista[0]]
    for i in range(1, len(lista)):
        nova_lista.append(nova_lista[-1] + lista[i])
    return nova_lista


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    resultado = []

    for sublista in lista_de_listas:
        for elemento in sublista:
            resultado.append(elemento)

    return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i
    return -1


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return contador


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    for i, elemento in enumerate(lista):
        if elemento > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    esquerda = 0
    direita = len(lista) - 1
    resultado = -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            resultado = meio
            direita = meio - 1  # Continua procurando à esquerda
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return resultado


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    soma = 0
    operacoes = 0

    for elemento in lista:
        operacoes += 1

        if elemento % 2 == 0:
            soma += elemento

    return soma, operacoes

def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    maior = lista[0]
    comparacoes = 0

    for elemento in lista[1:]:
        comparacoes += 1
        if elemento > maior:
            maior = elemento

    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    comparacoes = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes

    return False, comparacoes


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    comparacoes = 0

    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes

    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]

        esquerda += 1
        direita -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        if lista[esquerda] != lista[direita]:
            return False
        esquerda += 1
        direita -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]
        if soma == alvo:
            return (esquerda, direita)
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1

    return (-1, -1)


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    if len(lista) < k:
        return 0

    max_soma = sum(lista[:k])
    soma = max_soma

    for i in range(1, len(lista) - k + 1):
        soma = soma - lista[i - 1] + lista[i + k - 1]
        if soma > max_soma:
            max_soma = soma

    return max_soma


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pilha = []
    topo = 0

    for caractere in texto:
        if caractere == '(' or caractere == '[':
            pilha.append(caractere)
            topo += 1

        elif caractere == ')' or caractere == ']':
            if topo == 0:
                return False

            topo -= 1

            if caractere == ')' and pilha[topo] != '(':
                return False

            if caractere == ']' and pilha[topo] != '[':
                return False

    return topo == 0
