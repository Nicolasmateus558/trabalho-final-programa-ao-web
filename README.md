# detecção  de grandes em transações bancárias
Projeto de Computação Paralela com PaySim1

Projeto acadêmico desenvolvido para a disciplina de Computação Paralela, utilizando o dataset PaySim1 para simulação e análise de transações financeiras e detecção de fraudes.

Dataset utilizado:
PaySim1 Dataset - Kaggle

Objetivo do Projeto

O objetivo principal deste projeto é comparar o desempenho entre processamento sequencial e processamento paralelo em Python utilizando um grande volume de dados financeiros.

O projeto inclui:

Leitura e análise do dataset PaySim
Explicação das colunas e estrutura dos dados
Aumento artificial do dataset
Processamento sequencial
Processamento paralelo com multiprocessing
Medição de tempo de execução
Cálculo de speedup
Geração de gráficos de desempenho
Estrutura para relatório acadêmico
Tecnologias Utilizadas
Python 3
Pandas
NumPy
Matplotlib
Multiprocessing
Estrutura do Projeto
Projeto_Paralela_PaySim/
│
├── data/
│   └── PS_20174392719_1491204439457_log.csv
│
├── src/
│   ├── main.py
│   ├── sequencial.py
│   ├── paralelo.py
│   ├── aumento_dataset.py
│   └── graficos.py
│
├── resultados/
│   ├── graficos/
│   └── logs/
│
├── README.md
└── requirements.txt
Sobre o Dataset

O PaySim é um dataset sintético que simula transações financeiras móveis.

Principais colunas:

Coluna	Descrição
step	Momento da transação
type	Tipo da transação
amount	Valor transferido
nameOrig	Conta de origem
oldbalanceOrg	Saldo antes da transação
newbalanceOrig	Saldo após transação
nameDest	Conta destino
oldbalanceDest	Saldo destino antes
newbalanceDest	Saldo destino após
isFraud	Indica se houve fraude
isFlaggedFraud	Fraude detectada automaticamente
Instalação

Clone o repositório:

git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

Entre na pasta:

cd SEU-REPOSITORIO

Instale as dependências:

pip install -r requirements.txt
Executando o Projeto
Executar análise inicial
python src/main.py
Executar aumento artificial do dataset
python src/aumento_dataset.py
Executar versão sequencial
python src/sequencial.py
Executar versão paralela
python src/paralelo.py
Computação Paralela

O projeto utiliza multiprocessing para dividir o dataset em partes menores e processar múltiplas operações simultaneamente.

Objetivos da abordagem paralela:

Reduzir tempo de execução
Melhorar desempenho
Demonstrar conceitos de paralelismo
Comparar speedup entre versões
Métricas Avaliadas
Tempo de execução
Uso de CPU
Speedup
Eficiência paralela

Fórmula do speedup:

Speedup=
Tempo Paralelo
Tempo Sequencial
	​


Resultados Esperados
Processamento paralelo mais rápido que o sequencial
Melhor desempenho em datasets aumentados artificialmente
Visualização clara através de gráficos
Gráficos

O projeto gera gráficos comparando:

Tempo sequencial vs paralelo
Speedup
Volume de dados processados
Quantidade de fraudes detectadas
Possíveis Melhorias Futuras
Uso de Spark
Processamento distribuído
Dashboard interativo
Machine Learning para detecção de fraude
Execução em GPU
