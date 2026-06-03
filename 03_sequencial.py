import pandas as pd
import time

# ==================================
# Processamento de um chunk
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
# ==================================
def consolidar_resultados(resultados):
    total_geral  = sum(r['total']       for r in resultados)
    fraudes_geral = sum(r['fraudes']    for r in resultados)
    valor_geral  = sum(r['valor_total'] for r in resultados)

    return {
        'total'      : total_geral,
        'fraudes'    : fraudes_geral,
        'valor_total': valor_geral
    }

# ==================================
# Execução Serial
# ==================================
def executar_serial(arquivo, chunksize=1_000_000):
    resultados = []
    n_chunks   = 0

    inicio = time.time()
    for chunk in pd.read_csv(arquivo, chunksize=chunksize):
        resultado = processar_chunk(chunk)
        resultados.append(resultado)
        n_chunks += 1
    fim = time.time()

    resumo = consolidar_resultados(resultados)

    print("\n=== EXECUCAO SERIAL COMPLETA ===")
    print(f"Chunks processados : {n_chunks}")
    print(f"Tempo total        : {fim - inicio:.4f} segundos")

    print("\n=== RESULTADO CONSOLIDADO ===")
    print(f"Total de transacoes  : {resumo['total']:,}")
    print(f"Transacoes fraudulentas: {resumo['fraudes']:,}")
    print(f"Taxa de fraude       : {resumo['fraudes']/resumo['total']*100:.4f}%")
    print(f"Valor movimentado    : R$ {resumo['valor_total']:,.2f}")

    return fim - inicio

# ==================================
# Main
# ==================================
if __name__ == "__main__":
    arquivo = "paysim_grande.csv"

    print("=" * 45)
    print("  Analise Serial - Deteccao de Fraudes")
    print("  Dataset: PaySim1")
    print("=" * 45)

    tempo = executar_serial(arquivo)

    with open("tempo_sequencial.txt", "w") as f:
        f.write(str(tempo))

    print(f"\nTempo salvo em tempo_sequencial.txt")
