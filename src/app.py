import os
from pathlib import Path

import streamlit as st

from busca import buscar_top_k
from embeddings import gerar_indice


def limpar_pasta_documentos(pasta: Path):
    pasta.mkdir(parents=True, exist_ok=True)
    for item in pasta.iterdir():
        if item.is_file():
            item.unlink()


def processar_uploads(arquivos):
    pasta = Path("data/amostras")
    limpar_pasta_documentos(pasta)

    for arquivo in arquivos:
        caminho = pasta / arquivo.name
        caminho.write_bytes(arquivo.getvalue())

    gerar_indice(pasta, "indice")
    st.session_state["indice_pronto"] = True
    st.session_state["mensagem_status"] = "Documentos processados com sucesso."


def responder_pergunta(pergunta: str):
    if not pergunta.strip():
        return

    resultados = buscar_top_k(pergunta, k=3)
    contexto = "\n\n".join(
        f"[Arquivo: {item['arquivo']}]\n{item['texto']}" for item in resultados
    )

    prompt = (
        "Responda só com base nos trechos abaixo. "
        "Se a resposta não estiver neles, diga que não encontrou.\n\n"
        f"Pergunta: {pergunta}\n\nTrechos:\n{contexto}"
    )

    cliente = st.session_state.get("cliente_anthropic")
    if cliente is None:
        st.session_state["ultima_resposta"] = (
            "A chave da Anthropic não está configurada. "
            "Edite o arquivo .env com ANTHROPIC_API_KEY para responder."
        )
        st.session_state["ultimos_resultados"] = resultados
        return

    modelo = os.getenv("MODELO_CHAT", "claude-haiku-4-5-20251001")
    resposta = cliente.messages.create(
        model=modelo,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    st.session_state["ultima_resposta"] = resposta.content[0].text
    st.session_state["ultimos_resultados"] = resultados


st.set_page_config(page_title="RAG de documentos", page_icon="📚")

st.title("RAG de documentos internos")

if "indice_pronto" not in st.session_state:
    st.session_state["indice_pronto"] = False
if "ultima_resposta" not in st.session_state:
    st.session_state["ultima_resposta"] = ""
if "ultimos_resultados" not in st.session_state:
    st.session_state["ultimos_resultados"] = []
if "mensagem_status" not in st.session_state:
    st.session_state["mensagem_status"] = ""

if "cliente_anthropic" not in st.session_state:
    from anthropic import Anthropic
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    st.session_state["cliente_anthropic"] = Anthropic(api_key=api_key) if api_key else None

with st.sidebar:
    st.subheader("Documentos")
    arquivos = st.file_uploader(
        "Suba arquivos PDF, TXT ou MD",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
    )

    if st.button("Processar documentos") and arquivos:
        processar_uploads(arquivos)

    if st.session_state["mensagem_status"]:
        st.success(st.session_state["mensagem_status"])

if not st.session_state["indice_pronto"]:
    st.info("Faça o upload de documentos e clique em Processar documentos para criar o índice.")

pergunta = st.chat_input("Faça uma pergunta sobre os documentos")

if pergunta:
    responder_pergunta(pergunta)

if st.session_state["ultima_resposta"]:
    st.markdown("### Resposta")
    st.write(st.session_state["ultima_resposta"])

    if st.session_state["ultimos_resultados"]:
        with st.expander("Trechos usados"):
            for item in st.session_state["ultimos_resultados"]:
                st.markdown(f"**Arquivo:** {item['arquivo']}")
                st.markdown(f"**Similaridade:** {item['score']:.4f}")
                st.write(item["texto"][:500])
                st.markdown("---")
