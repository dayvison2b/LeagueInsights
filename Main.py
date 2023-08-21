from League.League import League
from Summoner.Summoner import Summoner
from Champion.Champion import Champion
import json
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

league = League(api_key)



#if __name__ == "__main__":
    #asyncio.run(main())
