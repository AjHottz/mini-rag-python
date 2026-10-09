import json
from pathlib import Path

import numpy as np
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

MODELO_EMBEDDING = "paraphrase-multilingual-MiniLM-L12-v2"


def carregar_indice(pasta_indice: str | Path = "indice"):
    """Carrega os vetores e os chunks salvos em disco."""
    pasta = Path(pasta_indice)
    vetores = np.load(pasta / "vetores.npy")
    with open(pasta / "chunks.json", "r", encoding="utf-8") as arquivo:
        chunks = json.load(arquivo)
    return vetores, chunks


def similaridade_cosseno(vetor_1: np.ndarray, vetor_2: np.ndarray) -> float:
    """Calcula a similaridade de cosseno entre dois vetores."""
    denominador = norm(vetor_1) * norm(vetor_2)
    if denominador == 0:
        return 0.0
    return float(np.dot(vetor_1, vetor_2) / denominador)


def buscar_top_k(pergunta: str, k: int = 3, pasta_indice: str | Path = "indice"):
    """Busca os k chunks mais parecidos com a pergunta."""
    vetores, chunks = carregar_indice(pasta_indice)
    modelo = SentenceTransformer(MODELO_EMBEDDING)

    pergunta_vetor = modelo.encode([pergunta], convert_to_numpy=True, normalize_embeddings=False)[0]

    resultados = []
    for indice, chunk in enumerate(chunks):
        score = similaridade_cosseno(pergunta_vetor, vetores[indice])
        resultados.append({
            "indice": indice,
            "arquivo": chunk["arquivo"],
            "texto": chunk["texto"],
            "score": score,
        })

    resultados_ordenados = sorted(resultados, key=lambda item: item["score"], reverse=True)
    return resultados_ordenados[:k]


if __name__ == "__main__":
    pergunta = "Qual o prazo do reembolso?"
    resultados = buscar_top_k(pergunta)
    for item in resultados:
        print(f"Arquivo: {item['arquivo']}")
        print(f"Score: {item['score']:.4f}")
        print(item['texto'][:300])
        print("-" * 80)
