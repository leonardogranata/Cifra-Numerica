# Encriptador de Mensagens em Python

Este projeto é um simples encriptador de mensagens em Python que converte cada letra para sua posição correspondente no alfabeto. Espaços são representados por uma barra `/`.

---

## Funcionalidades

- Converte letras (maiúsculas ou minúsculas) em números conforme sua posição no alfabeto:
  - A → 1, B → 2, ..., Z → 26
- Espaços são convertidos em `/`
- Verifica se a entrada contém apenas letras e espaços
- Exibe uma observação se a mensagem tiver espaços

---

## Regras

- ✅ Permitidos:
  - Letras (maiúsculas ou minúsculas)
  - Espaços
- ❌ Não Permitidos:
  - Números
  - Pontuação (.,!?)
  - Símbolos (@, #, $, etc.)

---
## Exemplo de uso

```bash
Digite a mensagem a ser encriptada: ola mundo
15 12 1 / 13 21 14 4 15
OBS: o '/' significa que a mensagem contém um espaço

