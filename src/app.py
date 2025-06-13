import streamlit as st

from devices.equipamento_de_monitoramento import EquipamentoDeMonitoramento
from observers.display_de_condicoes_atuais import DisplayDeCondicoesAtuais
from observers.display_estatistico import DisplayEstatistico
from subjects.monitor_de_dados_do_clima import MonitorDeDadosDoClima

# Inicializa o equipamento e o monitor de dados do clima
if "equipamento" not in st.session_state:
    st.session_state.equipamento = EquipamentoDeMonitoramento()
if "monitor_dados_clima" not in st.session_state:
    st.session_state.monitor_dados_clima = MonitorDeDadosDoClima(
        st.session_state.equipamento
    )
    st.session_state.equipamento.monitor_dados_clima = (
        st.session_state.monitor_dados_clima
    )

# Cria os displays
if "display_condicoes_atuais" not in st.session_state:
    st.session_state.display_condicoes_atuais = DisplayDeCondicoesAtuais()
if "display_estatistico" not in st.session_state:
    st.session_state.display_estatistico = DisplayEstatistico()

# Registra os displays como observadores
st.session_state.monitor_dados_clima.registra_observador(
    st.session_state.display_condicoes_atuais
)
st.session_state.monitor_dados_clima.registra_observador(
    st.session_state.display_estatistico
)


st.title("Padrão Observer")

with st.expander("📑 Sobre o projeto"):
    st.markdown(
        """
        Este projeto demonstra uma versão simples do padrão Observer
        utilizando Streamlit para interface gráfica.

        **Objetivo:**  
        Implementar displays que apresentam dados do clima obtidos do `EquipamentoDeMonitoramento`:

        - **DisplayDeCondicoesAtuais:** mostra temperatura, umidade e pressão atuais,
            além dos últimos 10 valores lidos.
        - **DisplayEstatistico:** apresenta temperatura e umidade médias,
            além das temperaturas máxima e mínima (últimas 10 atualizações).

        Os displays são observadores e podem ser 
        conectados/desconectados do publicador via botões abaixo.
        """
    )

st.button(
    "Coletar Dados",
    on_click=st.session_state.equipamento.coletar,
    help="Coleta dados do equipamento de monitoramento.",
)


col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("🌡️ Display Cond. Atuais")
    for x, leitura in enumerate(
        st.session_state.display_condicoes_atuais.todas_leituras()
    ):
        with st.container(border=True):
            st.markdown(f"Leitura {x}")
            c1, c2, c3 = st.columns(3)
            c1.metric("🌡️ Temperatura (°C)", leitura[0])
            c2.metric("💧 Umidade (%)", leitura[1])
            c3.metric("🧭 Pressão (hPa)", leitura[2])

with col2:
    st.subheader("📊 Display Estatístico")
    c1, c2 = st.columns(2)
    c1.metric(
        "🌡️ Temp. Média (°C)", st.session_state.display_estatistico.media_temperatura()
    )
    c2.metric(
        "💧 Umidade Média (%)", st.session_state.display_estatistico.media_humidade()
    )
    st.markdown("---")
    c3, c4 = st.columns(2)
    c3.metric(
        "⬆️ Temp. Máxima (°C)", st.session_state.display_estatistico.maxima_temperatura()
    )
    c4.metric(
        "⬇️ Temp. Mínima (°C)", st.session_state.display_estatistico.minima_temperatura()
    )
