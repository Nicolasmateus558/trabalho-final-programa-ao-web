import pandas as pd
import numpy as np
import time
import os

# ================================================
#  ETAPA 2 - Expansao do Dataset para ~15GB
# ================================================

MULTIPLICADOR = 32
ARQUIVO_SAIDA = "paysim_grande.csv"

print("=" * 60)
print("   ETAPA 2: Expandindo dataset para ~15GB")
print("=" * 60)

print("\nCarregando dataset original...")
df_original = pd.read_csv("paysim.csv")
print(f"Original: {len(df_original):,} linhas")
print(f"Gerando {MULTIPLICADOR} copias com variacao nos valores...")
print(f"Estimativa: ~{len(df_original) * MULTIPLICADOR:,} linhas no total\n")

inicio = time.time()

# Escreve a primeira copia com o header
df_original.to_csv(ARQUIVO_SAIDA, index=False)
tamanho_gb = os.path.getsize(ARQUIVO_SAIDA) / (1024 ** 3)
print(f"  Copia  1/{MULTIPLICADOR} gravada — {tamanho_gb:.2f} GB acumulado")

# Gera e grava cada copia diretamente no disco (evita estourar a memoria)
for i in range(1, MULTIPLICADOR):
    copia = df_original.copy()

    ruido = np.random.uniform(0.95, 1.05, size=len(copia))
    copia['amount']         = (copia['amount']         * ruido).round(2)

    ruido2 = np.random.uniform(0.95, 1.05, size=len(copia))
    copia['oldbalanceOrg']  = (copia['oldbalanceOrg']  * ruido2).round(2)
    copia['newbalanceOrig'] = (copia['newbalanceOrig'] * ruido2).round(2)

    ruido3 = np.random.uniform(0.95, 1.05, size=len(copia))
    copia['oldbalanceDest'] = (copia['oldbalanceDest'] * ruido3).round(2)
    copia['newbalanceDest'] = (copia['newbalanceDest'] * ruido3).round(2)

    copia['step'] = copia['step'] + (i * 744)

    copia.to_csv(ARQUIVO_SAIDA, mode='a', header=False, index=False)

    tamanho_gb = os.path.getsize(ARQUIVO_SAIDA) / (1024 ** 3)
    print(f"  Copia {i+1:>2}/{MULTIPLICADOR} gravada — {tamanho_gb:.2f} GB acumulado")

fim = time.time()
tamanho_final = os.path.getsize(ARQUIVO_SAIDA) / (1024 ** 3)
total_linhas  = len(df_original) * MULTIPLICADOR

print()
print("=" * 60)
print(f"   Concluido em {fim - inicio:.0f} segundos")
print(f"   Linhas totais : {total_linhas:,}")
print(f"   Tamanho final : {tamanho_final:.2f} GB")
print("=" * 60)
