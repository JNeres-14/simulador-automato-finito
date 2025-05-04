# Simulador de Autômatos Finitos

## Descrição

Este projeto é um simulador de linha de comando capaz de processar três tipos de autômatos finitos:

- AFD – Autômato Finito Determinístico  
- AFN – Autômato Finito Não Determinístico  
- AFN-λ – AFN com transições vazias (ε)

A ferramenta recebe como entrada a definição do autômato e uma lista de palavras, simulando seu comportamento e verificando se cada palavra é aceita ou rejeitada.

---

## Funcionalidades

- Detecta automaticamente o tipo de autômato com base nas transições.
- Lê arquivos `.aut` (formato JSON) contendo a definição do autômato.
- Lê arquivos `.in` com as palavras de teste e o resultado esperado.
- Executa as simulações e gera um arquivo `.out` com os resultados comparados.
- Mede o tempo de execução individual de cada palavra.

---

## Como usar

Execute o simulador via terminal com o comando:

```bash
python simulador_af.py exemplo.aut exemplo.in resultado.out

python simulador_af.py exemplo.aut exemplo.in resultado.out

python simulador_af.py exemplo.aut exemplo.in resultado.out
```

## Formatos dos Arquivos

### Automato (`.aut`)
```json
{
  "initial": 0,
  "final": [2],
  "transitions": [
    {"from": 0, "read": "a", "to": 1},
    {"from": 1, "read": "b", "to": 2},
    {"from": 2, "read": "c", "to": 2},
    {"from": 1, "read": null, "to": 0}
  ]
}
```

### Entradas (`.in`)
```
palavra;resultadoesperado
abc;1
abcc;1
a;0
ac;0
b;0
ab;1
```

### Saída (`.out`)
```
abc;1;1;0.000123
abcc;1;1;0.000145
a;0;0;0.000089
...
```

## Autor
Trabalho individual realizado como parte da disciplina de Autômatos.

**Nome:** José Neres de Meira Filho  
**Curso:** Ciência da Computação – UENP  
**Data:** Maio de 2025
