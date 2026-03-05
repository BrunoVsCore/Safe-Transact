# ======================================
# Analise_de_Fraude.py - modulo reutilizavel + execucao direta
# ======================================

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

COLUNAS_ESPERADAS = [
    "Valor",
    "Saldo_Anterior",
    "Mudanca_Dispositivo",
    "Horario",
    "Novo_Destino",
]


def carregar_modelo(caminho_modelo=None):
    base_dir = Path(__file__).resolve().parent
    caminho = Path(caminho_modelo) if caminho_modelo else base_dir / "modelo_fraude_final.pkl"
    return joblib.load(caminho)


def preparar_entrada(df):
    faltando = [col for col in COLUNAS_ESPERADAS if col not in df.columns]
    if faltando:
        raise ValueError(
            f"Colunas obrigatorias ausentes: {faltando}. "
            f"Colunas recebidas: {list(df.columns)}"
        )
    return df[COLUNAS_ESPERADAS].copy()


def analisar_dataframe(df_entrada, modelo=None):
    modelo = modelo or carregar_modelo()
    df_novos = preparar_entrada(df_entrada)

    y_prob = modelo.predict_proba(df_novos)[:, 1]
    y_pred = (y_prob > 0.5).astype(int)

    df_resultado = df_novos.copy()
    df_resultado["Fraude_Predita"] = y_pred
    df_resultado["Probabilidade_Fraude"] = y_prob
    df_resultado["Fraude_Label"] = df_resultado["Fraude_Predita"].map({1: "Sim", 0: "Nao"})
    return df_resultado


def analisar_csv(caminho_csv, modelo=None):
    df = pd.read_csv(caminho_csv, sep=None, engine="python")
    return analisar_dataframe(df, modelo=modelo)


def exibir_grafico(df_resultado):
    contagem = df_resultado["Fraude_Label"].value_counts().reindex(["Sim", "Nao"], fill_value=0)
    plt.figure(figsize=(6, 4))
    contagem.plot(kind="bar", color=["red", "green"])
    plt.title("Contagem de Fraudes Detectadas")
    plt.ylabel("Numero de Transacoes")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def main():
    arquivo_csv = "novos_dados_teste.csv"
    modelo = carregar_modelo()
    print("Modelo carregado com sucesso.")

    df_resultado = analisar_csv(arquivo_csv, modelo=modelo)
    print(f"Arquivo carregado: {arquivo_csv}")
    print(f"Colunas usadas para previsao: {COLUNAS_ESPERADAS}")

    saida = "resultado_analise_fraude.csv"
    df_resultado.to_csv(saida, index=False)
    print(f"Resultados salvos em '{saida}'")

    exibir_grafico(df_resultado)
    print("Grafico de fraudes exibido.")


if __name__ == "__main__":
    main()
