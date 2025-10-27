# Projeto 13: Monitor de Ações da Bolsa de Valores 📈
---
## O Cenário 👨‍💼

Você é a mais nova contratação em uma "Fintech", uma startup de tecnologia financeira. Sua equipe está desenvolvendo um novo dashboard para investidores e precisa de acesso em tempo real aos preços das ações da bolsa de valores brasileira (B3).

Sua primeira tarefa é criar um protótipo, um script em Python, que sirva como "prova de conceito". Ele deve ser capaz de se conectar a uma API pública, buscar a cotação atual de uma ação específica (como a da Petrobras, PETR4) e exibir o valor de forma clara no terminal.

Este script será a base para futuras ferramentas, como dashboards web, alertas de preço e até robôs de investimento.

## 📋 Requisitos da Missão

A equipe de produto precisa de um resultado rápido e funcional. Seu script deve atender aos seguintes requisitos:

1.  **Fazer uma Requisição Web:** Utilizar a biblioteca `requests` do Python para fazer uma chamada (`GET request`) a uma API pública de bolsa de valores.
      * **API Sugerida:** `https://brapi.dev/` (gratuita e sem necessidade de chave para consultas básicas).
2.  **Consultar uma Ação Específica:** O script deve buscar os dados de uma ação conhecida, como `PETR4` (Petrobras).
      * **URL do Endpoint:** `https://brapi.dev/api/quote/PETR4`
3.  **Processar a Resposta JSON:** O script deve ser capaz de "ler" a resposta JSON da API e extrair a informação mais importante: o preço atual da ação (`regularMarketPrice`).
4.  **Exibir o Resultado:** O programa deve imprimir uma mensagem clara e formatada no terminal, como: `COTAÇÃO ATUAL: O valor da ação PETR4 é R$ 38.50`.
5.  **Tratamento de Erros:** O script deve verificar se a comunicação com a API foi bem-sucedida. Se houver um erro (ex: a API está fora do ar), ele deve informar o usuário em vez de quebrar.

## 💡 Roteiro Sugerido para o Sucesso

1.  **Instale a Biblioteca**: Se ainda não tiver, abra o terminal e rode: `pip install requests`.
2.  **Importe a Biblioteca**: No seu arquivo Python, comece com: `import requests`.
3.  **Defina a URL**: Crie uma variável para guardar o endereço da API que você vai consultar.
    ```python
    ticker = 'PETR4'
    url = f'https://brapi.dev/api/quote/{ticker}'
    ```
4.  **Faça a Requisição**: Use o `requests` para "chamar" a URL e guarde a resposta.
    ```python
    response = requests.get(url)
    ```
5.  **Verifique o Status**: Antes de prosseguir, verifique se o pedido deu certo. O código `200` significa "OK".
    ```python
    if response.status_code == 200:
        # Se deu certo, continua...
    else:
        print("Erro ao buscar dados da API.")
    ```
6.  **Converta para JSON**: Transforme a resposta de texto em um dicionário Python para poder manipulá-la.
    ```python
    dados = response.json()
    ```
7.  **Extraia o Preço**: Navegue pela estrutura do dicionário para pegar o valor que você precisa. A resposta da Brapi vem dentro de uma lista chamada `results`.
    ```python
    # Acessa o primeiro item da lista 'results' e depois a chave 'regularMarketPrice'
    preco = dados['results'][0]['regularMarketPrice']
    ```
8.  **Imprima o Resultado Final**: Use uma f-string para exibir a informação de forma amigável.
    ```python
    print(f"COTAÇÃO ATUAL: O valor da ação {ticker} é R$ {preco:.2f}")
    ```