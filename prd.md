## Problema
Informações da empresa ficam espalhadas em documentos longos.
Encontrar uma resposta exige abrir arquivo por arquivo.

## Para quem
Qualquer pessoa que precisa consultar documentos internos sem ler tudo.

## O que o produto faz
1. A pessoa sobe um ou mais arquivos.
2. O sistema processa e avisa quando está pronto.
3. A pessoa faz uma pergunta em um chat.
4. O sistema responde **e mostra os trechos usados**, com o nome do arquivo.

## Por que mostrar os trechos
É o objetivo da aula: enxergar a busca vetorial acontecendo,
não só receber uma resposta pronta.

## Fora do escopo (nesta versão)
- Banco de dados (vetores ficam salvos em arquivo)
- Login e múltiplos usuários
- Deploy na internet

## Como saberemos que deu certo
- Funciona com os documentos de `data/amostras/`.
- Acerta pelo menos 4 das 5 perguntas de `eval/perguntas.json`.
- Quando a resposta não está nos documentos, diz que não encontrou.
