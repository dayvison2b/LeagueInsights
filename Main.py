from Summoner.Summoner import Summoner
from Champion.Champion import Champion
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

# Example usage:
champions = Champion(api_key)
print(champions.get_champion("Fizz"))
