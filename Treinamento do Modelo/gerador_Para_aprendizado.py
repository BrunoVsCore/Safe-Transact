import pandas as pd
import numpy as np

np.random.seed(42)

num_transacoes = 5000
num_fraudes = num_transacoes // 2
num_normais = num_transacoes - num_fraudes

def gerar_transacoes(n, fraude=False):
    valor = np.round(np.random.uniform(10, 10000, n), 2)
    saldo_anterior = np.round(valor + np.random.uniform(100, 20000, n), 2)

    if fraude:
        horario = np.random.choice(list(range(22,24)) + list(range(0,7)), n)
        return pd.DataFrame({
            "Valor": valor,
            "Saldo_Anterior": saldo_anterior,
            "Mudanca_Dispositivo": np.random.choice([0, 1], n, p=[0.3, 0.7]),
            "Horario": horario,
            "Novo_Destino": np.random.choice([0, 1], n, p=[0.3, 0.7]),
            "Fraude": 1
        })
    else:
        horario = np.random.choice(list(range(8,21)), n)
        return pd.DataFrame({
            "Valor": valor,
            "Saldo_Anterior": saldo_anterior,
            "Mudanca_Dispositivo": np.random.choice([0, 1], n, p=[0.9, 0.1]),
            "Horario": horario,
            "Novo_Destino": np.random.choice([0, 1], n, p=[0.9, 0.1]),
            "Fraude": 0
        })

# Gerar fraudes e não fraudes
df_fraudes = gerar_transacoes(num_fraudes, fraude=True)
df_normais = gerar_transacoes(num_normais, fraude=False)

# Concatenar e embaralhar
df = pd.concat([df_fraudes, df_normais]).sample(frac=1).reset_index(drop=True)

# Salvar CSV (apenas as features + Fraude como target)
df.to_csv("transacoes_treinamento_final.csv", index=False)
print("✅ CSV gerado: transacoes_treinamento_final.csv")
