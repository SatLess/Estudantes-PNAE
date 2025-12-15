import pandas as pd

tabela = pd.read_csv("ALUNOS ATENDIDOS PELO PNAE.csv")
QTD_ALUNOS = "Qt_alunos_pnae"
OUTUPUT_PATH = "resultados/"

def variacao_percentual(table, idx_inicial, idx_final):
    return (table.iloc[idx_final][QTD_ALUNOS] - table.iloc[idx_inicial][QTD_ALUNOS]) / table.iloc[idx_inicial][QTD_ALUNOS]
    
#region Quantidade de alunos por ano
alunos_por_ano = tabela[["Ano", QTD_ALUNOS]].groupby("Ano").sum()
total_beneficiados = tabela[[QTD_ALUNOS]].sum().iloc[0]
qtd_anos = len(alunos_por_ano)

variacao_percentual_anual = [0.0]
for i in range(1, qtd_anos):
    variacao_percentual_anual.append(round(variacao_percentual(alunos_por_ano,i - 1, i), 4))

alunos_por_ano.insert(1, "Variação percentual", variacao_percentual_anual)
alunos_por_ano.to_csv(OUTUPUT_PATH + "alunos_por_ano.csv")
#endregion

#region Alunos divididos por etapa escolar
etapa_escolar = tabela[["Ano", "Etapa_ensino", QTD_ALUNOS]].groupby(["Etapa_ensino","Ano"]).sum()
etapa_escolar.to_csv(OUTUPUT_PATH + "aluno_por_etapa_escolar.csv")
#endregion


