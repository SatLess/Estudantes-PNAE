from IPython.display import display
import pandas as pd

tabela = pd.read_csv("ALUNOS ATENDIDOS PELO PNAE.csv")


def variacao_percentual(table, idx_inicial, idx_final):
    return (table.iloc[idx_final]["Qt_alunos_pnae"] - table.iloc[idx_inicial]["Qt_alunos_pnae"]) / table.iloc[idx_inicial]["Qt_alunos_pnae"]
    
###########################
alunos_por_ano = tabela[["Ano", "Qt_alunos_pnae"]].groupby("Ano").sum()
total_beneficiarios = tabela[["Qt_alunos_pnae"]].sum().iloc[0]
qtd_anos = len(alunos_por_ano) - 1

variacao_entre_anos = [100]
for i in range(1, qtd_anos + 1):
    variacao_entre_anos.append(variacao_percentual(alunos_por_ano,i - 1, i) * 100)

alunos_por_ano.insert(1, "Variação percentual", variacao_entre_anos)

print(alunos_por_ano)
print("Variação percentual total: " + str(variacao_percentual(alunos_por_ano, 0, -1)))
print("Média de alunos beneficiados por ano: " + str(total_beneficiarios/qtd_anos))
###########################

etapa_escolar = tabela[["Ano", "Etapa_ensino", "Qt_alunos_pnae"]]
alunos_fundamental = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "ENSINO FUNDAMENTAL"].groupby(["Etapa_ensino","Ano"]).sum()
alunos_medio = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "ENSINO MÉDIO"].groupby(["Etapa_ensino","Ano"]).sum()
alunos_eja = etapa_escolar.loc[etapa_escolar["Etapa_ensino"] == "EDUCAÇÃO DE JOVENS E ADULTOS (EJA)"].groupby(["Etapa_ensino","Ano"]).sum()

print("Variação fundamental percentual total: " + str(variacao_percentual(alunos_fundamental, 0, -1)))
print("Variação medio percentual total: " + str(variacao_percentual(alunos_medio, 0, -1)))
print("Variação eja percentual total: " + str(variacao_percentual(alunos_eja, 0, -1)))



