import streamlit as st

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


col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("🌡️ Display Cond. Atuais")

    with st.container(border=True):
        st.markdown("Leitura X")
        c1, c2, c3 = st.columns(3)
        c1.metric("🌡️ Temperatura (°C)", "--")
        c2.metric("💧 Umidade (%)", "--")
        c3.metric("🧭 Pressão (hPa)", "--")

with col2:
    st.subheader("📊 Display Estatístico")
    c1, c2 = st.columns(2)
    c1.metric("🌡️ Temp. Média (°C)", "--")
    c2.metric("💧 Umidade Média (%)", "--")
    st.markdown("---")
    c3, c4 = st.columns(2)
    c3.metric("⬆️ Temp. Máxima (°C)", "--")
    c4.metric("⬇️ Temp. Mínima (°C)", "--")
