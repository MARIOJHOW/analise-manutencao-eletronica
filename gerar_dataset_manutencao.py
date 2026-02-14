import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurar seed para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Parâmetros
n_records = 500
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 6, 30)

# Dados base
equipamentos = ['Validador VA-2000', 'Validador VA-3000', 'Catraca CT-500', 'Catraca CT-700', 
                'Computador Bordo CB-100', 'Display Digital DD-50', 'Antena GPS AG-20']
tipos_falha = ['Falha de Leitura', 'Erro de Comunicação', 'Desgaste Mecânico', 
               'Falha Elétrica', 'Defeito de Software', 'Sensor Danificado', 'Conectividade']
prioridades = ['Baixa', 'Média', 'Alta', 'Crítica']
status = ['Concluída', 'Concluída', 'Concluída', 'Concluída', 'Pendente']  # 80% concluídas
tecnicos = ['João Silva', 'Maria Santos', 'Pedro Oliveira', 'Ana Costa', 'Mário Inácio']

# Gerar dados
data = []
for i in range(n_records):
    equipamento = random.choice(equipamentos)
    tipo_falha = random.choice(tipos_falha)
    prioridade = random.choice(prioridades)
    tecnico = random.choice(tecnicos)
    status_atual = random.choice(status)
    
    # Data de abertura
    data_abertura = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Tempo de resolução baseado na prioridade
    if status_atual == 'Concluída':
        if prioridade == 'Crítica':
            tempo_resolucao = random.randint(30, 180)  # minutos
        elif prioridade == 'Alta':
            tempo_resolucao = random.randint(120, 480)
        elif prioridade == 'Média':
            tempo_resolucao = random.randint(240, 1440)
        else:
            tempo_resolucao = random.randint(480, 2880)
        
        data_conclusao = data_abertura + timedelta(minutes=tempo_resolucao)
        tempo_resolucao_horas = round(tempo_resolucao / 60, 2)
    else:
        data_conclusao = None
        tempo_resolucao_horas = None
    
    # Custo estimado
    custo_base = {'Baixa': 150, 'Média': 300, 'Alta': 600, 'Crítica': 1200}
    custo = custo_base[prioridade] + random.randint(-50, 100)
    
    # Peça trocada (60% dos casos)
    peca_trocada = random.choice([True, False, False, True, True])
    
    data.append({
        'ID_Chamado': f'CH{str(i+1).zfill(5)}',
        'Data_Abertura': data_abertura.strftime('%Y-%m-%d %H:%M:%S'),
        'Equipamento': equipamento,
        'Tipo_Falha': tipo_falha,
        'Prioridade': prioridade,
        'Tecnico_Responsavel': tecnico,
        'Status': status_atual,
        'Data_Conclusao': data_conclusao.strftime('%Y-%m-%d %H:%M:%S') if data_conclusao else None,
        'Tempo_Resolucao_Horas': tempo_resolucao_horas,
        'Custo_Estimado_R$': custo,
        'Peca_Trocada': 'Sim' if peca_trocada else 'Não',
        'Linha_Onibus': random.choice(['Linha 100', 'Linha 200', 'Linha 300', 'Linha 400', 'Linha 500'])
    })

# Criar DataFrame
df = pd.DataFrame(data)

# Adicionar coluna de mês para análises
df['Mes_Abertura'] = pd.to_datetime(df['Data_Abertura']).dt.to_period('M').astype(str)

# Salvar
output_path = '/home/claude/dados_manutencao.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ Dataset criado com sucesso!")
print(f"📊 Total de registros: {len(df)}")
print(f"📁 Arquivo salvo em: {output_path}")
print("\n📈 Resumo dos dados:")
print(f"- Período: {df['Data_Abertura'].min()} a {df['Data_Abertura'].max()}")
print(f"- Equipamentos: {df['Equipamento'].nunique()} tipos")
print(f"- Chamados concluídos: {(df['Status'] == 'Concluída').sum()} ({(df['Status'] == 'Concluída').sum()/len(df)*100:.1f}%)")
print(f"- Custo total estimado: R$ {df['Custo_Estimado_R$'].sum():,.2f}")
