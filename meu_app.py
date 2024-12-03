import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Meu Site Streamlit")

# Credenciais de login
USUARIOS = {
    "junior": "123",  
}

def autenticar(usuario, senha):
    """Valida as credenciais de login."""
    return USUARIOS.get(usuario) == senha

# Estado de autenticação
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    # Formulário de login
    st.title("Login")
    with st.form("login_form"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")

    if submit:
        if autenticar(usuario, senha):
            st.session_state.autenticado = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos!")
else:
    # Interface principal do app
    with st.container():
        st.subheader("Streamlit Teste")
        st.title("Dashboard de Teste")
        

    @st.cache_data
    def carregar_dados():
        tabela = pd.read_csv("resultados.csv")
        return tabela

    with st.container():
        st.write("---")
        qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
        num_dias = int(qtde_dias.replace("D", ""))
        dados = carregar_dados()
        dados = dados[-num_dias:]
        st.area_chart(dados, x="Data", y="Contratos")
    
    # Botão de logout
    if st.button("Sair"):
        st.session_state.autenticado = False
        st.experimental_rerun()
