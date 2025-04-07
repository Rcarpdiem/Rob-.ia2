
import streamlit as st
from modules import zimpa_ai, long_term_predictor, market_monitor

st.set_page_config(page_title="Robô Trader Zimba", layout="wide")

st.title("Robô Trader Zimba - Versão Beta")
if st.button("Ativar Robô Trader"):
    st.success("Robô ativado em modo simulação!")

st.sidebar.header("Painel Zimba")
st.sidebar.info(zimpa_ai.zimpa_welcome())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Análise de Longo Prazo")
    st.write(long_term_predictor.long_term_analysis())

with col2:
    st.subheader("Monitoramento de Mercado")
    st.write(market_monitor.market_status())
