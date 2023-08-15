# RiotPy - Biblioteca Python para Requisições à API da Riot Games

A RiotPy é uma biblioteca Python projetada para facilitar o acesso à API da Riot Games, permitindo que desenvolvedores obtenham informações sobre jogadores, partidas, campeões e estatísticas do League of Legends. Esta biblioteca foi criada para oferecer uma alternativa personalizada e flexível às soluções existentes, permitindo que você obtenha os dados necessários de forma simples e eficiente.

## Características Principais

- Recupere informações detalhadas de jogadores, incluindo perfis, estatísticas e histórico de partidas.
- Acesse detalhes completos de partidas, como resultados, estatísticas de jogadores e cronograma.
- Explore informações sobre campeões, como estatísticas, habilidades e skins.
- Facilite as requisições à API da Riot Games com métodos e funcionalidades encapsuladas.

## Instalação

Para começar a usar a RiotPy, siga as etapas abaixo:

1. Instale a biblioteca via pip:

<pre>
pip install riotpy
</pre>

2. Importe a classe Summoner e inicialize-a com a sua chave de API da Riot Games:

```
from riotpy import Summoner

api_key = "SUA_CHAVE_DE_API"
summoner = Summoner(api_key)
```

## Como usar
### Obtendo informações do jogador

```
# Buscar informações do jogador por nome de invocador
summoner_info = summoner.get_summoner_by_name("NomeDoJogador")

# Acessar informações do jogador
print("Nome de Invocador:", summoner_info["name"])
print("Nível:", summoner_info["summonerLevel"])
# ... Outras informações disponíveis
```

### Obtendo histórico de partidas

```
# Buscar histórico de partidas por nome de invocador
match_history = summoner.get_match_history("NomeDoJogador")

# Acessar as últimas partidas
for match in match_history:
    print("Partida:", match["match_id"])
    print("Data:", match["date"])
    print("Resultado:", "Vitória" if match["result"] else "Derrota")
    print()
```
### Obtendo detalhes de uma partida

```
# Buscar detalhes de uma partida pelo ID
match_id = "ID_DA_PARTIDA"
match_details = summoner.get_match_details_by_id(match_id)

# Acessar detalhes da partida
print("Jogadores:")
for player in match_details["participants"]:
    print("Nome:", player["summonerName"])
    print("Campeão:", player["championName"])
    print("Kills:", player["kills"])
    # ... Outras informações disponíveis
```

## Contribuição

A RiotPy é uma biblioteca em constante evolução e você é convidado a contribuir para melhorar seu funcionamento e recursos. Sinta-se à vontade para abrir problemas, enviar solicitações de pull e colaborar em seu desenvolvimento.

