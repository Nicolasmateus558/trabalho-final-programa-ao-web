# Detecção  de grandes em transações bancárias
Computação Paralela com PaySim1

Projeto acadêmico de Computação Paralela utilizando o dataset PaySim1 para análise de transações financeiras e simulação de detecção de fraudes.

Dataset utilizado:
PaySim1 - Kaggle

Objetivo

O foco do projeto é comparar o desempenho entre:

Processamento Sequencial
Processamento Paralelo com multiprocessing

Utilizando grandes volumes de dados para medir:

Tempo de execução
Speedup
Ganho de desempenho
Eficiência do paralelismo
Tecnologias Utilizadas
Python 3
Pandas
NumPy
Matplotlib
Multiprocessing
Estrutura do Projeto
Projeto_Paralela_PaySim/
│
├── data/                # Dataset
├── src/                 # Códigos principais
├── resultados/          # Gráficos e resultados
├── README.md
└── requirements.txt
Funcionalidades
Carregamento do dataset com pandas
Explicação das colunas do PaySim
Aumento artificial do dataset
Análise sequencial
Processamento paralelo
Comparação de desempenho
Cálculo de speedup
Geração de gráficos
Instalação

Clone o repositório:

git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

Instale as dependências:

pip install -r requirements.txt
Execução
Rodar análise inicial
python src/main.py
Aumentar dataset
python src/aumento_dataset.py
Executar versão sequencial
python src/sequencial.py
Executar versão paralela
python src/paralelo.py
Fórmula do Speedup

Speedup=
Tempo Paralelo
Tempo Sequencial
	​


Resultados Esperados
Melhor desempenho utilizando paralelismo
Redução do tempo de processamento
Comparação visual através de gráficos
Aplicação prática de computação paralela
