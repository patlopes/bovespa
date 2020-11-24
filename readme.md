# Desafio técnico

Durante a execução do desafio a API de finanças da Alpha Vantage não estava retornando os valore de **data** e **meta data** da Bovespa (**^BVSP**) e por isso segui o desenvolvimento consumindo a API de finanças do Yahoo [https://rapidapi.com/apidojo/api/yahoo-finance1/endpoints](https://rapidapi.com/apidojo/api/yahoo-finance1/endpoints)


# Desafios

## Level 1

 - Escrever um programa consulte o número de pontos do bovespa usando o
   alpha vantage (registro simples para obter chave de api aqui:
   [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key))
   
  - Validar o input da API para garantir que ela sempre esteja correta
   
   - Apresentar esse número em uma página html
   
   - Deixar usuário informar qual empresa (listar 10 maiores brasileiras)
   ele quer ver o preço do momento
   
   - Escrever testes

## Level 2

- Modelar Usuário, Empresa e Cotação em um banco de dados relacional (Postgres)

- Escrever as opções do usuário em um banco de dados postgres

## Level 3

- Apresentar esse número em tempo real usando um framework async de python

## Level 4

- Utilizar o Zeromq para criar um pipeline de trabalho que mostra o valor atual e a derivada das empresas selecionadas

## Level 5

- Plotar em tempo real a evolução das cotações no front, suas derivadas (do level 4)  
  
## BÔNUS

### Level 6 (Front)

- implementar leitura dinamica dos valores em framework React ou VueJs

### Level 7 (Front)

- Uso de css-grid e variáveis para tornar design responsivo

- Guardar estado da aplicação em Vuex ou Redux

### Level 8 (Front)

- User um service worker para estimar dinamicamente tendência (reta) das cotações coletadas até agora.

- Apresentar essa reta na tela  
  
  
## Pontos extras para:

1. Documentação da API (swagger, etc)

2. Testes (+1 com Pytest)

3. Async

4. Validação dos inputs

5. Tipagem