import streamlit as st
from chatbot_ia import responder_pergunta
from faq_data import faq_data

st.set_page_config(page_title="Chatbot da Loja", page_icon="🛠️")

st.title("🧱 Chatbot da Loja de Materiais de Construção")

# Inicializa a conversa na sessão
if "historico" not in st.session_state:
    st.session_state.historico = []

# Entrada do usuário
pergunta_usuario = st.text_input("Digite sua pergunta:")

if st.button("Enviar") and pergunta_usuario:
    resposta = responder_pergunta(pergunta_usuario)
    st.session_state.historico.append({
        "pergunta": pergunta_usuario,
        "resposta": resposta
    })

# Exibe o histórico com avatares
if st.session_state.historico:
    st.subheader("💬 Conversa:")
    for item in st.session_state.historico:
        st.markdown(f"""
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='margin-right: 10px;'>🧑‍💼</div>
            <div style='background-color: #f0f2f6; padding: 10px; border-radius: 10px; max-width: 80%;'>
                <strong>Você:</strong> {item['pergunta']}
            </div>
        </div>
        <div style='display: flex; align-items: center; margin-bottom: 20px;'>
            <div style='margin-right: 10px;'>🤖</div>
            <div style='background-color: #e0f7fa; padding: 10px; border-radius: 10px; max-width: 80%;'>
                <strong>Bot:</strong> {item['resposta']}
            </div>
        </div>
        """, unsafe_allow_html=True)
