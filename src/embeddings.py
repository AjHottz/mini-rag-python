import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from ingestao import processar_pasta


MODELO_EMBEDDING = "paraphrase-multilingual-MiniLM-L12-v2"


def gerar_indice(
    pasta_entrada: str | Path = "data/amostras",
    pasta_saida: str | Path = "indice",
    tamanho_chunk: int = 800,
    sobreposicao: int = 100,
):
    """Lê os chunks, gera vetores e salva o índice em disco."""
    chunks = processar_pasta(pasta_entrada, tamanho_chunk=tamanho_chunk, sobreposicao=sobreposicao)

    if not chunks:
        raise ValueError(f"Nenhum texto foi encontrado em {pasta_entrada}.")

    modelo = SentenceTransformer(MODELO_EMBEDDING)
    textos = [chunk["texto"] for chunk in chunks]
    vetores = modelo.encode(textos, convert_to_numpy=True, normalize_embeddings=False)

    pasta_saida = Path(pasta_saida)
    pasta_saida.mkdir(parents=True, exist_ok=True)

    np.save(pasta_saida / "vetores.npy", np.asarray(vetores, dtype=np.float32))

    with open(pasta_saida / "chunks.json", "w", encoding="utf-8") as arquivo:
        json.dump(chunks, arquivo, ensure_ascii=False, indent=2)

    print(f"Total de chunks: {len(chunks)}")
    print(f"Formato do vetor: {np.asarray(vetores).shape}")
    print(f"Arquivo salvo: {pasta_saida / 'vetores.npy'}")
    print(f"Arquivo salvo: {pasta_saida / 'chunks.json'}")

    return chunks, np.asarray(vetores, dtype=np.float32)


if __name__ == "__main__":
    gerar_indice()
