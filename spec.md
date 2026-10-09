## Ambiente
- Python 3.11 ou superior. Verificar com `python --version` (ou `python3 --version`).
- Se não houver Python:
  - Windows: `winget install Python.Python.3.12`
  - Mac: `brew install python@3.12`
  - Linux (Ubuntu): `sudo apt install python3 python3-venv python3-pip`
- Criar ambiente virtual: `python -m venv .venv`
- Dependências em `requirements.txt`.
- Na primeira execução, o modelo de embedding é baixado (~120 MB). Precisa de internet.

## Bibliotecas
| Biblioteca | Para quê |
|---|---|
| streamlit | Tela de upload e chat |
| pypdf | Ler PDFs |
| sentence-transformers | Gerar embeddings no próprio computador |
| numpy | Guardar vetores e calcular similaridade |
| anthropic | Gerar a resposta final |
| python-dotenv | Ler o `.env` |

## Variáveis (`.env`)

ANTHROPIC_API_KEY=
MODELO_CHAT=claude-haiku-4-5-20251001


## O caminho de um documento
1. **Leitura** — aceita `.pdf`, `.txt` e `.md`. Extrai o texto puro.
2. **Chunking** — corta em pedaços de 800 caracteres, com 100 de sobreposição
   (para não partir uma ideia no meio). Cada pedaço guarda o nome do arquivo.
3. **Embedding** — cada pedaço vira um vetor com o modelo
   `paraphrase-multilingual-MiniLM-L12-v2` (entende português, gera 384 números).
4. **Índice** — vetores em `indice/vetores.npy`, textos em `indice/chunks.json`.
   Sem banco: é só arquivo.

## O caminho de uma pergunta
1. A pergunta vira vetor, com o mesmo modelo.
2. Similaridade de cosseno contra todos os vetores do índice.
3. Pega os 3 pedaços mais parecidos (top-k = 3).
4. Envia pergunta + 3 pedaços ao modelo de chat, com a instrução:
   "Responda só com base nos trechos. Se não estiver neles, diga que não encontrou."
5. Mostra a resposta e, abaixo, os 3 trechos com arquivo e nota de similaridade.

## Avaliação
- `src/avaliar.py` roda as perguntas de `eval/perguntas.json`.
- **Acerto** = o documento esperado aparece entre os 3 trechos recuperados.
- Pergunta com `documento_esperado: null` acerta se a resposta disser que não encontrou.
- Resultado: tabela no terminal + total (ex.: 4/5).

## Organização

src/
├── ingestao.py    leitura e chunking
├── embeddings.py  gera os vetores
├── busca.py       índice e similaridade
├── app.py         tela Streamlit
└── avaliar.py     roda o eval
