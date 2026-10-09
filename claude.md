Você está construindo um RAG simples, sem banco de dados, em uma aula ao vivo.
Os alunos estão aprendendo. Clareza vale mais que esperteza.

## Antes de escrever código
1. Leia `prd.md` (o que construir) e `spec.md` (como construir).
2. Siga o `plan.md` na ordem. Uma etapa por vez.
3. Ao terminar uma etapa, marque `[x]` no plan.md e pare. Espere o "pode seguir".

## Ambiente
- Comece sempre pela Etapa 0: verifique se Python e pip estão instalados.
- Se faltar algo, diga o que falta, mostre o comando de instalação para o
  sistema do aluno (Windows, Mac ou Linux) e peça confirmação antes de rodar.
- Use um ambiente virtual (`.venv`). Nunca instale pacotes fora dele.

## Como escrever o código
- Python simples, funções pequenas, nomes em português.
- Comente o *porquê*, não o *o quê*.
- Só use as bibliotecas listadas na spec. Precisa de outra? Pergunte antes.

## Segurança
- Nunca leia, exiba ou comite o arquivo `.env`.
- Chaves ficam só no `.env`. O `.env.example` mostra os nomes, sem valores.

## Ao final de cada etapa
- Atualize o `CHANGELOG.md` com uma linha sobre o que mudou.
- Explique em 3 frases o que foi feito, como se fosse para um aluno.
