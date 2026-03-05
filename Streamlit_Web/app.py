# =========================================================
# Safe Transact
# Fraud Detection System with Machine Learning & XAI
# ---------------------------------------------------------
# Author: Bruno Irvayni
# Year: 2026
# Description: Sistema de detecção de fraudes utilizando
# modelos de Machine Learning com explicabilidade (XAI).
# =========================================================


import streamlit as st
import json
import streamlit.components.v1 as components
import base64
from streamlit_option_menu import option_menu
from pathlib import Path

base_dir = Path(__file__).resolve().parent
# Remove A barra de deploy automatica
st.markdown("""
<style>
    header {visibility: hidden;}
    .stToolbar {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)
# ---- CSS para mudar a cor da sidebar ----
st.markdown("""
<style>
[data-testid="stSidebar"] {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
    border-right: 1px solid rgba(46,122,49,0.4);
    box-shadow: 0 0 12px rgba(46,122,49,0.25);
    background: rgba(15,23,42,0.85);
    border-right: 1.5px solid;
    border-image: linear-gradient(
        to bottom,
        #2e7a31,
        #00c6ff,
        transparent
    ) 1;
}
</style>
""", unsafe_allow_html=True)
# --------- Inicializa a pÃ¡gina ----------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Pagina Principal"
# ---------- CSS aprimorado para fundo totalmente transparente ----------
st.markdown("""
    <style>
        /* Fundo geral */
        .stApp {
            background: linear-gradient(135deg,#0f2a1b00 , #0f172a90, #40869a2a);
        }

        /* Ãrea central */
        .block-container {
            background-color: transparent !important;
            color: white !important;
            padding: 2rem;
            "border": "1px solid rgba(0,255,170,0.15)",
        }

        /* Texto branco */
        h1, h2, h3, h4, h5, h6, p, div, label, span, section, .stMarkdown {
            color: white !important;
        }

        /* Labels de input */
        .stTextInput > label, .stTextArea > label, .stSelectbox > label {
            color: white !important;
        
        .block-container {
    max-width: 1200px !important;
    padding-left: 0 !important;
    padding-right: 2rem !important;
    margin-left: -2rem !important;  /* Desloca mais ainda para esquerda */
}

        }
    </style>
""", unsafe_allow_html=True)
# ---------- BARRA LATERAL ----------
with st.sidebar:  
    st.sidebar.image(str(base_dir / "logo_circular.png"), width=400 )
    
# ---------- ESTILO GLOBAL HIGH-TECH Fundo-Sidebar ----------
st.markdown("""
<style>

/* FUNDO SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(10,15,28,0.9);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-right: 1px solid rgba(0,255,170,0.15);
    box-shadow:
        inset -1px 0 rgba(255,255,255,0.03),
        0 0 30px rgba(0,255,170,0.08);
    
            
}
/* TÍTULO MENU */
h1 {
    font-size: 20px !important;
    letter-spacing: 1px;
    color: #00ffaa;
}
</style>
""", unsafe_allow_html=True)

# ---------- BARRA LATERAL ----------
with st.sidebar:

    st.markdown("<h1>🛡 SYSTEM CONTROL</h1>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Pagina Principal", "Sobre"],
        icons=["house-door-fill", "info-circle-fill"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
               "padding": "0!important",
               "border-color": "00ffaa",
               "border-width": "1px",
               "border-style": "solid",
                                
               

            },
            "icon": {
                "color": "#00ffaa",
                "font-size": "18px",
            },
            #Com o link selecionado
            "nav-link-selected": {
                "background": "rgba(46, 176, 133, 0.4)",
                "border-left": "3px solid rgba(0,255,170,0.4)",
                
                "color": "#ffffff",
                "font-weight": "600",
                "box-shadow": "0 0 12px rgba(0,255,170,0.4)",
            },

        }
    )
   
#Funcao que abre a pagina clickada
if selected == "Pagina Principal":
    st.session_state.pagina = "Pagina Principal"
if selected == "Sobre":
    st.session_state.pagina = "Sobre"


# ---------- ÃREA PRINCIPAL ----------
if st.session_state.pagina == "Sobre":
    st.markdown("""
<h2 style="
    text-align: left; 
    font-weight: bold;
    margin-bottom: -10px;
">
Sobre o Safe Transact
</h2>
<hr style="margin-top:0px; border:1px solid rgba(0,255,170,0.2);">

<div style="
    margin-top: -5px;
    text-align:center;
    padding:0px;
    font-size:14px;
    color: rgba(0,255,170,0.6);
">
""", unsafe_allow_html=True)
    


    #Text
    st.markdown("""
O Safe Transact é um sistema inteligente de detecção de fraudes em transações financeiras baseado em Machine Learning.

O projeto foi desenvolvido para identificar padrões anômalos em transações de cartão de crédito, utilizando modelos supervisionados treinados com dados reais.

🔎 Tecnologias e Métodos Utilizados

- Python
- Scikit-learn
- Random Forest
- XGBoost
- SMOTE (balanceamento de dados)
- Análise exploratória e métricas como Recall e F1-Score
                
🎯 Objetivo do Projeto
Detectar fraudes com alta taxa de recall, minimizando falsos negativos — priorizando a segurança financeira.

🚀 Diferencial

O modelo não apenas classifica transações como fraude ou não fraude, mas também oferece explicabilidade através de técnicas de Explainable AI, permitindo entender quais variáveis influenciaram a decisão do modelo.
""", unsafe_allow_html=True)


    st.markdown("""
👨‍💻 Desenvolvido por
Bruno — Especialista em Inteligência Artificial e Machine Learning, com foco em segurança digital e soluções baseadas em dados.
- https://github.com/BrunoVsCore 
- https://www.linkedin.com/in/brunoirvayni/
""", unsafe_allow_html=True)


elif st.session_state.pagina == "Pagina Principal":
    
    #importa animacao
    def carregar_lottie(caminho):
        with open(caminho, "r") as arquivo:
            return json.load(arquivo)

    animacao_fraude = carregar_lottie(base_dir / "fraude.json")
    animacao_json_b64 = base64.b64encode(json.dumps(animacao_fraude).encode('utf-8')).decode('utf-8')

    col1, col2 = st.columns([2, 1])
    with col1:

        st.markdown("""
            <h1 style='
                color: #FFFFFF;
                font-size: 44px;
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                margin-bottom: 10px;
            '>
                Bem-vindo ao Safe 
                    Transact
            </h1>
            <p style='
                color: #F0F3F4;
                font-size: 20px;
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
            '>
                Detecte fraudes em suas transações com rapidez e precisão, protegendo seu dinheiro e sua tranquilidade
.
            </p>
        """, unsafe_allow_html=True)
    #Transparencia da animacao
    with col2:

        html_code = f"""
        <html>
          <head>
            <style>
            
              body {{
                margin: 0;
                background:"transparent;
              }}
              #lottie {{
                width: 200px;
                height: 250px;
                margin: auto;
              }}
            </style>
          </head>
          <body>
            <lottie-player id="lottie" 
                           autoplay 
                           loop 
                           mode="normal" 
                           background="transparent"
                           src="data:application/json;base64,{animacao_json_b64}"></lottie-player>

            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
          </body>
        </html>
        """
        components.html(html_code, height=350)

    # Sistema AI (usa o modulo de analise ja existente)
    import pandas as pd
    import sys
    import matplotlib.pyplot as plt

    pasta_analise = base_dir / "modelo"
    if str(pasta_analise) not in sys.path:
        sys.path.append(str(pasta_analise))

    from Analise_de_Fraude import analisar_dataframe

    # Interface do Streamlit
    st.write("Envie um arquivo `.csv` com suas transações para verificar possíveis fraudes.")

    arquivo = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

    if arquivo is not None:
        df_usuario = pd.read_csv(arquivo, sep=None, engine="python")

        st.write("Pre-visualizacao do arquivo:")
        st.dataframe(df_usuario.head())

        try:
            df_resultado = analisar_dataframe(df_usuario.copy())
            st.subheader("Resultado das Previsões:")
            st.dataframe(df_resultado)

            # KPIs
            total = int(len(df_resultado))
            total_fraudes = int((df_resultado["Fraude_Predita"] == 1).sum())
            taxa_fraude = (total_fraudes / total * 100) if total else 0.0
            prob_media = float(df_resultado["Probabilidade_Fraude"].mean()) if total else 0.0

            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric("Total", f"{total}")
            kpi2.metric("Suspeitas", f"{total_fraudes}")
            kpi3.metric("Taxa suspeita", f"{taxa_fraude:.2f}%")
            kpi4.metric("Prob media", f"{prob_media:.3f}")

            st.subheader("Graficos")

            # Linha 1: Contagem + Distribuicao de probabilidades
            col_graf1, col_graf2 = st.columns(2)

            contagem = (
                df_resultado["Fraude_Label"]
                .value_counts()
                .reindex(["Sim", "Nao"], fill_value=0)
            )
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            ax1.bar(contagem.index, contagem.values, color=["#d62728", "#2ca02c"])
            ax1.set_title("Contagem de Fraudes")
            ax1.set_ylabel("Numero de transacoes")
            col_graf1.pyplot(fig1)
            plt.close(fig1)

            fig2, ax2 = plt.subplots(figsize=(6, 3))
            ax2.hist(df_resultado["Probabilidade_Fraude"], bins=20, color="#1f77b4")
            ax2.set_title("Distribuicao da Probabilidade de Fraude")
            ax2.set_xlabel("Probabilidade")
            ax2.set_ylabel("Frequencia")
            col_graf2.pyplot(fig2)
            plt.close(fig2)

            # Linha 2: Top suspeitas + Dispersao Valor x Probabilidade
            col_graf3, col_graf4 = st.columns(2)

            top_n = min(10, len(df_resultado))
            top_suspeitas = df_resultado.nlargest(top_n, "Probabilidade_Fraude").copy()
            top_suspeitas = top_suspeitas.sort_values("Probabilidade_Fraude", ascending=True)
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            ax3.barh(
                [f"Linha {i}" for i in top_suspeitas.index],
                top_suspeitas["Probabilidade_Fraude"],
                color="#ff7f0e",
            )
            ax3.set_title("Top Transacoes Suspeitas")
            ax3.set_xlabel("Probabilidade de fraude")
            col_graf3.pyplot(fig3)
            plt.close(fig3)

            fig4, ax4 = plt.subplots(figsize=(6, 4))
            cores = df_resultado["Fraude_Predita"].map({1: "#d62728", 0: "#2ca02c"})
            ax4.scatter(df_resultado["Valor"], df_resultado["Probabilidade_Fraude"], c=cores, alpha=0.7)
            ax4.set_title("Valor x Probabilidade de Fraude")
            ax4.set_xlabel("Valor")
            ax4.set_ylabel("Probabilidade")
            col_graf4.pyplot(fig4)
            plt.close(fig4)

            # Linha 3: Heatmap Horario x Mudanca + Taxa por faixa de valor
            col_graf5, col_graf6 = st.columns(2)

            tabela_heat = pd.pivot_table(
                df_resultado,
                index="Horario",
                columns="Mudanca_Dispositivo",
                values="Probabilidade_Fraude",
                aggfunc="mean",
                fill_value=0,
            )
            fig5, ax5 = plt.subplots(figsize=(6, 4))
            heat = ax5.imshow(tabela_heat.values, aspect="auto", cmap="YlOrRd")
            ax5.set_title("Risco Medio por Horario x Mudanca")
            ax5.set_xticks(range(len(tabela_heat.columns)))
            ax5.set_xticklabels([str(c) for c in tabela_heat.columns])
            ax5.set_yticks(range(len(tabela_heat.index)))
            ax5.set_yticklabels([str(i) for i in tabela_heat.index])
            ax5.set_xlabel("Mudanca_Dispositivo")
            ax5.set_ylabel("Horario")
            fig5.colorbar(heat, ax=ax5, fraction=0.046, pad=0.04)
            col_graf5.pyplot(fig5)
            plt.close(fig5)

            df_faixa = df_resultado.copy()
            faixas = pd.cut(df_faixa["Valor"], bins=5, include_lowest=True)
            taxa_por_faixa = (
                df_faixa.assign(Faixa_Valor=faixas)
                .groupby("Faixa_Valor", observed=False)["Fraude_Predita"]
                .mean()
                .mul(100)
            )
            fig6, ax6 = plt.subplots(figsize=(6, 4))
            ax6.plot(range(len(taxa_por_faixa)), taxa_por_faixa.values, marker="o", color="#9467bd")
            ax6.set_title("Taxa de Fraude por Faixa de Valor")
            ax6.set_ylabel("Taxa (%)")
            ax6.set_xticks(range(len(taxa_por_faixa)))
            ax6.set_xticklabels([str(idx) for idx in taxa_por_faixa.index], rotation=25, ha="right")
            col_graf6.pyplot(fig6)
            plt.close(fig6)

            # Linha 4: Boxplot por Novo_Destino + Correlacao
            col_graf7, col_graf8 = st.columns(2)

            grupos_box = [
                df_resultado.loc[df_resultado["Novo_Destino"] == 0, "Probabilidade_Fraude"].values,
                df_resultado.loc[df_resultado["Novo_Destino"] == 1, "Probabilidade_Fraude"].values,
            ]
            fig7, ax7 = plt.subplots(figsize=(6, 4))
            ax7.boxplot(grupos_box, labels=["Destino 0", "Destino 1"], patch_artist=True)
            ax7.set_title("Probabilidade por Novo_Destino")
            ax7.set_ylabel("Probabilidade de fraude")
            col_graf7.pyplot(fig7)
            plt.close(fig7)

            corr_cols = ["Valor", "Saldo_Anterior", "Mudanca_Dispositivo", "Horario", "Novo_Destino", "Probabilidade_Fraude"]
            corr = df_resultado[corr_cols].corr(numeric_only=True).fillna(0)
            fig8, ax8 = plt.subplots(figsize=(6, 4))
            hm = ax8.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
            ax8.set_title("Matriz de Correlacao")
            ax8.set_xticks(range(len(corr.columns)))
            ax8.set_xticklabels(corr.columns, rotation=45, ha="right")
            ax8.set_yticks(range(len(corr.index)))
            ax8.set_yticklabels(corr.index)
            fig8.colorbar(hm, ax=ax8, fraction=0.046, pad=0.04)
            col_graf8.pyplot(fig8)
            plt.close(fig8)

            # Linha 5: Curva cumulativa de risco
            st.subheader("Curva Cumulativa de Risco")
            probs_ordenadas = df_resultado["Probabilidade_Fraude"].sort_values(ascending=False).reset_index(drop=True)
            risco_cumulativo = probs_ordenadas.cumsum() / probs_ordenadas.sum() if probs_ordenadas.sum() > 0 else probs_ordenadas
            fig9, ax9 = plt.subplots(figsize=(8, 3))
            ax9.plot(
                range(1, len(risco_cumulativo) + 1),
                risco_cumulativo.values,
                color="#17becf",
                linewidth=2,
            )
            ax9.set_title("Concentracao de Risco no Ranking")
            ax9.set_xlabel("Top transacoes ordenadas por risco")
            ax9.set_ylabel("Risco acumulado")
            ax9.set_ylim(0, 1.05)
            st.pyplot(fig9)
            plt.close(fig9)

            csv_resultado = df_resultado.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Baixar resultado como CSV",
                data=csv_resultado,
                file_name="resultado_fraude.csv",
                mime="text/csv",
            )
        except Exception as erro:
            st.error(f"Erro ao analisar o arquivo: {erro}")
#RODAPÉ
st.markdown("""
<hr style="margin-top:50px; border:1px solid rgba(0,255,170,0.2);">

<div style="
    text-align:center;
    padding:20px 0;
    font-size:14px;
    color: rgba(0,255,170,0.6);
">
© 2026 Bruno Irvayni Dev • Safe Transact <br>
Machine Learning & Explainable AI
</div>
""", unsafe_allow_html=True)
        
