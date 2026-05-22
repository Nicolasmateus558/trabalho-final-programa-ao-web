# detecção  de grandes em transações bancárias
Computação Paralela com PaySim1

Projeto acadêmico de Computação Paralela utilizando o dataset PaySim1 para análise de transações financeiras e simulação de detecção de fraudes.

Dataset:
PaySim1 - Kaggle

Objetivo

Comparar desempenho entre processamento sequencial e paralelo em Python utilizando grandes volumes de dados.

O projeto inclui:

Leitura do dataset com pandas
Explicação das colunas
Aumento artificial do dataset
Processamento sequencial
Processamento paralelo com multiprocessing
Medição de tempo de execução
Cálculo de speedup
Geração de gráficos
Tecnologias
Python 3
Pandas
NumPy
Matplotlib
Multiprocessing
Estrutura
Projeto_Paralela_PaySim/
│
├── data/
├── src/
├── resultados/
├── README.md
└── requirements.txt
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
Speedup

Speedup=
Tempo Paralelo
Tempo Sequencial
	​


Resultados Esperados
Redução do tempo de execução
Melhor desempenho com paralelismo
Comparação visual através de gráficos
