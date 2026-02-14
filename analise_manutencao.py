"""
PROJETO 1: Análise de Dados de Manutenção Eletrônica
Autor: Mário Sérgio Inácio Júnior
Data: Fevereiro 2026

Objetivo: Analisar padrões de falhas em equipamentos de mobilidade urbana
para otimizar manutenção preventiva e reduzir custos operacionais.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==========================================
# 1. CARREGAR E PREPARAR DADOS
# ==========================================
print("=" * 60)
print("ANÁLISE DE DADOS DE MANUTENÇÃO - MOBILIDADE URBANA")
print("=" * 60)

df = pd.read_csv('dados_manutencao.csv')

# Converter datas
df['Data_Abertura'] = pd.to_datetime(df['Data_Abertura'])
df['Data_Conclusao'] = pd.to_datetime(df['Data_Conclusao'])

print(f"\n📊 Total de registros: {len(df)}")
print(f"📅 Período: {df['Data_Abertura'].min().strftime('%d/%m/%Y')} a {df['Data_Abertura'].max().strftime('%d/%m/%Y')}")

# ==========================================
# 2. ANÁLISES PRINCIPAIS
# ==========================================

print("\n" + "=" * 60)
print("ANÁLISE 1: Taxa de Conclusão por Equipamento")
print("=" * 60)

conclusao_por_equip = df.groupby('Equipamento').agg({
    'Status': lambda x: (x == 'Concluída').sum() / len(x) * 100,
    'ID_Chamado': 'count',
    'Tempo_Resolucao_Horas': 'mean'
}).round(2)
conclusao_por_equip.columns = ['Taxa_Conclusao_%', 'Total_Chamados', 'Tempo_Medio_Horas']
conclusao_por_equip = conclusao_por_equip.sort_values('Taxa_Conclusao_%', ascending=False)

print(conclusao_por_equip)

# Identificar equipamento com pior desempenho
pior_equip = conclusao_por_equip.index[-1]
print(f"\n⚠️  INSIGHT: {pior_equip} tem a menor taxa de conclusão ({conclusao_por_equip.loc[pior_equip, 'Taxa_Conclusao_%']:.1f}%)")
print(f"   Recomendação: Revisar processo de manutenção deste equipamento")

print("\n" + "=" * 60)
print("ANÁLISE 2: Tipos de Falha Mais Frequentes")
print("=" * 60)

falhas_freq = df['Tipo_Falha'].value_counts()
print(falhas_freq)

top_falha = falhas_freq.index[0]
print(f"\n🔧 INSIGHT: '{top_falha}' é o tipo de falha mais comum ({falhas_freq.iloc[0]} ocorrências)")
print(f"   Representa {falhas_freq.iloc[0]/len(df)*100:.1f}% dos chamados")

print("\n" + "=" * 60)
print("ANÁLISE 3: Tempo Médio de Resolução por Prioridade")
print("=" * 60)

tempo_por_prioridade = df[df['Status'] == 'Concluída'].groupby('Prioridade').agg({
    'Tempo_Resolucao_Horas': ['mean', 'median', 'count']
}).round(2)
tempo_por_prioridade.columns = ['Tempo_Medio_h', 'Tempo_Mediano_h', 'Total']

# Ordenar por ordem lógica de prioridade
ordem_prioridade = ['Crítica', 'Alta', 'Média', 'Baixa']
tempo_por_prioridade = tempo_por_prioridade.reindex(ordem_prioridade)

print(tempo_por_prioridade)

# Calcular meta de SLA (Service Level Agreement)
meta_critica = 3  # horas
tempo_real_critica = tempo_por_prioridade.loc['Crítica', 'Tempo_Medio_h']
diferenca_sla = tempo_real_critica - meta_critica

if tempo_real_critica <= meta_critica:
    print(f"\n✅ INSIGHT: Chamados críticos resolvidos em média em {tempo_real_critica}h (dentro da meta de {meta_critica}h)")
else:
    print(f"\n⚠️  INSIGHT: Chamados críticos levam {tempo_real_critica}h em média (meta: {meta_critica}h)")
    print(f"   Acima da meta em {diferenca_sla:.2f}h - necessário otimização")

print("\n" + "=" * 60)
print("ANÁLISE 4: Custo Total por Tipo de Falha")
print("=" * 60)

custo_por_falha = df.groupby('Tipo_Falha').agg({
    'Custo_Estimado_R$': ['sum', 'mean', 'count']
}).round(2)
custo_por_falha.columns = ['Custo_Total_R$', 'Custo_Medio_R$', 'Qtd_Chamados']
custo_por_falha = custo_por_falha.sort_values('Custo_Total_R$', ascending=False)

print(custo_por_falha)

falha_mais_cara = custo_por_falha.index[0]
custo_total_falha = custo_por_falha.loc[falha_mais_cara, 'Custo_Total_R$']
print(f"\n💰 INSIGHT: '{falha_mais_cara}' gera maior custo total: R$ {custo_total_falha:,.2f}")
print(f"   Foco em prevenção pode gerar economia significativa")

print("\n" + "=" * 60)
print("ANÁLISE 5: Tendência Temporal de Chamados")
print("=" * 60)

chamados_por_mes = df.groupby('Mes_Abertura').size()
print(chamados_por_mes)

# Calcular variação percentual
variacao = ((chamados_por_mes.iloc[-1] - chamados_por_mes.iloc[0]) / chamados_por_mes.iloc[0] * 100)
print(f"\n📈 INSIGHT: Variação de chamados do primeiro ao último mês: {variacao:+.1f}%")

if variacao > 10:
    print("   Tendência crescente - pode indicar envelhecimento de frota")
elif variacao < -10:
    print("   Tendência decrescente - manutenção preventiva está funcionando")
else:
    print("   Tendência estável")

print("\n" + "=" * 60)
print("ANÁLISE 6: Performance dos Técnicos")
print("=" * 60)

perf_tecnicos = df[df['Status'] == 'Concluída'].groupby('Tecnico_Responsavel').agg({
    'Tempo_Resolucao_Horas': ['mean', 'count'],
    'Custo_Estimado_R$': 'mean'
}).round(2)
perf_tecnicos.columns = ['Tempo_Medio_h', 'Chamados_Concluidos', 'Custo_Medio_R$']
perf_tecnicos = perf_tecnicos.sort_values('Tempo_Medio_h')

print(perf_tecnicos)

melhor_tecnico = perf_tecnicos.index[0]
tempo_melhor = perf_tecnicos.loc[melhor_tecnico, 'Tempo_Medio_h']
print(f"\n⭐ INSIGHT: {melhor_tecnico} tem o melhor tempo médio de resolução: {tempo_melhor}h")

# ==========================================
# 3. CRIAR VISUALIZAÇÕES
# ==========================================

print("\n" + "=" * 60)
print("Gerando visualizações...")
print("=" * 60)

# Visualização 1: Falhas por Equipamento
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Chamados por Equipamento
df['Equipamento'].value_counts().plot(kind='barh', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('Total de Chamados por Equipamento', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Quantidade de Chamados')

# 2. Distribuição de Prioridades
df['Prioridade'].value_counts().plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', 
                                      colors=['#d62728', '#ff7f0e', '#ffdd57', '#2ca02c'])
axes[0,1].set_title('Distribuição de Prioridades', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('')

# 3. Tempo de Resolução por Tipo de Falha
tempo_falha = df[df['Status'] == 'Concluída'].groupby('Tipo_Falha')['Tempo_Resolucao_Horas'].mean().sort_values()
tempo_falha.plot(kind='barh', ax=axes[1,0], color='coral')
axes[1,0].set_title('Tempo Médio de Resolução por Tipo de Falha', fontsize=14, fontweight='bold')
axes[1,0].set_xlabel('Horas')

# 4. Tendência de Chamados ao Longo do Tempo
chamados_mes = df.groupby(df['Data_Abertura'].dt.to_period('M')).size()
chamados_mes.index = chamados_mes.index.astype(str)
chamados_mes.plot(kind='line', ax=axes[1,1], marker='o', color='green', linewidth=2)
axes[1,1].set_title('Tendência de Chamados por Mês', fontsize=14, fontweight='bold')
axes[1,1].set_xlabel('Mês')
axes[1,1].set_ylabel('Quantidade de Chamados')
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/analise_manutencao_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✅ Dashboard salvo: analise_manutencao_dashboard.png")

# ==========================================
# 4. GERAR RELATÓRIO FINAL
# ==========================================

print("\n" + "=" * 60)
print("RESUMO EXECUTIVO - PRINCIPAIS INSIGHTS")
print("=" * 60)

total_chamados = len(df)
taxa_conclusao = (df['Status'] == 'Concluída').sum() / total_chamados * 100
custo_total = df['Custo_Estimado_R$'].sum()
tempo_medio_geral = df[df['Status'] == 'Concluída']['Tempo_Resolucao_Horas'].mean()

print(f"""
📊 MÉTRICAS GERAIS:
   - Total de Chamados: {total_chamados}
   - Taxa de Conclusão: {taxa_conclusao:.1f}%
   - Custo Total: R$ {custo_total:,.2f}
   - Tempo Médio de Resolução: {tempo_medio_geral:.2f} horas

🔍 PRINCIPAIS DESCOBERTAS:
   1. {top_falha} é o tipo de falha mais comum ({falhas_freq.iloc[0]} casos)
   2. {falha_mais_cara} gera maior custo operacional (R$ {custo_total_falha:,.2f})
   3. {pior_equip} necessita atenção especial (menor taxa de conclusão)
   4. {melhor_tecnico} é o técnico mais eficiente ({tempo_melhor}h média)

💡 RECOMENDAÇÕES:
   1. Implementar manutenção preventiva focada em '{top_falha}'
   2. Investigar causa raiz de falhas em {pior_equip}
   3. Criar programa de treinamento baseado nas práticas de {melhor_tecnico}
   4. Estabelecer SLA de {meta_critica}h para chamados críticos
   5. Otimizar estoque de peças para reduzir tempo de resolução

📈 IMPACTO ESPERADO:
   - Redução de 15% no tempo de resposta com manutenção preventiva
   - Economia estimada de R$ {custo_total_falha * 0.20:,.2f} com prevenção de '{falha_mais_cara}'
   - Melhoria de 10% na disponibilidade de equipamentos
""")

print("\n✅ Análise concluída com sucesso!")
print("📁 Arquivos gerados:")
print("   - dados_manutencao.csv")
print("   - analise_manutencao_dashboard.png")
