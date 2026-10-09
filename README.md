# Mini RAG - Retrieval-Augmented Generation

Este é um projeto simples de RAG construído com Python, utilizando uma interface web em [Streamlit](https://streamlit.io/) e a API da [Anthropic (Claude)](https://www.anthropic.com/) para geração de respostas. A recuperação de informações é feita localmente utilizando embeddings e cálculo de similaridade de cosseno com Numpy, sem a necessidade de um banco de dados vetorial externo.

## 🚀 Funcionalidades

- **Upload de Documentos:** Suporta a ingestão de arquivos `.txt`, `.md` e `.pdf`.
- **Processamento e Chunking:** Extrai o texto dos documentos, dividindo-os em trechos (chunks) de 800 caracteres com 100 caracteres de sobreposição, preservando a rastreabilidade do arquivo de origem.
- **Embeddings Locais:** Utiliza o modelo `paraphrase-multilingual-MiniLM-L12-v2` via `sentence-transformers` para gerar embeddings localmente. É capaz de entender perguntas em português.
- **Busca por Similaridade:** Armazena os vetores gerados em arquivos Numpy (`.npy`) e textos em JSON local. Utiliza similaridade de cosseno para encontrar os trechos mais relevantes à pergunta feita.
- **Chat Interativo:** Interface web criada com Streamlit, exibindo não só a resposta gerada pelo modelo da Anthropic (com base nos trechos recuperados), mas também os arquivos fontes utilizados e sua pontuação de similaridade.
- **Avaliação (Eval):** Script incluído (`src/avaliar.py`) para validar se a recuperação de dados está funcionando corretamente conforme um conjunto de testes predefinido.

## 🛠️ Tecnologias e Bibliotecas

| Biblioteca | Propósito |
|---|---|
| `streamlit` | Interface web interativa para upload e chat |
| `pypdf` | Extração de texto de PDFs |
| `sentence-transformers` | Geração de embeddings vetoriais locais |
| `numpy` | Armazenamento de vetores e cálculo matemático (cosseno) |
| `anthropic` | Chamadas para o modelo LLM (ex: Claude) para geração das respostas |
| `python-dotenv` | Gerenciamento de variáveis de ambiente (`.env`) |

## ⚙️ Instalação e Configuração

### 1. Pré-requisitos
Certifique-se de possuir **Python 3.11 ou superior**. Verifique a versão instalada:
```bash
python --version
```

### 2. Configurar o Ambiente Virtual
Clone o repositório e crie um ambiente virtual na raiz do projeto:
```bash
python -m venv .venv
```

Ative o ambiente virtual:
- **Windows:** `.venv\Scripts\activate`
- **Linux/Mac:** `source .venv/bin/activate`

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```
> **Aviso:** Na primeira execução, o modelo de embedding (~120 MB) será baixado. Certifique-se de possuir conexão com a internet.

### 4. Variáveis de Ambiente
Renomeie ou crie um arquivo `.env` na raiz do projeto contendo as seguintes variáveis:
```ini
ANTHROPIC_API_KEY=sua_chave_de_api_da_anthropic_aqui
MODELO_CHAT=claude-haiku-4-5-20251001
```

## 🚀 Como Usar

Para iniciar a interface web do chat:
```bash
streamlit run src/app.py
```
Acesse o sistema no navegador através do endereço exibido no terminal (geralmente `http://localhost:8501`).

## 🧪 Avaliação
Para rodar a rotina de testes (eval) de recuperação de dados (verifica se os documentos esperados estão entre os top 3 recuperados):
```bash
python src/avaliar.py
```

## 📂 Organização do Projeto

```text
/
├── src/
│   ├── app.py         # Tela principal no Streamlit
│   ├── busca.py       # Índice e cálculo de similaridade
│   ├── embeddings.py  # Geração dos vetores
│   ├── ingestao.py    # Leitura e chunking de documentos
│   └── avaliar.py     # Script de execução dos testes de eval
├── eval/              # Perguntas e definições para avaliação
├── data/ / dados/     # Diretório para armazenamento dos documentos brutos
├── indice/            # Armazenamento do índice vetorial (arquivos .npy e .json)
├── .env.example       # Exemplo de configuração
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```
