# Relatório — Detecção de Fraudes em Transações Bancárias com Computação Paralela

**Disciplina:** Programação Concorrente e Distribuída
**Aluno(s):** Kelvin Raphael de Souza Pereira
**Turma:**
**Professor:**
**Data:**

---

## 1. Descrição do Problema

O problema consiste em analisar um dataset de transações financeiras (PaySim1) contendo **203.603.840 registros** (~15 GB), aplicando técnicas de detecção de fraudes e medindo o desempenho da execução serial como baseline para comparação futura com a versão paralela.

**Algoritmo utilizado:** Leitura do arquivo CSV em chunks de 1.000.000 linhas, processando cada chunk sequencialmente — contagem de transações, fraudes e valor movimentado agrupados por tipo.

**Tamanho da entrada:** 203.603.840 transações financeiras (arquivo `paysim_grande.csv`, ~15 GB).

**Objetivo da paralelização (próxima etapa):** Reduzir o tempo de execução distribuindo os chunks entre múltiplos processos com `multiprocessing.Pool`, contornando o GIL do Python.

**Complexidade aproximada:** O(n), onde n é o número de transações.

---

## 2. Ambiente Experimental

| Item | Descrição |
|------|-----------|
| Processador | Intel(R) Core(TM) i5-4590 CPU @ 3.30GHz |
| Número de núcleos | 4 núcleos físicos / 4 lógicos |
| Memória RAM | 16,0 GB |
| Sistema Operacional | Windows 10 Home |
| Linguagem utilizada | Python 3.14 |
| Biblioteca de paralelização | multiprocessing (Pool + map) — próxima etapa |
| Versão do Python | 3.14 |

---

## 3. Metodologia de Testes

**Medição de tempo:** Utilizou-se `time.time()` antes e depois do laço de leitura e processamento.

**Número de execuções:** 1 execução por configuração.

**Entrada utilizada:** `paysim_grande.csv` com 203.603.840 transações (~15 GB), gerado a partir do dataset original PaySim1 com 32 cópias e variação de ±5% nos valores numéricos para simular períodos distintos.

**Estratégia de leitura:** O arquivo foi lido em chunks de 1.000.000 linhas via `pd.read_csv(chunksize=1_000_000)`, pois o dataset ultrapassa a memória RAM disponível e não pode ser carregado de uma só vez.

**Cálculos realizados em cada chunk:**

1. **Contagem de transações e fraudes** — para cada chunk, conta o total de transações e soma os registros onde `isFraud = 1`, identificando quantas são fraudulentas.

2. **Valor total movimentado** — soma o campo `amount` de todas as transações do chunk, obtendo o volume financeiro processado.

3. **Agrupamento por tipo de transação** — agrupa as transações pelos 5 tipos existentes (PAYMENT, TRANSFER, CASH_OUT, CASH_IN, DEBIT) e calcula, para cada tipo: quantidade de transações, número de fraudes e valor total movimentado.

Ao final, a função `consolidar_resultados()` soma os resultados dos 204 chunks, produzindo os totais gerais.

**Configurações testadas (serial):**
- 1 processo (serial) — baseline medido

**Configurações a testar (próxima etapa):**
- 2 processos
- 4 processos
- 8 processos

---

## 4. Resultados Experimentais — Serial

| Nº de Processos | Tempo de Execução (s) |
|-----------------|----------------------|
| 1 (serial) | 470.1181 |
| 2 | *(próxima etapa)* |
| 4 | *(próxima etapa)* |
| 8 | *(próxima etapa)* |

### Resultado da análise serial

| Métrica | Valor |
|---------|-------|
| Chunks processados | 204 |
| Total de transações | 203.603.840 |
| Transações fraudulentas | 262.816 |
| Taxa de fraude | 0,1291% |
| Valor total movimentado | R$ 36.620.503.101.725,17 |
| Valor em fraudes | R$ 385.782.746.434,22 |

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
| 1 | 470.1181 | 1.00 | 1.00 |
| 2 | *(próxima etapa)* | — | — |
| 4 | *(próxima etapa)* | — | — |
| 8 | *(próxima etapa)* | — | — |

---

## 7. Gráfico de Tempo de Execução

*(a gerar na próxima etapa)*

**Eixo X:** Número de processos
**Eixo Y:** Tempo de execução (segundos)

---

## 8. Gráfico de Speedup

*(a gerar na próxima etapa)*

---

## 9. Gráfico de Eficiência

*(a gerar na próxima etapa)*

---

## 10. Análise dos Resultados

### Serial (baseline atual)

O processamento serial de **203 milhões de transações** em um arquivo de **15 GB** levou **470 segundos (~7,8 minutos)**. O tempo é dominado pela leitura sequencial do disco — o dataset ultrapassa a memória RAM disponível, exigindo leitura em chunks. O processamento de cada chunk (agrupamento por tipo, soma de valores, contagem de fraudes) é eficiente via pandas, mas ocorre um chunk por vez.

### Análise esperada do paralelo (próxima etapa)

- Com `multiprocessing`, múltiplos chunks serão processados simultaneamente em núcleos diferentes
- O ganho será sobre o tempo de processamento (CPU), enquanto o tempo de I/O (leitura de disco) permanece igual
- Espera-se speedup entre 2x e 4x com 4 processos

---

## 11. Conclusão

*(a completar após etapa paralela)*

O baseline serial foi estabelecido com sucesso: **470 segundos** para análise de 203 milhões de transações bancárias em 15 GB de dados. Os resultados da análise confirmam os dados do dataset PaySim1 — taxa de fraude de 0,1291%, consistente com o dataset original.

A próxima etapa implementará a versão paralela com `multiprocessing.Pool`, permitindo o cálculo de speedup e eficiência para 2, 4 e 8 processos.

**Dataset:** PaySim1 — Kaggle ([link](https://www.kaggle.com/datasets/ealaxi/paysim1))
**Autor:** Kelvin Raphael de Souza Pereira
