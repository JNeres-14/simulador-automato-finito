import json
import csv
import time
import sys
from collections import defaultdict, deque

def carregar_automato(arquivo_automato):
    with open(arquivo_automato, 'r') as f:
        return json.load(f)

def carregar_testes(arquivo_entrada):
    with open(arquivo_entrada, 'r') as f:
        leitor = csv.reader(f, delimiter=';')
        return [ (linha[0], int(linha[1])) for linha in leitor ]

def escrever_saida(arquivo_saida, resultados):
    with open(arquivo_saida, 'w', newline='') as f:
        escritor = csv.writer(f, delimiter=';')
        for resultado in resultados:
            escritor.writerow(resultado)

def construir_transicoes(transicoes_raw):
    from collections import defaultdict
    transicoes = defaultdict(list)
    for t in transicoes_raw:
        transicoes[(t['from'], t['read'])].append(t['to'])
    return transicoes

def mover(transicoes, estado, simbolo):
    return transicoes.get((estado, simbolo), [])

def epsilon_closure(transicoes, estados):
    pilha = deque(estados)
    visitados = set(estados)
    while pilha:
        estado = pilha.pop()
        for proximo in mover(transicoes, estado, None):
            if proximo not in visitados:
                visitados.add(proximo)
                pilha.append(proximo)
    return visitados

def simular_af(automato, palavra):
    transicoes = construir_transicoes(automato['transitions'])
    estados_atuais = epsilon_closure(transicoes, [automato['initial']])
    
    for simbolo in palavra:
        proximos = set()
        for estado in estados_atuais:
            proximos.update(mover(transicoes, estado, simbolo))
        estados_atuais = epsilon_closure(transicoes, proximos)

    return any(estado in automato['final'] for estado in estados_atuais)

def main():
    if len(sys.argv) != 4:
        print("Uso: python simulador_af.py arquivo_automato.aut arquivo_entrada.in arquivo_saida.out")
        sys.exit(1)

    arquivo_automato, arquivo_entrada, arquivo_saida = sys.argv[1], sys.argv[2], sys.argv[3]

    automato = carregar_automato(arquivo_automato)
    testes = carregar_testes(arquivo_entrada)
    resultados = []

    for palavra, esperado in testes:
        inicio = time.time()
        obtido = int(simular_af(automato, palavra))
        fim = time.time()
        resultados.append([palavra, esperado, obtido, round(fim - inicio, 6)])

    escrever_saida(arquivo_saida, resultados)

if __name__ == "__main__":
    main()
