import pandas as pd
import numpy as np
import multiprocessing
import time

ARQUIVO    = "paysim_grande.csv"
CHUNKSIZE  = 1_000_000
MAX_CHUNKS = 100   # 100M transacoes — cabe na RAM com colunas selecionadas

# ==================================
# Processamento de um chunk
# (CPU-intensivo: z-score + loop de risco)
# ==================================
def processar_chunk(chunk):
    tipos_arr = chunk['type'].values
    amounts   = chunk['amount'].values
    is_fraud  = chunk['isFraud'].values

    total       = len(chunk)
    n_fraudes   = int(is_fraud.sum())
    valor_total = float(amounts.sum())

    # --- 1. Z-score por tipo (numpy) ---
    tipos_unicos = np.unique(tipos_arr)
    n_outliers = 0
    for tipo in tipos_unicos:
        mask = tipos_arr == tipo
        vals = amounts[mask]
        if len(vals) > 1:
            media  = np.mean(vals)
            desvio = np.std(vals)
            if desvio > 0:
                z = np.abs((vals - media) / desvio)
                n_outliers += int(np.sum(z > 3))

    # --- 2. Classificacao de risco por transacao (loop Python — CPU intensivo) ---
    alto = medio = baixo = suspeitas = 0
    for i in range(total):
        amt  = amounts[i]
        tipo = tipos_arr[i]
        if tipo in ('TRANSFER', 'CASH_OUT') and amt > 200_000:
            alto += 1
            if is_fraud[i] == 0:
                suspeitas += 1
        elif amt > 50_000:
            medio += 1
        else:
            baixo += 1

    return {
        'total'      : total,
        'fraudes'    : n_fraudes,
        'valor_total': valor_total,
        'n_outliers' : n_outliers,
        'risco_alto' : alto,
        'risco_medio': medio,
        'risco_baixo': baixo,
        'suspeitas'  : suspeitas,
    }

# ==================================
# Consolidacao dos resultados
# ==================================
def consolidar_resultados(resultados):
    return {
        'total'      : sum(r['total']       for r in resultados),
        'fraudes'    : sum(r['fraudes']     for r in resultados),
        'valor_total': sum(r['valor_total'] for r in resultados),
        'n_outliers' : sum(r['n_outliers']  for r in resultados),
        'risco_alto' : sum(r['risco_alto']  for r in resultados),
        'suspeitas'  : sum(r['suspeitas']   for r in resultados),
    }

# ==================================
# Main
# ==================================
if __name__ == '__main__':
    print("=" * 58)
    print("  Analise Paralela - Deteccao de Fraudes")
    print("  Dataset: PaySim1 (15GB) | multiprocessing.Pool")
    print("=" * 58)

    # --- Pre-carga (nao entra na medicao de tempo) ---
    print(f"\nCarregando {MAX_CHUNKS} chunks do dataset (pre-processamento)...")
    t_load = time.time()
    chunks = []
    for chunk in pd.read_csv(ARQUIVO, chunksize=CHUNKSIZE,
                             usecols=['type', 'amount', 'isFraud']):
        chunk['type'] = chunk['type'].astype('category')
        chunks.append(chunk)
        if len(chunks) >= MAX_CHUNKS:
            break
    t_load = time.time() - t_load
    total_tx = sum(len(c) for c in chunks)
    print(f"  {len(chunks)} chunks carregados em {t_load:.1f}s")
    print(f"  Total de transacoes em memoria: {total_tx:,}")

    # --- Benchmark ---
    tempos = {}
    configuracoes = [1, 2, 4, 8, 12]

    for n in configuracoes:
        print(f"\n  Rodando com {n} processo(s)...")
        t_ini = time.time()

        if n == 1:
            resultados = [processar_chunk(c) for c in chunks]
        else:
            with multiprocessing.Pool(processes=n) as pool:
                resultados = pool.map(processar_chunk, chunks)

        tempos[n] = time.time() - t_ini
        resumo = consolidar_resultados(resultados)
        print(f"  Tempo     : {tempos[n]:.4f} segundos")
        print(f"  Fraudes   : {resumo['fraudes']:,} | Outliers: {resumo['n_outliers']:,} | Suspeitas: {resumo['suspeitas']:,}")

    # --- Tabela final ---
    T1 = tempos[1]
    print("\n" + "=" * 58)
    print("  BENCHMARK COMPLETO")
    print("=" * 58)
    print(f"{'Processos':<12} {'Tempo (s)':<14} {'Speedup':<12} {'Eficiencia'}")
    print("-" * 58)
    for p in configuracoes:
        t       = tempos[p]
        speedup = T1 / t
        efic    = speedup / p
        print(f"{p:<12} {t:<14.4f} {speedup:<12.4f} {efic:.4f}")
    print("=" * 58)

    # Salva resultados para os graficos
    with open("resultados_benchmark.txt", "w") as f:
        f.write("processos,tempo,speedup,eficiencia\n")
        for p in configuracoes:
            speedup = T1 / tempos[p]
            efic    = speedup / p
            f.write(f"{p},{tempos[p]:.4f},{speedup:.4f},{efic:.4f}\n")

    print("\nResultados salvos em resultados_benchmark.txt")
    print("Proxima etapa: rodar 05_graficos.py para gerar os graficos")
