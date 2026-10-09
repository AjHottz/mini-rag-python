from pathlib import Path

from pypdf import PdfReader

TAMANHO_CHUNK = 800
SOBREPOSICAO = 100


def ler_texto_do_arquivo(caminho: Path) -> str:
    """Extrai o texto puro de um arquivo PDF, TXT ou MD."""
    extensao = caminho.suffix.lower()

    if extensao == ".pdf":
        leitor = PdfReader(str(caminho))
        paginas = []
        for pagina in leitor.pages:
            texto = pagina.extract_text() or ""
            paginas.append(texto)
        return "\n".join(paginas).strip()

    return caminho.read_text(encoding="utf-8").strip()


def dividir_em_chunks(texto: str, tamanho: int = TAMANHO_CHUNK, sobreposicao: int = SOBREPOSICAO):
    """Corta o texto em pedaços com sobreposição para manter contexto."""
    if not texto:
        return []

    if len(texto) <= tamanho:
        return [texto.strip()]

    chunks = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho
        pedaco = texto[inicio:fim].strip()
        if pedaco:
            chunks.append(pedaco)

        if fim >= len(texto):
            break

        inicio += max(1, tamanho - sobreposicao)

    return chunks


def processar_pasta(pasta: str | Path, tamanho_chunk: int = TAMANHO_CHUNK, sobreposicao: int = SOBREPOSICAO):
    """Lê todos os arquivos suportados e imprime a contagem de chunks por arquivo."""
    pasta = Path(pasta)
    arquivos = sorted(pasta.iterdir())

    todos_os_chunks = []

    for arquivo in arquivos:
        if not arquivo.is_file():
            continue

        if arquivo.suffix.lower() not in {".pdf", ".txt", ".md"}:
            continue

        texto = ler_texto_do_arquivo(arquivo)
        chunks = dividir_em_chunks(texto, tamanho=tamanho_chunk, sobreposicao=sobreposicao)

        for indice, pedaco in enumerate(chunks):
            todos_os_chunks.append(
                {
                    "arquivo": arquivo.name,
                    "indice": indice,
                    "texto": pedaco,
                }
            )

        print(f"{arquivo.name}: {len(chunks)} chunks")

    if todos_os_chunks:
        exemplo = todos_os_chunks[0]
        print("\nExemplo:")
        print(f"Arquivo: {exemplo['arquivo']}")
        print(f"Chunk {exemplo['indice']}: {exemplo['texto'][:250]}...")

    return todos_os_chunks


if __name__ == "__main__":
    processar_pasta("data/amostras")
