# Safe Transact 1.0 - Deteccao de Fraudes com Machine Learning

## Demo / Preview
  <img src="demo.gif" width="800" style="border-radius:15px; border:2px solid #30363d;" />

</p>Projeto para deteccao de fraudes financeiras com Python, Scikit-learn e Streamlit. Voltado para instituições financeiras focado em seguranca digital e IA aplicada.

## Visao Geral

O projeto tem tres partes principais:

- `Treinamento`: treino e salvamento do modelo de fraude.
- `streamlit_aprendendo`: interface web para upload de CSV e visualizacao dos resultados.

O modelo final usado na aplicacao e um `Pipeline` com:

- `StandardScaler`
- `RandomForestClassifier`

## Funcionalidades

- Treinamento supervisionado para classificacao de fraude (`Fraude = 0/1`).
- Predicao em lote via script Python.
- Dashboard em Streamlit com:
- tabela de previsoes,
- KPIs de suspeitas,
- multiplos graficos de analise,
- download do resultado em CSV.
- Leitura de CSV com separador automatico (`,` ou `;`).

## Dados Esperados para Inferencia

O modelo final espera exatamente estas colunas:

- `Valor`
- `Saldo_Anterior`
- `Mudanca_Dispositivo`
- `Horario`
- `Novo_Destino`

Exemplo de cabecalho CSV:

```csv
Valor,Saldo_Anterior,Mudanca_Dispositivo,Horario,Novo_Destino
```

## Como o Modelo Foi Treinado

Arquivo: `Treinamento/Treina_ai.py`

1. Leitura de `creditcard.csv`.
2. Definicao de `Fraude` como target.
3. Criacao de `sample_weight` com enfase em alto risco.
4. Split treino/teste (`test_size=0.2`, `stratify=y`, `random_state=42`).
5. Treino de `Pipeline(StandardScaler + RandomForestClassifier)`.
6. Avaliacao com `classification_report`.
7. Salvamento em `modelo_fraude_final.pkl`.
8. Export de importancia das features em `feature_importance_log.csv`.

## Requisitos

Python 3.10+ recomendado.
Instalacao rapida:
```bash
pip install pandas numpy scikit-learn matplotlib joblib streamlit streamlit-option-menu
```

## Como Executar interface web (Streamlit)
```bash
streamlit run app.py
```
No app, faca upload de um `.csv` com as colunas esperadas para obter as previsoes e os graficos.

## Observacoes Tecnicas
- O modelo serializado pode gerar aviso se a versao do `scikit-learn` de treino e diferente da versao de execucao.
- Para resultados mais consistentes em producao, mantenha a mesma versao usada no treinamento.

