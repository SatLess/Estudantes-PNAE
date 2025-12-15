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
    variacao_percentual_anual.append(variacao_percentual(alunos_por_ano,i - 1, i) * 100)

alunos_por_ano.insert(1, "Variação percentual", variacao_percentual_anual)
alunos_por_ano.loc[len(alunos_por_ano)] = ["Variação percentual total:", variacao_percentual(alunos_por_ano, 0, -1)]
alunos_por_ano.loc[len(alunos_por_ano)] = ["Média de alunos beneficiados por ano:", total_beneficiados/(qtd_anos - 1)]
alunos_por_ano.to_csv(OUTUPUT_PATH + "alunos_por_ano.csv")
#endregion

#region Alunos divididos por etapa escolar
etapa_escolar = tabela[["Ano", "Etapa_ensino", QTD_ALUNOS]]
alunos_fundamental = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "ENSINO FUNDAMENTAL"].groupby(["Etapa_ensino","Ano"]).sum()
alunos_fundamental.to_csv(OUTUPUT_PATH + "alunos_por_etapa_fundamental.csv")

alunos_medio = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "ENSINO MÉDIO"].groupby(["Etapa_ensino","Ano"]).sum()
alunos_medio.to_csv(OUTUPUT_PATH + "alunos_por_etapa_medio.csv")

alunos_eja = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "EDUCAÇÃO DE JOVENS E ADULTOS (EJA)"].groupby(["Etapa_ensino","Ano"]).sum()
alunos_eja.to_csv(OUTUPUT_PATH + "alunos_por_etapa_eja.csv")
#endregion


