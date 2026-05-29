# Detecção de Fraudes em Transações Bancárias
Projeto acadêmico de Computação Paralela utilizando o dataset PaySim1 para análise de transações financeiras e simulação de detecção de fraudes.

## Dataset
[PaySim1 — Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)

Dataset simulado de transações financeiras via celular com ~6,3 milhões de registros. Colunas principais: `step`, `type`, `amount`, `isFraud`.

## Objetivo
Comparar o desempenho entre processamento **sequencial** e **paralelo** utilizando grandes volumes de dados (~44 milhões de linhas / 3,31 GB).

Métricas avaliadas:
- Tempo de execução
- Speedup (Tempo Serial / Tempo Paralelo)
- Ganho de desempenho com paralelismo

## Ferramentas Utilizadas
- Python 3
- Pandas
- NumPy
- Matplotlib
- Multiprocessing

## Estrutura do Projeto
```
Projeto_Paralela_PaySim/
├── paysim.csv                  # Dataset original (~6,3M linhas)
├── paysim_grande.csv           # Dataset expandido (~44M linhas / 3,31 GB)
├── 01_explorar_dataset.py      # Exploração e entendimento do dataset
├── 02_expandir_dataset.py      # Expansão artificial dos dados
├── 03_sequencial.py            # Análise sequencial (baseline)
├── 04_paralelo.py              # Análise paralela com multiprocessing
├── 05_graficos.py              # Geração de gráficos de desempenho
├── tempo_sequencial.txt        # Tempo serial salvo para comparação
└── requirements.txt
```

## Instalação
```bash
pip install pandas numpy matplotlib seaborn tqdm
```

## Execução

### 1. Explorar o dataset original
```bash
python 01_explorar_dataset.py
```

### 2. Expandir o dataset para ~3GB
```bash
python 02_expandir_dataset.py
```

### 3. Rodar versão sequencial (baseline)
```bash
python 03_sequencial.py
```

### 4. Rodar versão paralela
```bash
python 04_paralelo.py
```

### 5. Gerar gráficos de comparação
```bash
python 05_graficos.py
```

## Resultados Parciais

| Etapa | Resultado |
|-------|-----------|
| Dataset original | 6.362.620 linhas |
| Dataset expandido | 44.538.340 linhas — 3,31 GB |
| Fraudes detectadas | 57.491 (0,1291%) |
| Tempo serial (processamento) | ~0,31 segundos |
| Tempo paralelo | em desenvolvimento |
| Speedup | em desenvolvimento |

> O tempo medido considera apenas o processamento dos chunks, sem a leitura do arquivo, garantindo comparação justa entre as versões.

## Fórmula do Speedup
```
Speedup = Tempo Serial / Tempo Paralelo
```

## Autor
**Kelvin Rafael de Souza Pereira**

[LinkedIn](https://www.linkedin.com/in/kelvin-raphael-7b4278231)
