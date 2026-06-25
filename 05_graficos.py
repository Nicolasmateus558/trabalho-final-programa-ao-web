import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

# ================================================
#  ETAPA 5 - Graficos de Desempenho
# ================================================

os.makedirs("graficos", exist_ok=True)

processos  = [1, 2, 4, 8, 12]
tempos     = [528.5361, 293.5872, 170.1957, 165.2813, 152.2672]
speedups   = [1.0000,   1.8003,   3.1055,   3.1978,   3.4711]
eficiencia = [1.0000,   0.9001,   0.7764,   0.3997,   0.2893]
speedup_ideal = processos  # linha ideal: 1x, 2x, 4x, 8x, 12x

COR_REAL  = '#2563EB'
COR_IDEAL = '#DC2626'

# ------------------------------------------------
# Grafico 1 — Tempo de Execucao
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(processos, tempos, marker='o', color=COR_REAL, linewidth=2.5,
        markersize=8, label='Tempo real')
ax.fill_between(processos, tempos, alpha=0.1, color=COR_REAL)
for x, y in zip(processos, tempos):
    ax.annotate(f'{y:.1f}s', (x, y), textcoords="offset points",
                xytext=(0, 10), ha='center', fontsize=9)
ax.set_xlabel('Número de Processos', fontsize=12)
ax.set_ylabel('Tempo de Execução (s)', fontsize=12)
ax.set_title('Tempo de Execução × Número de Processos\nPaySim1 — 100 milhões de transações', fontsize=13)
ax.set_xticks(processos)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
plt.tight_layout()
plt.savefig('graficos/01_tempo.png', dpi=150)
plt.close()
print("Grafico 1 salvo: graficos/01_tempo.png")

# ------------------------------------------------
# Grafico 2 — Speedup
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(processos, speedup_ideal, linestyle='--', color=COR_IDEAL,
        linewidth=1.8, label='Speedup ideal (linear)')
ax.plot(processos, speedups, marker='o', color=COR_REAL, linewidth=2.5,
        markersize=8, label='Speedup real')
for x, y in zip(processos, speedups):
    ax.annotate(f'{y:.2f}x', (x, y), textcoords="offset points",
                xytext=(0, 10), ha='center', fontsize=9)
ax.set_xlabel('Número de Processos', fontsize=12)
ax.set_ylabel('Speedup', fontsize=12)
ax.set_title('Speedup × Número de Processos\nPaySim1 — 100 milhões de transações', fontsize=13)
ax.set_xticks(processos)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
plt.tight_layout()
plt.savefig('graficos/02_speedup.png', dpi=150)
plt.close()
print("Grafico 2 salvo: graficos/02_speedup.png")

# ------------------------------------------------
# Grafico 3 — Eficiencia
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ef_pct = [e * 100 for e in eficiencia]
bars = ax.bar(processos, ef_pct, color=COR_REAL, alpha=0.8, width=0.8)
ax.axhline(y=100, linestyle='--', color=COR_IDEAL, linewidth=1.5, label='Eficiência ideal (100%)')
for bar, val in zip(bars, ef_pct):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{val:.1f}%', ha='center', fontsize=10, fontweight='bold')
ax.set_xlabel('Número de Processos', fontsize=12)
ax.set_ylabel('Eficiência (%)', fontsize=12)
ax.set_title('Eficiência Paralela × Número de Processos\nPaySim1 — 100 milhões de transações', fontsize=13)
ax.set_xticks(processos)
ax.set_ylim(0, 115)
ax.grid(True, linestyle='--', alpha=0.5, axis='y')
ax.legend()
plt.tight_layout()
plt.savefig('graficos/03_eficiencia.png', dpi=150)
plt.close()
print("Grafico 3 salvo: graficos/03_eficiencia.png")

print("\nTodos os graficos gerados na pasta 'graficos/'")
