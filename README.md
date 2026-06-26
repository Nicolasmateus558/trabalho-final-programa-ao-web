# Detecção de Fraudes em Transações Bancárias com Computação Paralela

Este é um projeto acadêmico para a disciplina de **Programação Concorrente e Distribuída** que analisa fraudes financeiras usando o dataset PaySim1, comparando desempenho entre processamento serial e paralelo com `multiprocessing`.

## Principais Destaques

**Objetivo:** Demonstrar ganhos práticos de computação paralela processando centenas de milhões de registros bancários.

**Tecnologia:** Python com `multiprocessing` em vez de threads, pois múltiplas threads não conseguem executar código Python simultaneamente em operações CPU-bound devido ao GIL.

## Dataset PaySim1

- **Tamanho original:** 6,3 milhões de transações (~460 MB)
- **Versão expandida:** 203,6 milhões de transações (~15 GB)
- **Taxa de fraude:** 0,1291% (predominante em TRANSFER e CASH_OUT)
- **Valor movimentado:** R$ 36,6 trilhões na versão expandida

## Execução dos Scripts

Os 5 scripts devem rodar em sequência:

1. `01_explorar_dataset.py` — análise inicial do dataset
2. `02_expandir_dataset.py` — gera versão de 15 GB
3. `03_sequencial.py` — processamento serial (baseline)
4. `04_paralelo.py` — benchmark com 1-12 processos
5. `05_graficos.py` — gera visualizações de desempenho

## Resultados Obtidos

### Ambiente 1 — Intel Core i5-4590 (4 núcleos)

Com 4 processos paralelos:

- **Tempo reduzido de 528s para 170s** (redução de 67,8%)
- **Speedup de 3,11x com eficiência de 77,6%**
- Ganho máximo limitado pelos 4 núcleos físicos disponíveis

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 1         | 528.00    | 1.00x   | 1.0000     |
| 2         | —         | —       | —          |
| 4         | 170.00    | 3.11x   | 0.7760     |

### Ambiente 2 — AMD Ryzen 7 5700 (8 núcleos físicos / 16 threads)

**Especificações:**
- Processador: AMD Ryzen 7 5700 — 8 núcleos físicos / 16 threads lógicos
- Clock base: 3.701 MHz
- RAM: 32 GB
- Sistema Operacional: Windows 11 Pro 64-bit
- Python: 3.14.6
- Dataset: PaySim1 expandido — 203.603.840 transações (~15 GB, idêntico ao Ambiente 1)

**Resultados:**

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 1         | 152.89    | 1.00x   | 1.0000     |
| 2         | 80.36     | 1.90x   | 0.9512     |
| 4         | 44.50     | 3.44x   | 0.8589     |
| 8         | 28.31     | 5.40x   | 0.6750     |
| 12        | 22.00     | 6.95x   | 0.5791     |

**Comparação direta com 4 processos:** 3.44x (Ryzen 7 5700) vs 3.11x (i5-4590) — **+10,6% de speedup relativo**.

Com 8 núcleos disponíveis foi possível testar configurações além dos 4 processos do Ambiente 1, atingindo **6.95x de speedup com 12 processos** — mais que o dobro do melhor resultado anterior.

A eficiência mais alta no Ambiente 2 (85,9% com 4 processos vs 77,6% no Ambiente 1) reflete menor overhead de serialização IPC proporcionalmente ao poder de processamento disponível.

## Análise — Lei de Amdahl

O crescimento do speedup desacelera conforme o número de processos aumenta, ilustrando a Lei de Amdahl: a fração sequencial do código (loop Python de classificação de risco) limita o ganho máximo teórico independentemente de quantos núcleos sejam usados.

A eficiência cai de 95,1% com 2 processos para 57,9% com 12, evidenciando o overhead crescente de comunicação entre processos via IPC (Inter-Process Communication).
