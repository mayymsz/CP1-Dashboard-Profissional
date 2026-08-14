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

    /* MENU LATERAL */

    section[data-testid="stSidebar"] {
        background-color: #161A22;
    }

    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        border-radius: 7px;
        padding: 10px 14px;
    }

    section[data-testid="stSidebar"] .stButton > button > div {
        width: 100%;
        justify-content: flex-start !important;
    }

    section[data-testid="stSidebar"] .stButton > button p {
        width: 100%;
        text-align: left !important;
        margin: 0;
    }

    section[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"] {
        background-color: transparent !important;
        border: none !important;
        color: #D6DAE1 !important;
    }

    section[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #202631 !important;
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] button[data-testid="stBaseButton-primary"] {
        background-color: #252C38 !important;
        border: none !important;
        border-left: 3px solid #7C83FD !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }


    /* CARDS PADRÃO DO STREAMLIT */

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


    /* TOPO DO DASHBOARD */

    .dashboard-title {
        margin-top: 8px;
        margin-bottom: 28px;
    }

    .dashboard-tag {
        display: inline-block;
        padding: 6px 12px;
        margin-bottom: 14px;

        background-color: rgba(124, 58, 237, 0.12);
        border: 1px solid rgba(124, 58, 237, 0.35);
        border-radius: 20px;

        color: #A78BFA;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .dashboard-title h1 {
        margin: 0;
        color: #FFFFFF;
        font-size: 38px;
        font-weight: 700;
    }

    .dashboard-title p {
        margin-top: 8px;
        color: #959BAA;
        font-size: 15px;
    }


    /* TÍTULOS DAS SEÇÕES */

    .section-label {
        margin-top: 8px;
        margin-bottom: 14px;

        color: #FFFFFF;
        font-size: 18px;
        font-weight: 600;
    }


    /* CARDS DA VISÃO GERAL */

    .summary-card {
        min-height: 120px;
        padding: 18px 20px;

        background-color: #171A22;
        border: 1px solid #2A2F3A;
        border-radius: 12px;

        display: flex;
        flex-direction: column;
        justify-content: center;

        transition: 0.2s ease;
    }

    .summary-card:hover {
        border-color: #7C3AED;
        transform: translateY(-2px);
    }

    .summary-label {
        color: #8F95A3;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.8px;
    }

    .summary-number {
        margin-top: 8px;

        color: #FFFFFF;
        font-size: 30px;
        font-weight: 650;
        line-height: 1.1;
    }

    .summary-text {
        font-size: 23px;
    }

    .summary-detail {
        margin-top: 6px;

        color: #A78BFA;
        font-size: 12px;
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
    st.markdown(
    """
    <div class="dashboard-title"><span class="dashboard-tag">DASHBOARD PROFISSIONAL</span><h1>Perfil dos Estagiários</h1><p>Mercado brasileiro de Dados e Tecnologia</p></div>
        """,
        unsafe_allow_html=True
    ) 

    total_estagiarios = len(estagiarios)

    faixa_mais_comum = estagiarios["2.h_faixa_salarial"].mode()[0]

    modelo_mais_comum = estagiarios["2.q_modelo_de_trabalho_atual"].mode()[0]

    st.markdown(
        '<div class="section-label">Visão Geral</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
<div class="summary-card">
    <span class="summary-label">TOTAL DE ESTAGIÁRIOS</span>
    <strong class="summary-number">{total_estagiarios}</strong>
    <span class="summary-detail">participantes analisados</span>
</div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
<div class="summary-card">
    <span class="summary-label">FAIXA SALARIAL MAIS COMUM</span>
    <strong class="summary-number summary-text">R$ 1.001 - 2.000</strong>
    <span class="summary-detail">por mês</span>
</div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
<div class="summary-card">
    <span class="summary-label">MODELO MAIS COMUM</span>
    <strong class="summary-number summary-text">Híbrido</strong>
    <span class="summary-detail">com dias fixos presenciais</span>
</div>
            """,
            unsafe_allow_html=True
        )

    aba1, aba2, aba3, aba4, aba5 = st.tabs([
        "Faixa Salarial",
        "Modelo de Trabalho",
        "Linguagens",
        "Formação",
        "Experiência em TI"
    ])

    with aba1:
        st.subheader("Análise Salarial")

        # Filtro por modelo de trabalho
        opcoes_modelo = ["Todos"] + sorted(
            estagiarios["2.q_modelo_de_trabalho_atual"]
            .dropna()
            .unique()
            .tolist()
        )

        modelo_salario = st.selectbox(
            "Filtrar por modelo de trabalho:",
            opcoes_modelo
        )

        dados_salario = estagiarios.copy()

        if modelo_salario != "Todos":
            dados_salario = dados_salario[
                dados_salario["2.q_modelo_de_trabalho_atual"] == modelo_salario
            ]

        # Moda da faixa salarial
        moda_salario = (
            dados_salario["2.h_faixa_salarial"]
            .dropna()
            .mode()[0]
        )

        # Valores representativos das faixas salariais
        valores_salariais = {
            "Menos de R$ 1.000/mês": 500,
            "de R$ 1.001/mês a R$ 2.000/mês": 1500,
            "de R$ 2.001/mês a R$ 3.000/mês": 2500,
            "de R$ 3.001/mês a R$ 4.000/mês": 3500,
            "de R$ 4.001/mês a R$ 6.000/mês": 5000,
            "de R$ 8.001/mês a R$ 12.000/mês": 10000
        }

        dados_boxplot = dados_salario.copy()

        dados_boxplot["Salário estimado"] = dados_boxplot[
            "2.h_faixa_salarial"
        ].map(valores_salariais)

        dados_boxplot = dados_boxplot.dropna(
            subset=["Salário estimado"]
        )

        # Cálculos estatísticos
        media_salario = dados_boxplot["Salário estimado"].mean()
        mediana_salario = dados_boxplot["Salário estimado"].median()
        total_salarios = len(dados_boxplot)

        # Indicadores
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Estagiários analisados",
            total_salarios
        )

        col2.metric(
            "Média estimada",
            f"R$ {media_salario:,.0f}".replace(",", ".")
        )

        col3.metric(
            "Mediana estimada",
            f"R$ {mediana_salario:,.0f}".replace(",", ".")
        )

        st.write(
            f"**Moda salarial:** {moda_salario}"
        )

        # Boxplot
        st.subheader("Distribuição Salarial Estimada")

        grafico_boxplot = px.box(
            dados_boxplot,
            x="Salário estimado",
            points="all",
            labels={
                "Salário estimado": "Salário mensal estimado (R$)"
            }
        )

        grafico_boxplot.update_traces(
            fillcolor="#6D28D9",
            line_color="#8B5CF6",
            marker_color="#A78BFA",
            marker_size=7,
            marker_opacity=0.55,
            jitter=0.25,
            pointpos=0
        )

        # Média destacada em verde
        grafico_boxplot.add_vline(
            x=media_salario,
            line_width=3,
            line_dash="dash",
            line_color="#22C55E",
            annotation_text="Média",
            annotation_position="top"
        )

        # Mediana em roxo claro
        grafico_boxplot.add_vline(
            x=mediana_salario,
            line_width=2,
            line_dash="dot",
            line_color="#C4B5FD",
            annotation_text="Mediana",
            annotation_position="bottom"
        )

        grafico_boxplot.update_layout(
            height=420,
            showlegend=False,
            xaxis=dict(
                tickprefix="R$ ",
                separatethousands=True,
                rangemode="tozero"
            ),
            yaxis=dict(
                showticklabels=False,
                title=""
            ),
            margin=dict(
                l=30,
                r=30,
                t=60,
                b=40
            )
        )

        st.plotly_chart(
            grafico_boxplot,
            use_container_width=True
        )

        # Aviso quando não existe variação salarial
        if dados_boxplot["Salário estimado"].nunique() == 1:
            st.info(
                "Nesta seleção, todos os estagiários estão na mesma faixa salarial. "
                "Por isso, o boxplot aparece concentrado em uma única posição."
            )

        st.caption(
            "Os salários são estimados a partir de valores representativos das "
            "faixas salariais informadas na pesquisa."
        )

    with aba2:
        st.subheader("Modelo de Trabalho dos Estagiários")

        # Filtro por área de formação
        opcoes_formacao = [
            "Todas",
            "Computação / Engenharia de Software / Sistemas de Informação/ TI",
            "Ciência de Dados / Inteligência Artificial",
            "Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais",
            "Outras Engenharias (não incluir engenharia de software ou TI)"
        ]

        formacao_modelo = st.selectbox(
            "Filtrar por área de formação:",
            opcoes_formacao,
            key="formacao_modelo"
        )

        dados_modelo = estagiarios.copy()

        if formacao_modelo != "Todas":
            dados_modelo = dados_modelo[
                dados_modelo["1.m_área_de_formação"] == formacao_modelo
            ]

        # Contagem dos modelos de trabalho
        modelos_trabalho = (
            dados_modelo["2.q_modelo_de_trabalho_atual"]
            .dropna()
            .value_counts()
            .reset_index()
        )

        modelos_trabalho.columns = [
            "Modelo de trabalho",
            "Quantidade"
        ]

        # Gráfico de barras horizontais
        grafico_modelos = px.bar(
            modelos_trabalho,
            x="Quantidade",
            y="Modelo de trabalho",
            orientation="h",
            color="Modelo de trabalho",
            text="Quantidade",
            color_discrete_sequence=[
                "#5B21B6",
                "#6D28D9",
                "#7C3AED",
                "#A78BFA"
            ],
            labels={
                "Quantidade": "Quantidade de estagiários",
                "Modelo de trabalho": ""
            }
        )

        grafico_modelos.update_traces(
            textposition="outside"
        )

        grafico_modelos.update_layout(
            height=400,
            showlegend=False,
            yaxis={
                "categoryorder": "total ascending"
            },
            margin=dict(l=20, r=40, t=20, b=20)
        )

        st.plotly_chart(
            grafico_modelos,
            use_container_width=True
        )

        # Modelo predominante
        modelo_mais_comum = modelos_trabalho.iloc[0]

        percentual_modelo = (
            modelo_mais_comum["Quantidade"]
            / modelos_trabalho["Quantidade"].sum()
        ) * 100

        st.write(
            f"""
            O modelo de trabalho mais frequente nesta seleção é
            **{modelo_mais_comum["Modelo de trabalho"]}**, representando
            aproximadamente **{percentual_modelo:.1f}%** dos estagiários
            considerados.
            """
        )

    with aba3:
        st.subheader("Linguagens mais utilizadas")

        # Linguagens disponíveis na base
        colunas_linguagens = {
            "SQL": "4.c.1_SQL",
            "R": "4.c.2_R",
            "Python": "4.c.3_Python",
            "C/C++/C#": "4.c.4_C/C++/C#",
            "Julia": "4.c.5_Julia",
            "Visual Basic/VBA": "4.c.6_Visual Basic/VBA",
            "Scala": "4.c.7_Scala",
            "DAX": "4.c.8_DAX",
            "Rust": "4.c.9_Rust"
        }

        # Filtro por modelo de trabalho
        opcoes_modelo_linguagens = ["Todos"] + sorted(
            estagiarios["2.q_modelo_de_trabalho_atual"]
            .dropna()
            .unique()
            .tolist()
        )

        modelo_linguagens = st.selectbox(
            "Filtrar por modelo de trabalho:",
            opcoes_modelo_linguagens,
            key="modelo_linguagens"
        )

        dados_linguagens = estagiarios.copy()

        if modelo_linguagens != "Todos":
            dados_linguagens = dados_linguagens[
                dados_linguagens["2.q_modelo_de_trabalho_atual"]
                == modelo_linguagens
            ]

        # Contagem das linguagens
        linguagens = {}

        for nome, coluna in colunas_linguagens.items():
            linguagens[nome] = (dados_linguagens[coluna] == 1).sum()

        linguagens_df = pd.DataFrame({
            "Linguagem": linguagens.keys(),
            "Quantidade": linguagens.values()
        })

        # Remove linguagens que não foram utilizadas
        linguagens_df = linguagens_df[
            linguagens_df["Quantidade"] > 0
        ]

        # Ordena da menor para a maior
        linguagens_df = linguagens_df.sort_values(
            "Quantidade",
            ascending=True
        )

                # Gráfico
        grafico_linguagens = px.bar(
            linguagens_df,
            x="Quantidade",
            y="Linguagem",
            orientation="h",
            color="Linguagem",
            text="Quantidade",
            color_discrete_sequence=[
                "#5B21B6",
                "#6D28D9",
                "#7C3AED",
                "#8B5CF6",
                "#A78BFA"
            ],
            labels={
                "Quantidade": "Quantidade de estagiários",
                "Linguagem": "Linguagem"
            }
        )

        grafico_linguagens.update_traces(
            textposition="outside"
        )

        grafico_linguagens.update_layout(
            height=450,
            showlegend=False,
            yaxis={
                "categoryorder": "total ascending"
            },
            margin=dict(l=20, r=40, t=20, b=20)
        )

        st.plotly_chart(
            grafico_linguagens,
            use_container_width=True
        )

    with aba4:
        st.subheader("Área de Formação dos Estagiários")

        # Áreas relacionadas a Dados e Tecnologia
        areas_tecnologia = [
            "Computação / Engenharia de Software / Sistemas de Informação/ TI",
            "Ciência de Dados / Inteligência Artificial",
            "Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais",
            "Outras Engenharias (não incluir engenharia de software ou TI)"
        ]

        dados_formacao = estagiarios[
            estagiarios["1.m_área_de_formação"].isin(areas_tecnologia)
        ]

        formacao = (
            dados_formacao["1.m_área_de_formação"]
            .value_counts()
            .reset_index()
        )

        formacao.columns = ["Área de formação", "Quantidade"]

        grafico_formacao = px.bar(
            formacao,
            x="Quantidade",
            y="Área de formação",
            orientation="h",
            text="Quantidade",
            color="Área de formação",
            color_discrete_sequence=[
                "#5B21B6",
                "#6D28D9",
                "#7C3AED",
                "#A78BFA"
            ],
            labels={
                "Quantidade": "Quantidade de estagiários",
                "Área de formação": ""
            }
        )

        grafico_formacao.update_traces(
            textposition="outside"
        )

        grafico_formacao.update_layout(
            height=400,
            showlegend=False,
            yaxis={
                "categoryorder": "total ascending"
            },
            margin=dict(l=20, r=40, t=20, b=20)
        )

        st.plotly_chart(
            grafico_formacao,
            use_container_width=True
        )

    with aba5:
        st.subheader("Experiência em TI")

        # Áreas relacionadas a Dados e Tecnologia
        areas_experiencia = [
            "Todas",
            "Computação / Engenharia de Software / Sistemas de Informação/ TI",
            "Ciência de Dados / Inteligência Artificial",
            "Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais",
            "Outras Engenharias (não incluir engenharia de software ou TI)"
        ]

        filtro_experiencia = st.selectbox(
            "Filtrar por área de formação:",
            areas_experiencia,
            key="filtro_experiencia"
        )

        dados_experiencia = estagiarios.copy()

        if filtro_experiencia != "Todas":
            dados_experiencia = dados_experiencia[
                dados_experiencia["1.m_área_de_formação"] == filtro_experiencia
            ]

        experiencia_ti = (
            dados_experiencia["2.j_tempo_de_experiencia_em_ti"]
            .dropna()
            .value_counts()
            .reset_index()
        )

        experiencia_ti.columns = [
            "Tempo de experiência",
            "Quantidade"
        ]

        # Nomes mais curtos para facilitar a visualização
        nomes_experiencia = {
            "Não tive experiência na área de TI/Engenharia de Software antes de começar a trabalhar na área de dados": "Sem experiência anterior",
            "Menos de 1 ano": "Menos de 1 ano",
            "de 1 a 2 anos": "1 a 2 anos",
            "de 3 a 4 anos": "3 a 4 anos",
            "de 5 a 6 anos": "5 a 6 anos"
        }

        experiencia_ti["Experiência"] = experiencia_ti[
            "Tempo de experiência"
        ].replace(nomes_experiencia)

        # Gráfico de rosca
        grafico_experiencia = px.pie(
            experiencia_ti,
            names="Experiência",
            values="Quantidade",
            hole=0.55,
            color_discrete_sequence=[
                "#4C1D95",
                "#5B21B6",
                "#6D28D9",
                "#8B5CF6",
                "#C4B5FD"
            ]
        )

        grafico_experiencia.update_traces(
            textposition="inside",
            textinfo="percent",
            hovertemplate="<b>%{label}</b><br>Quantidade: %{value}<br>Percentual: %{percent}<extra></extra>"
        )

        grafico_experiencia.update_layout(
            height=450,
            legend_title_text="Experiência em TI",
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.plotly_chart(
            grafico_experiencia,
            use_container_width=True
        )

        if not experiencia_ti.empty:
            categoria_principal = experiencia_ti.iloc[0]

            percentual_experiencia = (
                categoria_principal["Quantidade"]
                / experiencia_ti["Quantidade"].sum()
            ) * 100

            st.write(
                f"""
                A faixa de experiência mais frequente nesta seleção é
                **{categoria_principal["Tempo de experiência"]}**,
                representando aproximadamente
                **{percentual_experiencia:.1f}%** dos estagiários considerados.
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