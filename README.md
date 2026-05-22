# Detecção  de fraudes em transações bancárias
# Detecção de Fraudes em Transações Bancárias

Projeto acadêmico de Computação Paralela utilizando o dataset PaySim1 para análise de transações financeiras e simulação de detecção de fraudes.

## Dataset

PaySim1:  
https://www.kaggle.com/datasets/ealaxi/paysim1

---

## Objetivo

O foco do projeto é comparar o desempenho entre:

- Processamento Sequencial
- Processamento Paralelo com `multiprocessing`

Utilizando grandes volumes de dados para medir:

- Tempo de execução
- Speedup
- Ganho de desempenho
- Eficiência do paralelismo

---

## Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Multiprocessing

---

## Estrutura do Projeto

```txt
Projeto_Paralela_PaySim/
│
├── data/                # Dataset
├── src/                 # Códigos principais
├── resultados/          # Gráficos e resultados
├── README.md
└── requirements.txt
```

---

## Funcionalidades

- Carregamento do dataset com pandas
- Explicação das colunas do PaySim
- Aumento artificial do dataset
- Análise sequencial
- Processamento paralelo
- Comparação de desempenho
- Cálculo de speedup
- Geração de gráficos

---

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

### Rodar análise inicial

```bash
python src/main.py
```

### Aumentar dataset

```bash
python src/aumento_dataset.py
```

### Executar versão sequencial

```bash
python src/sequencial.py
```

### Executar versão paralela

```bash
python src/paralelo.py
```

---

## Fórmula do Speedup

Speedup = Tempo Sequencial / Tempo Paralelo

---

## Resultados Esperados

- Melhor desempenho utilizando paralelismo
- Redução do tempo de processamento
- Comparação visual através de gráficos
- Aplicação prática de computação paralela

---

## Autor

Kelvin Raphael de Souza Pereira

LinkedIn:  
https://www.linkedin.com/in/kelvin-raphael-7b4278231
