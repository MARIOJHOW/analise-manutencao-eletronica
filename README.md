# 📊 Análise de Dados de Manutenção Eletrônica

## 🎯 Objetivo do Projeto
Analisar padrões de falhas em equipamentos de mobilidade urbana para otimizar processos de manutenção preventiva e reduzir custos operacionais.

## 📁 Estrutura do Projeto
```
projeto-manutencao/
│
├── dados_manutencao.csv              # Dataset com 500 registros de manutenção
├── analise_manutencao.py             # Script de análise exploratória
├── analise_manutencao_dashboard.png  # Dashboard com visualizações
└── README.md                         # Documentação do projeto
```

## 🔧 Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Cálculos numéricos
- **Matplotlib** - Visualizações
- **Seaborn** - Gráficos estatísticos

## 📊 Dataset
O dataset contém 500 registros de chamados de manutenção de janeiro/2023 a junho/2024:

**Colunas:**
- `ID_Chamado` - Identificador único
- `Data_Abertura` - Data/hora de abertura
- `Equipamento` - Tipo de equipamento (7 categorias)
- `Tipo_Falha` - Categoria da falha (7 tipos)
- `Prioridade` - Crítica, Alta, Média, Baixa
- `Tecnico_Responsavel` - Técnico alocado
- `Status` - Concluída ou Pendente
- `Data_Conclusao` - Data/hora de conclusão
- `Tempo_Resolucao_Horas` - Tempo para resolver
- `Custo_Estimado_R$` - Custo da manutenção
- `Peca_Trocada` - Sim/Não
- `Linha_Onibus` - Linha onde está o equipamento

## 🔍 Principais Análises Realizadas

### 1. Taxa de Conclusão por Equipamento
Identificação de equipamentos com menor performance em conclusão de chamados.

**Insight:** Display Digital DD-50 possui menor taxa (77.6%) e necessita revisão de processo.

### 2. Tipos de Falha Mais Frequentes
Análise de frequência de cada tipo de falha.

**Insight:** "Desgaste Mecânico" representa 17.8% dos chamados (89 ocorrências).

### 3. Tempo de Resolução por Prioridade
Análise de SLA (Service Level Agreement) por prioridade.

**Insight:** Chamados críticos resolvidos em 1.81h (dentro da meta de 3h).

### 4. Custo por Tipo de Falha
Identificação dos tipos de falha com maior impacto financeiro.

**Insight:** "Desgaste Mecânico" gera R$ 49.013 em custos totais.

### 5. Tendência Temporal
Análise de evolução de chamados ao longo do tempo.

**Insight:** Tendência estável (-3.8% de variação).

### 6. Performance dos Técnicos
Comparação de eficiência entre técnicos.

**Insight:** João Silva possui melhor tempo médio (11.8h).

## 📈 Resultados e Métricas

**Métricas Gerais:**
- Total de Chamados: 500
- Taxa de Conclusão: 79.2%
- Custo Total: R$ 294.162,00
- Tempo Médio de Resolução: 13.02 horas

## 💡 Recomendações

1. **Manutenção Preventiva:** Implementar programa focado em "Desgaste Mecânico"
2. **Investigação de Causa Raiz:** Analisar falhas específicas do Display Digital DD-50
3. **Treinamento:** Criar programa baseado nas melhores práticas de João Silva
4. **SLA:** Manter meta de 3h para chamados críticos
5. **Gestão de Estoque:** Otimizar peças para reduzir tempo de resolução

## 📊 Impacto Esperado

- ✅ Redução de **15%** no tempo de resposta com manutenção preventiva
- ✅ Economia estimada de **R$ 9.802,60** com prevenção de Desgaste Mecânico
- ✅ Melhoria de **10%** na disponibilidade de equipamentos

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install pandas numpy matplotlib seaborn
```

2. **Gerar o dataset:**
```bash
python gerar_dataset_manutencao.py
```

3. **Executar análise:**
```bash
python analise_manutencao.py
```

4. **Visualizar resultados:**
- Análise completa será exibida no terminal
- [Dashboard de Análise](./analise_manutencao_dashboard.png)
## 👤 Autor
**Mário Sérgio Inácio Júnior**
- LinkedIn: [Mário Sérgio Inácio Júnior](https://linkedin.com/in/mário-sérgio-inácio-júnior-026705149)
- Email: mariosergioijr@gmail.com

## 📝 Licença
Este projeto foi desenvolvido para fins educacionais e de portfólio.

---

*Projeto desenvolvido como parte da transição de carreira para Análise de Dados e Cloud Computing - Fevereiro 2026*
