import asyncio
import sqlite3
import datetime
import json
from League.League import League
from Summoner.Summoner import Summoner


async def fetch_summoner_names(league, tier, division, queue, page):
    league_entries = league.get_league_entries(tier, division, queue, page)
    return [entry["summonerName"] for entry in league_entries]


def fetch_summoner_info(summoner, summoner_name):
    summoner_info = summoner.get_summoner_by_name(summoner_name)
    return summoner_info


async def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
        api_key = config['api_key']

    league = League(api_key)
    summoner = Summoner(api_key)

    summoner_names = []
    requests_made = 1

    elo_divisions = [
        ("IRON", "I")  # , ("IRON", "II"), ("IRON", "III"), ("IRON", "IV"),
        # ("BRONZE", "I"), ("BRONZE", "II"), ("BRONZE", "III"), ("BRONZE", "IV")
    ]
    for tier, division in elo_divisions:
        page = 1
        while True:
            try:
                current_time = datetime.datetime.now()
                print(f"Requisição {requests_made} iniciada: {current_time}")

                names = await fetch_summoner_names(league, tier, division, "RANKED_SOLO_5x5", page)
                if not names:
                    break

                # conn = sqlite3.connect("summoners.db")
                # cursor = conn.cursor()
                # cursor.execute("CREATE TABLE IF NOT EXISTS summoners (name TEXT, level TEXT, profileIcon TEXT)")
                #
                for summoner_name in names:
                    print(summoner_name)
                    summoner_info = fetch_summoner_info(summoner, summoner_name)
                    print(summoner_info)
                #
                #     cursor.execute("INSERT INTO summoners (name, level, profileIcon) VALUES (?, ?, ?)",
                #                    (summoner_info['name'], summoner_info['summonerLevel'],
                #                     summoner_info['profileIconId']))
                # conn.commit()
                # conn.close()

                print(f"Requisição {requests_made} finalizada: {current_time}")
                requests_made += 1
                page += 1

            except Exception as e:
                print(f"An error occurred: {e}")
                quit()



if __name__ == "__main__":
    asyncio.run(main())
