# ces22-game
Projeto de Jogo utilizando pygame para a disciplina CES 22 do ITA - Programação Orientada a Objetos

Documentação

O Jogo 2^n plus é um jogo baseado no jogo 2048, que consiste de uma tabela 4x4, que inicialmente está praticamente vazia com apenas alguns números '2' em posições aleatórias. A cada rodada, em uma casa vazia aleatória irá aparecer um novo número, que pode ser um '2' ou um '4' e, utilizando das setas do teclado, todas as peças que estão no jogo se movimentam na direção teclada. Se duas peças tiverem o mesmo número elas vão se unir e no lugar aparecerá apenas uma peça com valor igual à soma das duas.

Dessa forma, perceba que no jogo haverá apenas potências de 2 e a ideia do jogo é conseguir a maior potência de 2 possível, antes que a tabela fique cheia e não seja mais possível uma movimentação.

Na nossa versão, implementamos 3 fases. 
- A fase 1 é puramente a implementação do jogo 2048 em si, com suas funcionalidades básicas, apenas adicionando a possibilidade de reiniciar  voltar para a tela inciial do jogo.

- A fase 2 adiciona uma dificuldade extra em relação ao tempo total de jogo, ou seja, o jogador tem até determinado tempo (definido no código) para rodar e se passar desse tempo, terá game over. O tempo passado desde o início do jogo é mostrado na tela da fase.

- A fase 3 também adicionar uma dificuldade em relação ao tempo de jogo, mas relacionada a cada jogada. Nesse caso o jogador tem até determinado tempo em cada rodada para decidir sua jogada, caso contrário terá game over. O tempo escolhido foi de 3 segundos para cada jogada e o tempo remanescente em cada jogada é mostrada no tela da fase, sendo atualizado a cada movimento.

Para rodar o jogo, é necessário configurar um ambiente virtual Python.

Para criar o ambiente virtual `env`:
```
python3 -m venv env
```
Na pasta /env/Scripts (quando utilizado windows), rode:

```
activate.bat
```

Agora, com o ambiente virtual rodando, dentro da pasta raiz do projeto, instale os requerimentos:

```
pip install -r requirements.txt
```

Por fim para rodar o jogo:

```
python main.py
```