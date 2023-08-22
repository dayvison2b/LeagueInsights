from League.League import League
from Summoner.Summoner import Summoner
from Champion.Champion import Champion
import json
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

summoner = Summoner(api_key)
print(summoner.get_summoner_by_name("Perseüs"))



#if __name__ == "__main__":
    #asyncio.run(main())
