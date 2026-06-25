# Detecção de Fraudes em Transações Bancárias com Computação Paralela

> Projeto acadêmico da disciplina de **Programação Concorrente e Distribuída**
> utilizando o dataset PaySim1 para análise de fraudes financeiras, comparando
> desempenho entre processamento **serial** e **paralelo** com `multiprocessing`.

---

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Dataset](#dataset)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Ambiente e Requisitos](#ambiente-e-requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [O que cada script faz](#o-que-cada-script-faz)
- [Resultados](#resultados)
- [Análise de Desempenho](#análise-de-desempenho)
- [Conclusão](#conclusão)
- [Autor](#autor)

---

## Sobre o Projeto

O objetivo deste projeto é demonstrar na prática os ganhos de desempenho obtidos com **computação paralela** no contexto de análise de grandes volumes de dados financeiros.

O problema escolhido é a **detecção de fraudes** em transações bancárias: dado um dataset com centenas de milhões de registros, queremos calcular estatísticas de fraude, identificar transações suspeitas e medir o desempenho comparativo entre as abordagens serial e paralela.

### Por que Multiprocessing e não Threads?

Python possui o **GIL (Global Interpreter Lock)**, uma trava interna que impede que múltiplas threads executem código Python ao mesmo tempo em operações CPU-bound. Por isso, para operações de cálculo intensivo como as deste projeto, `multiprocessing` é a escolha correta — cada processo tem seu próprio interpretador Python e pode rodar em um núcleo físico diferente, obtendo paralelismo real.

---

## Dataset

**PaySim1** — Simulação de transações financeiras via celular

- Fonte: [Kaggle — PaySim1](https://www.kaggle.com/datasets/ealaxi/paysim1)
- Dataset original: **6.362.620 linhas**, ~460 MB
- Dataset expandido artificialmente: **203.603.840 linhas**, ~15 GB

### Colunas do Dataset

| Coluna | Descrição |
|--------|-----------|
| `step` | Hora da transação (1 = 1 hora) |
| `type` | Tipo: PAYMENT, TRANSFER, CASH_OUT, DEBIT, CASH_IN |
| `amount` | Valor da transação |
| `nameOrig` | Conta de origem |
| `oldbalanceOrg` | Saldo do remetente antes |
| `newbalanceOrig` | Saldo do remetente depois |
| `nameDest` | Conta de destino |
| `oldbalanceDest` | Saldo do destinatário antes |
| `newbalanceDest` | Saldo do destinatário depois |
| `isFraud` | **1 = fraude, 0 = legítima** |
| `isFlaggedFraud` | Detecção do sistema original (imprecisa) |

### Dados do Dataset Original

| Métrica | Valor |
|---------|-------|
| Total de transações | 6.362.620 |
| Transações fraudulentas | 8.213 (0,1291%) |
| Tipos com fraude | TRANSFER e CASH_OUT apenas |
| Valor total movimentado | R$ 1.144.392.944.759,77 |
| Valor em fraudes | R$ 12.056.415.427,84 |

> **Fraudes ocorrem apenas em TRANSFER (0,77%) e CASH_OUT (0,18%)** — as demais categorias não apresentam fraudes no PaySim.

---

## Estrutura do Projeto

```
Projeto_Paralela_PaySim/
│
├── 01_explorar_dataset.py     # Etapa 1: carrega e analisa o dataset original
├── 02_expandir_dataset.py     # Etapa 2: expande o dataset para ~15 GB
├── 03_sequencial.py           # Etapa 3: análise serial (baseline de tempo)
├── 04_paralelo.py             # Etapa 4: benchmark paralelo (2, 4, 8, 12 processos)
├── 05_graficos.py             # Etapa 5: gera os gráficos de desempenho
│
├── graficos/
│   ├── 01_tempo.png           # Gráfico: tempo × processos
│   ├── 02_speedup.png         # Gráfico: speedup × processos
│   └── 03_eficiencia.png      # Gráfico: eficiência × processos
│
├── tempo_sequencial.txt       # Tempo serial salvo automaticamente
├── resultados_benchmark.txt   # Resultados do benchmark paralelo
├── RELATORIO.md               # Relatório acadêmico completo
├── .gitignore                 # Ignora arquivos CSV grandes
└── README.md                  # Este arquivo
```

> Os arquivos `paysim.csv` e `paysim_grande.csv` **não estão no repositório** por excederem o limite do GitHub (460 MB e 15 GB). Baixe o dataset original no link acima e execute o `02_expandir_dataset.py` para gerar a versão expandida.

---

## Ambiente e Requisitos

| Item | Versão/Especificação |
|------|---------------------|
| Python | 3.14 |
| pandas | 3.0.0 |
| numpy | 2.4.1 |
| matplotlib | 3.10.9 |
| seaborn | 0.13.2 |
| Sistema Operacional | Windows 10 Home |
| Processador | Intel Core i5-4590 @ 3.30GHz |
| Núcleos físicos | 4 |
| RAM | 16 GB |

---

## Instalação

```bash
pip install pandas numpy matplotlib seaborn tqdm
```

---

## Como Executar

Execute os scripts **em ordem**, a partir da pasta do projeto:

### Etapa 1 — Explorar o dataset original
```bash
python 01_explorar_dataset.py
```
Carrega o `paysim.csv`, exibe informações gerais, estatísticas e análise de fraudes por tipo.

---

### Etapa 2 — Expandir o dataset para ~15 GB
```bash
python 02_expandir_dataset.py
```
Gera 32 cópias do dataset com variação de ±5% nos valores numéricos, simulando diferentes períodos de transações. Salva em `paysim_grande.csv`.

> ⚠️ Este processo demora vários minutos e requer ~15 GB de espaço em disco.

---

### Etapa 3 — Análise Serial (baseline)
```bash
python 03_sequencial.py
```
Lê o `paysim_grande.csv` em chunks de 1.000.000 linhas e processa sequencialmente. Salva o tempo em `tempo_sequencial.txt`.

---

### Etapa 4 — Benchmark Paralelo
```bash
python 04_paralelo.py
```
Carrega 100 chunks em memória e executa o benchmark com 1, 2, 4, 8 e 12 processos. Exibe a tabela completa de speedup e eficiência. Salva os resultados em `resultados_benchmark.txt`.

> ⚠️ Requer ~4 GB de RAM disponível para carregar os chunks. O processo completo pode levar 30–60 minutos.

---

### Etapa 5 — Gerar Gráficos
```bash
python 05_graficos.py
```
Gera os 3 gráficos de desempenho na pasta `graficos/`.

---

## O que cada script faz

### `processar_chunk(chunk)` — função central

A mesma função é usada no serial e no paralelo. Para cada chunk de 1.000.000 linhas, ela realiza:

**1. Contagem de fraudes e valor total**
```python
n_fraudes   = int(chunk['isFraud'].sum())
valor_total = float(chunk['amount'].sum())
```

**2. Z-score por tipo de transação**

Para cada um dos 5 tipos, calcula a distribuição estatística e identifica transações com z-score > 3 como outliers suspeitos:
```
z = |valor - média| / desvio_padrão
```
Transações com z > 3 estão a mais de 3 desvios padrão da média — estatisticamente raras e potencialmente fraudulentas.

**3. Classificação de risco por transação (loop Python)**

Cada transação é classificada individualmente:
- **ALTO** — TRANSFER ou CASH_OUT com valor > R$ 200.000
- **MÉDIO** — qualquer tipo com valor > R$ 50.000
- **BAIXO** — demais transações

Este loop em Python puro sobre 1 milhão de linhas é intencionalmente **CPU-intensivo**, tornando o processamento paralelo genuinamente mais rápido.

---

## Resultados

### Análise do Dataset Original (Etapa 1)

| Tipo | Transações | Fraudes | % Fraude |
|------|-----------|---------|---------|
| CASH_OUT | 2.237.500 | 4.116 | 0,184% |
| TRANSFER | 532.909 | 4.097 | 0,769% |
| PAYMENT | 2.151.495 | 0 | 0,000% |
| CASH_IN | 1.399.284 | 0 | 0,000% |
| DEBIT | 41.432 | 0 | 0,000% |

### Análise Serial no Dataset de 15 GB (Etapa 3)

| Métrica | Valor |
|---------|-------|
| Dataset utilizado | paysim_grande.csv (15,26 GB) |
| Total de transações | 203.603.840 |
| Chunks processados | 204 |
| Fraudes detectadas | 262.816 |
| Taxa de fraude | 0,1291% |
| Valor movimentado | R$ 36.620.503.101.725,17 |
| **Tempo serial (processamento)** | **470,12 segundos** |

### Benchmark Paralelo — 100 milhões de transações (Etapa 4)

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 1 (serial) | 528,54 | 1,00x | 100,0% |
| 2 | 293,59 | 1,80x | 90,0% |
| 4 | 170,20 | 3,11x | 77,6% |
| 8 | 165,28 | 3,20x | 40,0% |
| 12 | 152,27 | 3,47x | 28,9% |

---

## Análise de Desempenho

### Fórmulas utilizadas

```
Speedup(p)    = T(1) / T(p)
Eficiência(p) = Speedup(p) / p
```

### Gráfico de Tempo de Execução

![Tempo de Execução](graficos/01_tempo.png)

### Gráfico de Speedup

![Speedup](graficos/02_speedup.png)

### Gráfico de Eficiência

![Eficiência](graficos/03_eficiencia.png)

### Interpretação dos Resultados

**De 1 para 2 processos:** speedup de 1,80x com eficiência de 90%. O ganho é quase linear — cada processo ocupa um núcleo físico e o trabalho é bem distribuído.

**De 2 para 4 processos:** speedup de 3,11x com eficiência de 77,6%. Ainda muito bom — os 4 núcleos físicos do processador estão sendo utilizados ao máximo.

**De 4 para 8 processos:** speedup marginal (3,11 → 3,20). O processador possui apenas 4 núcleos físicos; adicionar mais processos força o sistema operacional a escalonar entre eles, gerando overhead sem ganho proporcional.

**De 8 para 12 processos:** ganho pequeno (3,20 → 3,47). A eficiência cai para 28,9% — o overhead de criação e escalonamento de processos consome parte do ganho.

### Lei de Amdahl

O teto do speedup é limitado pela **fração serial** do código (consolidação dos resultados, I/O). Mesmo com processadores infinitos, existe um limite máximo de speedup — fenômeno descrito pela Lei de Amdahl:

```
Speedup_max = 1 / (fração_serial)
```

A curva de speedup do projeto (que desacelera após 4 processos) ilustra exatamente este princípio.

---

## Conclusão

- O paralelismo via `multiprocessing` reduziu o tempo de processamento de **528 segundos** para **170 segundos** com 4 processos — uma redução de **67,8%**.
- O maior ganho ocorreu até o limite de **núcleos físicos disponíveis (4)**, confirmando que o hardware define o teto prático do paralelismo.
- Processos foram mais adequados que threads para este problema, pois contornam o GIL do Python em operações CPU-bound.
- A eficiência de **77,6% com 4 processos** é um resultado sólido para análise de dados em larga escala.

---

## Autor

**Kelvin Raphael de Souza Pereira**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kelvin%20Raphael-blue)](https://www.linkedin.com/in/kelvin-raphael-7b4278231)

---

*Disciplina: Programação Concorrente e Distribuída*
