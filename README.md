# API de Pontuações

Esta é uma API simples para gerenciar pontuações de jogadores.

## Endpoints Disponíveis

- `GET /pontuacoes`: Retorna todos os registros de pontuações.
- `GET /pontuacoes/<id>`: Retorna um registro de pontuação específico pelo ID.
- `POST /pontuacoes`: Cria um novo registro de pontuação.
- `PUT /pontuacoes/<id>`: Atualiza um registro de pontuação existente pelo ID.
- `DELETE /pontuacoes/<id>`: Exclui um registro de pontuação pelo ID.

## Estrutura do Registro de Pontuação

Cada registro de pontuação tem a seguinte estrutura:

```json
{
    "id": 1,
    "nome": "antony",
    "tempo": 50,
    "pontuacao": 900
}
