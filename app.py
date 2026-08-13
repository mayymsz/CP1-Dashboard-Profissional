import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Profissional",
    layout="wide"
)

st.markdown(
    """
    <style>

    /* Fundo do menu lateral */
    section[data-testid="stSidebar"] {
        background-color: #161A22;
    }

    /* Botões do menu */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        border-radius: 7px;
        padding: 10px 14px;
    }

    /* Faz o conteúdo do botão ocupar toda a largura */
    section[data-testid="stSidebar"] .stButton > button > div {
        width: 100%;
        justify-content: flex-start !important;
    }

    /* Texto alinhado à esquerda */
    section[data-testid="stSidebar"] .stButton > button p {
        width: 100%;
        text-align: left !important;
        margin: 0;
    }

    /* Opções não selecionadas */
    section[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"] {
        background-color: transparent !important;
        border: none !important;
        color: #D6DAE1 !important;
    }

    /* Ao passar o mouse */
    section[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #202631 !important;
        color: #FFFFFF !important;
    }

    /* Página selecionada */
    section[data-testid="stSidebar"] button[data-testid="stBaseButton-primary"] {
        background-color: #252C38 !important;
        border: none !important;
        border-left: 3px solid #7C83FD !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* Cards dos indicadores */
    div[data-testid="stMetric"] {
        background-color: #161A22;
        border: 1px solid #252C38;
        padding: 18px;
        border-radius: 10px;
    }

    div[data-testid="stMetricLabel"] {
        color: #AEB6C4;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Carregando a base de dados
df = pd.read_csv("dados/Final Dataset - State of Data 2025-2026 - Kaggle.csv")

# Filtrando apenas os estagiários
estagiarios = df[df["2.a_situação_de_trabalho"] == "Estagiário"]

# Página inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "Quem sou eu"

with st.sidebar:
    st.markdown("### NAVEGAÇÃO")

    if st.button(
        "Quem sou eu",
        use_container_width=True,
        type="primary" if st.session_state.pagina == "Quem sou eu" else "secondary"
    ):
        st.session_state.pagina = "Quem sou eu"
        st.rerun()

    if st.button(
        "Minhas qualificações",
        use_container_width=True,
        type="primary" if st.session_state.pagina == "Minhas qualificações" else "secondary"
    ):
        st.session_state.pagina = "Minhas qualificações"
        st.rerun()

    if st.button(
        "Skills",
        use_container_width=True,
        type="primary" if st.session_state.pagina == "Skills" else "secondary"
    ):
        st.session_state.pagina = "Skills"
        st.rerun()

    if st.button(
        "Análise de Dados",
        use_container_width=True,
        type="primary" if st.session_state.pagina == "Análise de Dados" else "secondary"
    ):
        st.session_state.pagina = "Análise de Dados"
        st.rerun()

pagina = st.session_state.pagina

if pagina == "Quem sou eu":
    st.title("Quem sou eu")

    st.subheader("Mayene Moura da Silva")
    st.write("Engenharia de Software | Desenvolvimento de Software")

    st.write(
        """
        Sou estudante de Engenharia de Software na FIAP, com experiência acadêmica
        no desenvolvimento de aplicações web e soluções digitais utilizando Java,
        Python, JavaScript, HTML e CSS.

        Ao longo da graduação, participei de projetos voltados à resolução de problemas
        reais, aplicando conceitos de programação, integração de APIs, desenvolvimento
        de sistemas e soluções com IA. Atualmente, direciono meus estudos para o aprofundamento em Java
        e desenvolvimento de software, buscando consolidar minha base técnica e ampliar
        meus conhecimentos na área de tecnologia.
        """
    )

elif pagina == "Minhas qualificações":
    st.title("Minhas qualificações")

    st.subheader("Formação")
    st.write(
        """
        **Engenharia de Software - FIAP**  
        Bacharelado | Fev/2025 - Nov/2028
        """
    )

    st.subheader("Experiências e Projetos")

    st.write(
        """
        **Challenge Passa a Bola - NEXT FIAP 2025**  
        Participação no desenvolvimento de uma plataforma voltada à ampliação da
        visibilidade do futebol feminino, utilizando React, TypeScript e Tailwind CSS.
        Desenvolvimento de interfaces, funcionalidades e integração de chatbot com
        Typebot. Projeto reconhecido com o **2º lugar no NEXT FIAP 2025**.

        **Projetos Acadêmicos - FIAP**  
        Desenvolvimento de aplicações, sistemas e soluções digitais utilizando
        Java, Python, JavaScript, HTML e CSS, aplicando conceitos de Programação
        Orientada a Objetos, integração de APIs, análise de dados e Inteligência Artificial.

        **Freelancer - Designer de Conteúdo Digital**  
        Desenvolvimento de design e conteúdo para redes sociais, criação de
        identidades visuais e materiais digitais.
        """
    )

elif pagina == "Skills":
    st.title("Skills")

    st.subheader("Linguagens")
    st.write("Java | Python | JavaScript | HTML | CSS")

    st.subheader("Ferramentas")
    st.write("Git | GitHub | Typebot | Figma")

    st.subheader("Conhecimentos")
    st.write(
        """
        Desenvolvimento Web | Programação Orientada a Objetos | Estruturas de Dados |
        Lógica de Programação | Integração de Sistemas e APIs | Chatbots |
        Inteligência Artificial
        """
    )

    st.subheader("Soft Skills")
    st.write(
        """
        Trabalho em equipe | Organização | Comunicação | Resolução de problemas |
        Aprendizado contínuo
        """
    )

elif pagina == "Análise de Dados":
    st.title("Perfil dos Estagiários no Mercado de Dados e Tecnologia no Brasil")

    st.write(
        """
        Esta análise utiliza dados da pesquisa State of Data Brazil 2025-2026
        e considera apenas os participantes que informaram estar atuando como estagiários.
        """
    )

    st.subheader("Visão Geral")

    total_estagiarios = len(estagiarios)

    faixa_mais_comum = estagiarios["2.h_faixa_salarial"].mode()[0]

    modelo_mais_comum = estagiarios["2.q_modelo_de_trabalho_atual"].mode()[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total de estagiários",
        total_estagiarios
    )

    col2.metric(
        "Faixa salarial mais comum",
        faixa_mais_comum
    )

    col3.metric(
        "Modelo mais comum",
        modelo_mais_comum
    )

    aba1, aba2, aba3, aba4, aba5 = st.tabs([
        "Faixa Salarial",
        "Modelo de Trabalho",
        "Formação",
        "Cargos",
        "Experiência em TI"
    ])

    with aba1:
        st.subheader("Distribuição por Faixa Salarial")

        salarios = estagiarios["2.h_faixa_salarial"].value_counts()
        grafico_salarios = px.bar(
            x=salarios.values,
            y=salarios.index,
            orientation="h",
            labels={
                "x": "Quantidade de estagiários",
                "y": "Faixa salarial"
            }
        )

        grafico_salarios.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=450
        )

        st.plotly_chart(grafico_salarios, use_container_width=True)

        percentual_salario = (salarios.iloc[0] / total_estagiarios) * 100

        st.write(
            f"""
            A faixa salarial mais frequente entre os estagiários é
            **{salarios.index[0]}**, representando aproximadamente
            **{percentual_salario:.1f}%** dos estagiários analisados.
            """
        )

    with aba2:
        st.subheader("Modelo de Trabalho dos Estagiários")

        modelos_trabalho = estagiarios["2.q_modelo_de_trabalho_atual"].value_counts()
        grafico_modelos = px.bar(
            x=modelos_trabalho.values,
            y=modelos_trabalho.index,
            orientation="h",
            labels={
                "x": "Quantidade de estagiários",
                "y": "Modelo de trabalho"
            }
        )

        grafico_modelos.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=400
        )

        st.plotly_chart(grafico_modelos, use_container_width=True)

        percentual_modelo = (modelos_trabalho.iloc[0] / total_estagiarios) * 100

        st.write(
            f"""
            O modelo de trabalho mais frequente é
            **{modelos_trabalho.index[0]}**, adotado por aproximadamente
            **{percentual_modelo:.1f}%** dos estagiários.
            """
        )

    with aba3:
        st.subheader("Área de Formação dos Estagiários")

        formacao = estagiarios["1.m_área_de_formação"].value_counts()
        grafico_formacao = px.bar(
            x=formacao.values,
            y=formacao.index,
            orientation="h",
            labels={
                "x": "Quantidade de estagiários",
                "y": "Área de formação"
            }
        )

        grafico_formacao.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=450
        )

        st.plotly_chart(grafico_formacao, use_container_width=True)

        percentual_formacao = (formacao.iloc[0] / total_estagiarios) * 100

        st.write(
            f"""
            A área de formação mais frequente entre os estagiários é
            **{formacao.index[0]}**, representando aproximadamente
            **{percentual_formacao:.1f}%** dos participantes analisados.
            """
        )

    with aba4:
        st.subheader("Cargos dos Estagiários")

        cargos = estagiarios["2.f_cargo_atual"].value_counts()
        grafico_cargos = px.bar(
            x=cargos.values,
            y=cargos.index,
            orientation="h",
            labels={
                "x": "Quantidade de estagiários",
                "y": "Cargo"
            }
        )

        grafico_cargos.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=450
        )

        st.plotly_chart(grafico_cargos, use_container_width=True)

        percentual_cargo = (cargos.iloc[0] / total_estagiarios) * 100

        st.write(
            f"""
            O cargo mais frequente entre os estagiários é
            **{cargos.index[0]}**, correspondendo a aproximadamente
            **{percentual_cargo:.1f}%** dos estagiários.
            """
        )

    with aba5:
        st.subheader("Experiência em TI")

        experiencia_ti = estagiarios["2.j_tempo_de_experiencia_em_ti"].value_counts()
        grafico_experiencia = px.bar(
            x=experiencia_ti.values,
            y=experiencia_ti.index,
            orientation="h",
            labels={
                "x": "Quantidade de estagiários",
                "y": "Tempo de experiência"
            }
        )

        grafico_experiencia.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=400
        )

        st.plotly_chart(grafico_experiencia, use_container_width=True)

        percentual_experiencia = (
            experiencia_ti.iloc[0] / total_estagiarios
        ) * 100

        st.write(
            f"""
            Em relação à experiência em TI, a categoria mais frequente é
            **{experiencia_ti.index[0]}**, representando aproximadamente
            **{percentual_experiencia:.1f}%** dos estagiários analisados.
            """
        )

    st.divider()

    st.subheader("Conclusão da Análise")

    st.write(
        """
        A análise dos dados mostra que os estagiários representam profissionais
        em início de carreira com diferentes formações, cargos e níveis de experiência
        dentro do mercado de dados e tecnologia no Brasil.

        A faixa salarial entre R$ 1.001 e R$ 2.000 se destaca como a mais frequente,
        enquanto os modelos presencial, híbrido e remoto apresentam participação
        relevante entre os estagiários.

        Os resultados também demonstram a diversidade de formações e funções presentes
        no setor de tecnologia, indicando diferentes possibilidades de entrada e
        desenvolvimento profissional na área.
        """
    )

    st.caption("Fonte: State of Data Brazil 2025-2026 - Data Hackers")