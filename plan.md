Uma etapa por vez. Ao terminar, marque [x] e espere o "pode seguir".

- [x] **Etapa 0 — Ambiente**
  Verificar Python, criar `.venv`, `requirements.txt`, `.gitignore` e `.env.example`.
  Pronto quando: `pip list` mostra as bibliotecas instaladas.

- [x] **Etapa 1 — Leitura e chunking**
  Ler os arquivos de `data/amostras/` e cortar em pedaços.
  Pronto quando: imprime quantos pedaços saíram de cada arquivo e mostra um exemplo.

- [x] **Etapa 2 — Embeddings e índice**
  Transformar os pedaços em vetores e salvar em `indice/`.
  Pronto quando: `vetores.npy` e `chunks.json` existem e o número de linhas bate.

- [x] **Etapa 3 — Busca**
  Receber uma pergunta e devolver os 3 trechos mais parecidos, no terminal.
  Pronto quando: "Qual o prazo do reembolso?" traz um trecho do manual de reembolso.

- [x] **Etapa 4 — Resposta**
  Juntar pergunta + trechos e gerar a resposta com o modelo de chat.
  Pronto quando: responde certo e diz "não encontrei" para algo fora da base.

- [x] **Etapa 5 — Interface**
  Tela Streamlit com upload, botão de processar e chat mostrando os trechos.
  Pronto quando: `streamlit run src/app.py` abre e funciona de ponta a ponta.

- [x] **Etapa 6 — Avaliação**
  Criar `src/avaliar.py` e rodar o eval.
  Pronto quando: mostra a tabela e o total de acertos.

- [x] **Etapa 7 — Experimento**
  Mudar o tamanho do chunk (400 e 1500), reprocessar e rodar o eval de novo.
  Pronto quando: o CHANGELOG registra o resultado de cada tamanho.
