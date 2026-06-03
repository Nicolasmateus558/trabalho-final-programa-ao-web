import pandas as pd
import multiprocessing
import time

# ==================================
# Processamento de um chunk
# (mesma funcao do serial)
# ==================================
def processar_chunk(chunk):
    total       = len(chunk)
    fraudes     = int(chunk['isFraud'].sum())
    valor_total = float(chunk['amount'].sum())

    por_tipo = {}
    for tipo, grupo in chunk.groupby('type'):
        por_tipo[tipo] = {
            'qtd'    : len(grupo),
            'fraudes': int(grupo['isFraud'].sum()),
            'valor'  : float(grupo['amount'].sum())
        }

    return {
        'total'      : total,
        'fraudes'    : fraudes,
        'valor_total': valor_total,
        'por_tipo'   : por_tipo
    }

# ==================================
# Consolidação dos resultados
# (mesma funcao do serial)
# ==================================
def consolidar_resultados(resultados):
    total_geral   = sum(r['total']       for r in resultados)
    fraudes_geral = sum(r['fraudes']     for r in resultados)
    valor_geral   = sum(r['valor_total'] for r in resultados)

    return {
        'total'      : total_geral,
        'fraudes'    : fraudes_geral,
        'valor_total': valor_geral
    }

# ==================================
# Execução Paralela
# ==================================
def executar_paralelo(arquivo, n_processos, chunksize=1_000_000):
    resultados = []
    n_chunks   = 0
    batch      = []

    inicio = time.time()

    with multiprocessing.Pool(processes=n_processos) as pool:
        for chunk in pd.read_csv(arquivo, chunksize=chunksize):
            batch.append(chunk)
            # quando acumula n_processos chunks, processa todos em paralelo
            if len(batch) == n_processos:
                resultados.extend(pool.map(processar_chunk, batch))
                n_chunks += len(batch)
                batch = []

        # processa os chunks restantes
        if batch:
            resultados.extend(pool.map(processar_chunk, batch))
            n_chunks += len(batch)

    fim = time.time()

    resumo = consolidar_resultados(resultados)

    print(f"\n=== EXECUCAO PARALELA ({n_processos} processos) ===")
    print(f"Chunks processados : {n_chunks}")
    print(f"Tempo total        : {fim - inicio:.4f} segundos")

    print("\n=== RESULTADO CONSOLIDADO ===")
    print(f"Total de transacoes    : {resumo['total']:,}")
    print(f"Transacoes fraudulentas: {resumo['fraudes']:,}")
    print(f"Taxa de fraude         : {resumo['fraudes']/resumo['total']*100:.4f}%")
    print(f"Valor movimentado      : R$ {resumo['valor_total']:,.2f}")

    return fim - inicio

# ==================================
# Main — benchmark 2, 4 e 8 processos
# ==================================
if __name__ == "__main__":
    arquivo        = "paysim_grande.csv"
    TEMPO_SERIAL   = 470.1181   # tempo do serial ja medido
    configuracoes  = [2, 4, 8]

    print("=" * 50)
    print("  Analise Paralela - Deteccao de Fraudes")
    print("  Dataset: PaySim1 (15GB)")
    print("=" * 50)

    tempos = {1: TEMPO_SERIAL}

    for n in configuracoes:
        print(f"\n{'='*50}")
        print(f"  Rodando com {n} processos...")
        print(f"{'='*50}")
        t = executar_paralelo(arquivo, n)
        tempos[n] = t

    # Relatorio final com speedup e eficiencia
    print("\n" + "=" * 50)
    print("  BENCHMARK COMPLETO")
    print("=" * 50)
    print(f"{'Processos':<12} {'Tempo (s)':<14} {'Speedup':<10} {'Eficiencia'}")
    print("-" * 50)
    for p in [1, 2, 4, 8]:
        t        = tempos[p]
        speedup  = TEMPO_SERIAL / t
        efic     = speedup / p
        print(f"{p:<12} {t:<14.4f} {speedup:<10.4f} {efic:.4f}")
    print("=" * 50)

    # Salva resultados para os graficos
    with open("resultados_benchmark.txt", "w") as f:
        for p in [1, 2, 4, 8]:
            f.write(f"{p},{tempos[p]}\n")

    print("\nResultados salvos em resultados_benchmark.txt")
