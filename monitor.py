import requests


ticker = 'PETR4'
url = f'https://brapi.dev/api/quote/{ticker}'


try:
    response = requests.get(url)


    if response.status_code == 200:
        dados = response.json()

  
        if 'results' in dados and len(dados['results']) > 0:
            preco = dados['results'][0]['regularMarketPrice']
            nome = dados['results'][0]['longName']
            hora = dados['results'][0]['regularMarketTime']

            print("=" * 60)
            print(f"COTAÇÃO ATUAL ({ticker}) - {nome}")
            print(f"Preço Atual: R$ {preco:.2f}")
            print(f"Horário da Última Atualização: {hora}")
            print("=" * 60)
        else:
            print("Nenhum resultado encontrado para o ticker informado.")
    else:
        print(f"Erro na requisição. Código HTTP: {response.status_code}")


except requests.exceptions.RequestException as e:
    print(f"Erro ao tentar conectar à API: {e}")
