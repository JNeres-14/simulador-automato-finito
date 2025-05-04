# Simulador de Autômatos Finitos

## Descrição
Ferramenta que simula autômatos finitos (DFA, NFA e com transições vazias) a partir de arquivos de entrada fornecidos.

## Uso
Executar via terminal:

```bash
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
...
```

## Autor
Trabalho individual realizado como parte da disciplina de Autômatos.
**Nome:** José Neres de Meira Filho  
**Curso:** Ciência da Computação – UENP  
**Data:** Maio de 2025
