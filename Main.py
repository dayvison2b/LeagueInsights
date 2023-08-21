from League.LeagueAPI import LeagueAPI
from Summoner.Summoner import Summoner
from Champion.Champion import Champion
import json
import asyncio


async def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
        api_key = config['api_key']

    liga = LeagueAPI(api_key)
    league_entries = liga.get_league_entries("BRONZE", "IV", queue="RANKED_SOLO_5x5")
    print(league_entries)


if __name__ == "__main__":
    asyncio.run(main())
