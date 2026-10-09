import json
from pathlib import Path

from busca import buscar_top_k


def avaliar(pasta_indice: str = "indice", perguntas_path: str = "eval/perguntas.json"):
    """Avalia se os 3 trechos recuperados contêm o documento esperado."""
    perguntas_path = Path(perguntas_path)
    perguntas = json.loads(perguntas_path.read_text(encoding="utf-8"))

    acertos = 0
    resultados = []

    for item in perguntas:
        pergunta = item["pergunta"]
        documento_esperado = item["documento_esperado"]
        chaves = buscar_top_k(pergunta, k=3, pasta_indice=pasta_indice)
        arquivos = [resultado["arquivo"] for resultado in chaves]

        acerto = documento_esperado in arquivos if documento_esperado else False

        if documento_esperado is None:
            acerto = "não encontrei" in " ".join(resultado["texto"].lower() for resultado in chaves).lower()

        if acerto:
            acertos += 1

        resultados.append({
            "pergunta": pergunta,
            "documento_esperado": documento_esperado,
            "arquivos": arquivos,
            "acerto": acerto,
        })

    total = len(perguntas)
    print("Resultado da avaliação")
    print("-" * 80)
    for item in resultados:
        print(f"Pergunta: {item['pergunta']}")
        print(f"Documentos retornados: {item['arquivos']}")
        print(f"Acerto: {'Sim' if item['acerto'] else 'Não'}")
        print()

    print(f"Total: {acertos}/{total}")
    return resultados, acertos, total


if __name__ == "__main__":
    avaliar()
