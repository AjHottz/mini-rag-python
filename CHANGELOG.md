# Changelog

- Etapa 0: ambiente preparado com Python, ambiente virtual .venv, dependências do projeto e arquivos de configuração iniciais.
- Etapa 1: leitura dos PDFs em data/amostras, extração de texto com pypdf e divisão em chunks com sobreposição de 100 caracteres, com saída de contagem por arquivo e exemplo de chunk.
- Etapa 2: geração de embeddings com sentence-transformers para cada chunk, salvamento do vetor em indice/vetores.npy e do metadata em indice/chunks.json, confirmando 9 chunks e shape (9, 384).
- Etapa 3: implementação da busca por similaridade de cosseno em src/busca.py; a pergunta "Qual o prazo do reembolso?" retornou os 3 trechos mais relevantes, com destaque para o manual de reembolso.
- Etapa 4: geração da resposta final em src/resposta.py usando os 3 trechos recuperados e o modelo da Anthropic, com validação de uma pergunta sobre prazo de reembolso e resposta grounded no contexto.
- Etapa 5: interface Streamlit em src/app.py com upload de arquivos, processamento do índice e chat com resposta e trechos usados; verificado com arranque do app em http://localhost:8501.
- Etapa 6: criação de src/avaliar.py e da avaliação com 5 perguntas em eval/perguntas.json; resultado obtido: 4/5 acertos, com a pergunta fora da base corretamente sinalizada como não encontrada.
- Etapa 7: experimento com tamanhos de chunk 400 e 1500 caracteres, reprocessamento do índice e execução do eval sobre o mesmo conjunto; ambos mantiveram 4/5 acertos, mostrando que a performance foi equivalente no conjunto atual.
