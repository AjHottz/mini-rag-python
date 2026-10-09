import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

from busca import buscar_top_k

load_dotenv()


def gerar_resposta(pergunta: str, top_k: int = 3):
    """Busca os trechos mais relevantes e pede uma resposta ao modelo de chat."""
    resultados = buscar_top_k(pergunta, k=top_k)

    contexto = "\n\n".join(
        f"[Arquivo: {item['arquivo']}]\n{item['texto']}" for item in resultados
    )

    prompt = (
        "Responda só com base nos trechos abaixo. "
        "Se a resposta não estiver neles, diga que não encontrou.\n\n"
        f"Pergunta: {pergunta}\n\nTrechos:\n{contexto}"
    )

    cliente = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    modelo = os.getenv("MODELO_CHAT", "claude-haiku-4-5-20251001")

    resposta = cliente.messages.create(
        model=modelo,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    texto = resposta.content[0].text
    return texto, resultados


if __name__ == "__main__":
    pergunta = "Qual o prazo do reembolso?"
    texto, resultados = gerar_resposta(pergunta)
    print(texto)
    print("\nTrechos usados:")
    for item in resultados:
        print(f"- {item['arquivo']} | score={item['score']:.4f}")
