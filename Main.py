from Summoner.Summoner import Summoner
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

# Example usage:
summoner = Summoner(api_key)
summoner._get_summoner_info()
#print(summoner._summoner_info)
print(summoner.get_match_history())
