import json
import pandas as pd
import requests
import streamlit as st

# ================== CONFIGURAÇÃO ================== #

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# ================== FUNÇÕES AUXILIARES ================== #

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def formatar_lista_simples(lista):
    if not lista:
        return "- Não informado"

    return "\n".join([f"- {item}" for item in lista])


@st.cache_data
def carregar_dados():
    perfil = carregar_json("./data/perfil_usuario.json")
    historico = pd.read_csv("./data/historico_treinos.csv").fillna("Não informado")
    fontes = carregar_json("./data/fontes_confiaveis.json")
    feedback = pd.read_csv("./data/feedback_usuario.csv").fillna("Não informado")
    exercicios = carregar_json("./data/base_exercicios.json")
    base = carregar_json("./data/base_conhecimento.json")

    return perfil, historico, fontes, feedback, exercicios, base


# ================== SYSTEM PROMPT ================== #

SYSTEM_PROMPT = """
Você é o Personal IA, um assistente inteligente, amigável e didático de apoio ao treinamento físico.

OBJETIVO:
Ajudar o usuário a montar, entender e adaptar treinos físicos de forma simples, segura e personalizada, usando os dados do próprio usuário como base para exemplos e recomendações práticas.

REGRAS:
- Nunca realize diagnóstico médico;
- Nunca prescreva medicamentos, suplementos, anabolizantes ou tratamentos clínicos;
- Nunca diga que substitui um profissional de Educação Física, médico ou fisioterapeuta;
- Nunca prometa resultados garantidos;
- Jamais ignore dores, limitações físicas ou sinais de risco relatados pelo usuário;
- Use os dados fornecidos para dar exemplos personalizados;
- Use a base de conhecimento e as fontes confiáveis disponíveis no projeto;
- Linguagem simples, motivadora e acessível para um usuário comum;
- Se não souber algo, admita: "Não tenho essa informação com segurança, mas posso te ajudar com...";
- Quando houver dor intensa, lesão, tontura, falta de ar ou sintomas persistentes, recomende procurar um profissional habilitado;
- Sempre pergunte se o usuário entendeu ou se deseja adaptar o treino;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos, exceto quando o usuário pedir um treino detalhado.
"""


# ================== CARREGAR DADOS ================== #

perfil, historico, fontes, feedback, exercicios, base = carregar_dados()


# ================== MONTAR CONTEXTO ================== #

metas_formatadas = "\n".join([
    f"- {meta.get('meta', 'Não informado')} | "
    f"Indicador: {meta.get('indicador', 'Não informado')} | "
    f"Prazo: {meta.get('prazo', 'Não informado')}"
    for meta in perfil.get("metas", [])
]) or "- Não informado"

equipamentos_formatados = formatar_lista_simples(
    perfil.get("equipamentos_disponiveis", [])
)

preferencias = perfil.get("preferencias", {})

exercicios_preferidos = formatar_lista_simples(
    preferencias.get("exercicios_preferidos", [])
)

exercicios_a_evitar = formatar_lista_simples(
    preferencias.get("exercicios_a_evitar", [])
)

limitacoes_formatadas = "\n".join([
    f"- {lim.get('regiao', 'Não informado')}: {lim.get('descricao', 'Não informado')} | "
    f"Gravidade: {lim.get('nivel_gravidade', 'Não informado')} | "
    f"Ação recomendada: {lim.get('acao_recomendada_para_o_agente', 'Não informado')}"
    for lim in perfil.get("limitacoes_fisicas", [])
]) or "- Não informado"

restricoes_formatadas = formatar_lista_simples(
    perfil.get("restricoes_de_seguranca", [])
)


# ================== FORMATAR HISTÓRICO DE TREINOS ================== #

historico_recente = historico.tail(5)

historico_formatado = "\n".join([
    f"- Data: {linha['data']} | Grupo muscular: {linha['grupo_muscular']} | "
    f"Exercício: {linha['exercicio']} | Séries: {linha['series']} | "
    f"Repetições: {linha['repeticoes']} | Carga: {linha['carga_kg']} kg | "
    f"Tipo: {linha['tipo_treino']} | Observações: {linha['observacoes']}"
    for _, linha in historico_recente.iterrows()
]) or "- Não informado"


# ================== FORMATAR FEEDBACK DO USUÁRIO ================== #

feedback_recente = feedback.tail(5)

feedback_formatado = "\n".join([
    f"- Data: {linha['data']} | Canal: {linha['canal']} | Tema: {linha['tema']} | "
    f"Resumo: {linha['resumo']} | Dor: {linha['nivel_dor_0_10']}/10 | "
    f"Fadiga: {linha['nivel_fadiga_0_10']}/10 | "
    f"Ação sugerida: {linha['acao_sugerida']} | Resolvido: {linha['resolvido']}"
    for _, linha in feedback_recente.iterrows()
]) or "- Não informado"


# ================== FORMATAR BASE DE EXERCÍCIOS ================== #

exercicios_limitados = exercicios[:8]

exercicios_formatados = "\n".join([
    f"- {exercicio.get('nome', 'Não informado')} | "
    f"Grupo principal: {exercicio.get('grupo_muscular_principal', 'Não informado')} | "
    f"Equipamento: {exercicio.get('equipamento', 'Não informado')} | "
    f"Nível: {exercicio.get('nivel', 'Não informado')} | "
    f"Objetivo indicado: {', '.join(exercicio.get('objetivo_indicado', []))} | "
    f"Séries: {exercicio.get('series_recomendadas', 'não informado')} | "
    f"Repetições/Duração: {exercicio.get('repeticoes_recomendadas', exercicio.get('duracao_recomendada', 'não informado'))} | "
    f"Substituições: {', '.join(exercicio.get('substituicoes', []))} | "
    f"Cuidados: {exercicio.get('cuidados', 'não informado')}"
    for exercicio in exercicios_limitados
]) or "- Não informado"


# ================== FORMATAR BASE DE CONHECIMENTO ================== #

principios_formatados = "\n".join([
    f"- {item.get('principio', 'Não informado')}: {item.get('descricao', 'Não informado')}"
    for item in base.get("principios_de_treinamento", [])
]) or "- Não informado"

diretrizes_formatadas = "\n".join([
    f"- {nome}: {conteudo.get('resumo', 'Não informado')} | "
    f"Fonte relacionada: {conteudo.get('fonte_relacionada', 'Não informado')}"
    for nome, conteudo in base.get("diretrizes_gerais", {}).items()
]) or "- Não informado"

parametros_formatados = "\n".join([
    f"- {nome}: {json.dumps(conteudo, ensure_ascii=False)}"
    for nome, conteudo in base.get("parametros_sugeridos", {}).items()
]) or "- Não informado"

regras_agente_formatadas = formatar_lista_simples(
    base.get("regras_para_o_agente", [])
)


# ================== FORMATAR FONTES CONFIÁVEIS ================== #

fontes_formatadas = "\n".join([
    f"- {fonte.get('nome', 'Não informado')} | "
    f"Instituição: {fonte.get('instituicao', 'Não informado')} | "
    f"Uso no projeto: {fonte.get('uso_no_projeto', 'Não informado')}"
    for fonte in fontes
]) or "- Não informado"


# ================== CONTEXTO FINAL DO PERSONAL IA ================== #

contexto = f"""
Use apenas as informações fornecidas abaixo e a base de conhecimento disponível.
Não invente dados, fontes, diagnósticos ou recomendações clínicas.

================== PERFIL DO USUÁRIO ==================

USUÁRIO: {perfil.get('nome', 'Não informado')}, {perfil.get('idade', 'Não informado')} anos
PROFISSÃO: {perfil.get('profissao', 'Não informado')}
ALTURA: {perfil.get('altura_cm', 'Não informado')} cm
PESO: {perfil.get('peso_kg', 'Não informado')} kg
NÍVEL DE EXPERIÊNCIA: {perfil.get('nivel_experiencia', 'Não informado')}
LOCAL DE TREINO: {perfil.get('local_de_treino', 'Não informado')}

OBJETIVO PRINCIPAL:
{perfil.get('objetivo_principal', 'Não informado')}

METAS:
{metas_formatadas}

FREQUÊNCIA:
- Frequência atual: {perfil.get('frequencia_treino_atual', 'Não informado')}
- Frequência desejada: {perfil.get('frequencia_treino_desejada', 'Não informado')}
- Tempo disponível por treino: {perfil.get('tempo_disponivel_por_treino_minutos', 'Não informado')} minutos

EQUIPAMENTOS DISPONÍVEIS:
{equipamentos_formatados}

PREFERÊNCIAS DE TREINO:
- Tipo de treino preferido: {preferencias.get('tipo_treino_preferido', 'Não informado')}
- Formato preferido: {preferencias.get('formato_preferido', 'Não informado')}

EXERCÍCIOS PREFERIDOS:
{exercicios_preferidos}

EXERCÍCIOS A EVITAR:
{exercicios_a_evitar}

LIMITAÇÕES FÍSICAS:
{limitacoes_formatadas}

RESTRIÇÕES DE SEGURANÇA DO PERFIL:
{restricoes_formatadas}

================== HISTÓRICO DE TREINOS RECENTE ==================

{historico_formatado}

================== FEEDBACK RECENTE DO USUÁRIO ==================

{feedback_formatado}

================== BASE DE EXERCÍCIOS ==================

{exercicios_formatados}

================== PRINCÍPIOS DA BASE DE CONHECIMENTO ==================

{principios_formatados}

================== DIRETRIZES GERAIS ==================

{diretrizes_formatadas}

================== PARÂMETROS SUGERIDOS ==================

{parametros_formatados}

================== FONTES CONFIÁVEIS ==================

{fontes_formatadas}

================== REGRAS DO PERSONAL IA ==================

{regras_agente_formatadas}

INSTRUÇÕES DE RESPOSTA:
- Personalize as respostas com base no perfil, objetivo, frequência, histórico, feedback e limitações do usuário.
- Quando houver relato de dor, seja conservador e priorize segurança.
- Se os dados forem insuficientes, peça informações adicionais antes de montar um treino completo.
- Não realize diagnóstico médico.
- Não prescreva medicamentos, suplementos, anabolizantes ou tratamentos clínicos.
- Não prometa resultados garantidos.
- Explique as recomendações de forma clara, objetiva e acessível.
"""


# ================== CHAMAR OLLAMA ================== #

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

PERGUNTA DO USUÁRIO:
{msg}
"""

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.4,
            "top_p": 0.9,
            "num_predict": 700,
            "num_ctx": 8192
        }
    }

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        resposta.raise_for_status()
        dados = resposta.json()

        return dados.get("response", "Não consegui gerar uma resposta no momento.")

    except requests.exceptions.ConnectionError:
        return "Não consegui conectar ao Ollama. Verifique se ele está aberto e rodando em http://localhost:11434."

    except requests.exceptions.Timeout:
        return "A resposta demorou mais do que o esperado. Tente novamente ou reduza o tamanho do contexto enviado ao modelo."

    except requests.exceptions.RequestException as erro:
        return f"Ocorreu um erro ao chamar o Ollama: {erro}"

    except Exception as erro:
        return f"Ocorreu um erro inesperado: {erro}"


# ================== INTERFACE STREAMLIT ================== #

st.set_page_config(
    page_title="Personal IA",
    page_icon="🏋️",
    layout="centered"
)

st.title("🏋️ Personal IA")
st.caption("Assistente inteligente de apoio à montagem, adaptação e acompanhamento de treinos físicos.")

with st.sidebar:
    st.header("Configurações")
    st.write(f"**Modelo Ollama:** `{MODELO}`")
    st.write("**Usuário teste:** Cleiton da Silva")
    st.info(
        "Este agente é uma ferramenta de apoio e não substitui um profissional de Educação Física, médico ou fisioterapeuta."
    )

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

pergunta = st.chat_input("Digite sua dúvida sobre treinamento físico...")

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.write(pergunta)

    with st.spinner("Personal IA está analisando seu contexto..."):
        resposta = perguntar(pergunta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })

    with st.chat_message("assistant"):
        st.write(resposta)