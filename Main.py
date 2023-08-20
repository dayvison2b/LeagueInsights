from Summoner.Summoner import Summoner
from Champion.Champion import Champion
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

# Example usage:
champions = Champion(api_key)
champion_name = "Fizz"
print(f"{champions.get_champion(champion_name)['id']} - {champions.get_champion(champion_name)}")
