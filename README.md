# Relatório — Detecção de Fraudes em Transações Bancárias com Computação Paralela

**Disciplina:** Programação Concorrente e Distribuída
**Aluno(s):** Kelvin Raphael de Souza Pereira
**Turma:**
**Professor:**
**Data:**

---

## 1. Descrição do Problema

O problema consiste em analisar um dataset de transações financeiras (PaySim1) contendo **6.362.620 registros**, aplicando técnicas de detecção de fraudes e medindo o desempenho entre execução serial e paralela com diferentes números de processos.

**Algoritmo utilizado:** Análise de fraudes por chunks, paralelizada distribuindo os chunks entre processos independentes usando `multiprocessing.Pool`.

**Tamanho da entrada:** 6.362.620 transações financeiras (arquivo `paysim.csv`, ~460 MB).

**Objetivo da paralelização:** Reduzir o tempo de execução da análise utilizando múltiplos processos, contornando o GIL do Python com `multiprocessing`.

**Complexidade aproximada:** O(n) por chunk, onde n é o número de transações no chunk.

**Técnicas de detecção de fraude aplicadas:**
- **Z-score por tipo de transação** — identifica valores estatisticamente anômalos
- **Lei de Benford** — fraudes tendem a violar a distribuição natural dos primeiros dígitos dos valores
- **Alta velocidade por conta** — muitas transações da mesma conta no mesmo período são suspeitas
- **Inconsistência de saldo** — saldo não alterado após transação é indicador direto de fraude no PaySim

---

## 2. Ambiente Experimental

| Item | Descrição |
|------|-----------|
| Processador | Intel(R) Core(TM) i5-4590 CPU @ 3.30GHz |
| Número de núcleos | 4 núcleos físicos / 4 lógicos |
| Memória RAM | 16,0 GB |
| Sistema Operacional | Windows 10 Home |
| Linguagem utilizada | Python 3.14 |
| Biblioteca de paralelização | multiprocessing (Pool + map) |
| Versão do Python | 3.14 |

---

## 3. Metodologia de Testes

**Medição de tempo:** Utilizou-se `time.time()` antes e depois do processamento dos chunks, excluindo o tempo de leitura do arquivo para garantir comparação justa.

**Número de execuções:** 1 execução por configuração.

**Entrada utilizada:** `paysim.csv` com 6.362.620 transações financeiras.

**Configurações testadas:**
- 1 processo (serial)
- 2 processos
- 4 processos
- 8 processos

**Estratégia de paralelização:**

O dataset foi dividido em chunks de 1.000.000 linhas. Cada chunk foi distribuído entre os processos via `multiprocessing.Pool.map()`, que executa a função `analisar_chunk()` em paralelo. Por usar processos (não threads), o GIL do Python não limita o desempenho — cada processo tem seu próprio interpretador e executa em um núcleo físico diferente.

---

## 4. Resultados Experimentais

| Nº de Processos | Tempo de Execução (s) |
|-----------------|----------------------|
| 1 (serial)      | 28.2915              |
| 2               | *(a preencher)*      |
| 4               | *(a preencher)*      |
| 8               | *(a preencher)*      |

---

## 5. Cálculo de Speedup e Eficiência

**Fórmulas utilizadas:**

```
Speedup(p)    = T(1) / T(p)
Eficiência(p) = Speedup(p) / p
```

---

## 6. Tabela de Resultados

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 1         | 28.2915   | 1.00    | 1.00       |
| 2         | *(a preencher)* | *(a calcular)* | *(a calcular)* |
| 4         | *(a preencher)* | *(a calcular)* | *(a calcular)* |
| 8         | *(a preencher)* | *(a calcular)* | *(a calcular)* |

---

## 7. Gráfico de Tempo de Execução

*(inserir gráfico gerado pelo script `05_graficos.py`)*

**Eixo X:** Número de processos
**Eixo Y:** Tempo de execução (segundos)

---

## 8. Gráfico de Speedup

*(inserir gráfico gerado pelo script `05_graficos.py`)*

---

## 9. Gráfico de Eficiência

*(inserir gráfico gerado pelo script `05_graficos.py`)*

---

## 10. Análise dos Resultados

*(a completar após rodar o paralelo)*

**Pontos esperados de análise:**
- O speedup com `multiprocessing` tende a ser real (diferente de threads), pois cada processo usa um núcleo físico independente
- Com 4 núcleos disponíveis, o ganho máximo esperado é ~4x (speedup ideal)
- O speedup real será menor devido ao overhead de: criação de processos, serialização dos dados entre processos (pickle) e junção dos resultados
- A eficiência tende a cair com o aumento do número de processos acima do número de núcleos físicos (4)

---

## 11. Conclusão

*(a completar após rodar o paralelo)*

O projeto demonstrou que a análise de fraudes em grandes volumes de dados pode se beneficiar significativamente do paralelismo via `multiprocessing`. Ao contrário de threads, processos independentes contornam o GIL do Python e permitem verdadeiro paralelismo em operações CPU-bound, como os cálculos estatísticos aplicados.

**Dataset:** PaySim1 — Kaggle ([link](https://www.kaggle.com/datasets/ealaxi/paysim1))
**Autor:** Kelvin Raphael de Souza Pereira
