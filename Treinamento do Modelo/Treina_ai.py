# ======================================
# Author: Bruno Irvayni
# Year: 2026
# Treina_ai.py - Treinamento + Importância das Features + Log
# ======================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import matplotlib.pyplot as plt


# 1️⃣ CARREGAR DADOS

CSV_PATH = "creditcard.csv" \
"" \
""
df = pd.read_csv(CSV_PATH)

# Coluna alvo
TARGET = "Fraude"
if TARGET not in df.columns:
    raise ValueError(f"❌ Coluna '{TARGET}' não encontrada no dataset.")

X = df.drop(columns=[TARGET])
y = df[TARGET]


# 2️⃣ DETECTAR COLUNA DE ÊNFASE

coluna_enfase = "Risco_Fraude" if "Risco_Fraude" in X.columns else X.select_dtypes(include=np.number).columns[0]
print(f"✅ Coluna de ênfase para sample_weight: {coluna_enfase}")

threshold = X[coluna_enfase].quantile(0.75)
weights = np.where(X[coluna_enfase] > threshold, 5.0, 1.0)


# 3️⃣ DIVIDIR TREINO / TESTE

X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(
    X, y, weights, test_size=0.2, random_state=42, stratify=y
)


# 4️⃣ PIPELINE COM SCALER + RANDOM FOREST

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=200, random_state=42))
])

pipeline.fit(X_train, y_train, clf__sample_weight=w_train)


# 5️⃣ AVALIAR MODELO

preds = pipeline.predict(X_test)
print("\n📊 Relatório de Classificação:")
print(classification_report(y_test, preds))


# 6️⃣ SALVAR MODELO

joblib.dump(pipeline, "modelo_fraude_final.pkl")
print("💾 Modelo salvo como 'modelo_fraude_final.pkl'")


# 7️⃣ IMPORTÂNCIA GLOBAL DAS FEATURES

try:
    feature_importances = pipeline.named_steps["clf"].feature_importances_
    feat_imp_series = pd.Series(feature_importances, index=X.columns)
    feat_imp_series = feat_imp_series.sort_values(ascending=True)

    # 🔹 Salvar em arquivo de log CSV
    feat_imp_series.to_csv("feature_importance_log.csv", header=["Importancia"])
    print("💾 Log de importância das features salvo como 'feature_importance_log.csv'")

    # 🔹 Gráfico de barras horizontal
    plt.figure(figsize=(8,6))
    feat_imp_series.plot(kind='barh', color='skyblue')
    plt.title("Importância das Features - RandomForest")
    plt.xlabel("Importância")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.show()
    print("✅ Gráfico de barras das features gerado.")
except Exception as e:
    print("\n⚠️ Não foi possível gerar gráfico ou log de importância:", e)
