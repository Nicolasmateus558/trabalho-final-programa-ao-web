import pandas as pd
import time

print("=" * 55)
print("  ETAPA 1: Carregando e explorando o dataset PaySim")
print("=" * 55)

print("\nCarregando o arquivo CSV...")
inicio = time.time()
df = pd.read_csv("paysim.csv")
fim = time.time()
print(f"Dataset carregado em {fim - inicio:.2f} segundos")

print("\nINFORMACOES GERAIS:")
print(f"  Linhas:   {df.shape[0]:,}")
print(f"  Colunas:  {df.shape[1]}")
tamanho_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)
print(f"  Tamanho em memoria: {tamanho_mb:.1f} MB")

print("\nPrimeiras 3 linhas:")
print(df.head(3).to_string())

print("\nTipos de dados:")
print(df.dtypes)

print("\nEstatisticas da coluna 'amount':")
print(f"  Minimo:  R$ {df['amount'].min():,.2f}")
print(f"  Maximo:  R$ {df['amount'].max():,.2f}")
print(f"  Media:   R$ {df['amount'].mean():,.2f}")
print(f"  Total movimentado: R$ {df['amount'].sum():,.2f}")

print("\nTipos de transacao e quantidade:")
print(df['type'].value_counts().to_string())

print("\nAnalise de Fraudes:")
total = len(df)
fraudes = df['isFraud'].sum()
legitimas = total - fraudes
print(f"  Total de transacoes:      {total:,}")
print(f"  Transacoes legitimas:     {legitimas:,}  ({legitimas/total*100:.3f}%)")
print(f"  Transacoes FRAUDULENTAS:  {fraudes:,}  ({fraudes/total*100:.3f}%)")

print("\nFraudes por tipo de transacao:")
fraudes_por_tipo = df.groupby('type')['isFraud'].agg(['sum', 'count'])
fraudes_por_tipo['percentual'] = fraudes_por_tipo['sum'] / fraudes_por_tipo['count'] * 100
fraudes_por_tipo.columns = ['Fraudes', 'Total', '% Fraude']
print(fraudes_por_tipo.to_string())

print("\n" + "=" * 55)
print("  Exploracao concluida!")
print("=" * 55)
