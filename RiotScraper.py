import asyncio
import sqlite3
import datetime
import json
from League.League import League
from Summoner.Summoner import Summoner
from CustomExceptions import NotFoundError


async def fetch_summoner_names(league, tier, division, queue, page):
    league_entries = league.get_league_entries(tier, division, queue, page)
    return [entry["summonerName"] for entry in league_entries]


def fetch_summoner_info(summoner, summoner_name):
    try:
        summoner_info = [summoner.get_summoner_by_name(summoner_name), summoner.summoner_masteries[0]]
        return summoner_info
    except NotFoundError:
        return False


def create_summoners_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS summoners (id TEXT, name TEXT, level TEXT, profileIcon TEXT, "
                   "mainChampion TEXT, greaterMasterie TEXT, lastPlayTime TEXT)")
    conn.commit()


def insert_summoner_info(conn, summoner_info):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO summoners (id, name, level, profileIcon, mainChampion, greaterMasterie, lastPlayTime) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (summoner_info[0]['id'], summoner_info[0]['name'], summoner_info[0]['summonerLevel'],
                    summoner_info[0]['profileIconId'], summoner_info[1]['championId'],
                    summoner_info[1]['championPoints'], summoner_info[1]['lastPlayTime']))
    conn.commit()


async def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
        api_key = config['api_key']

    league = League(api_key)
    summoner = Summoner(api_key)

    elo_divisions = [
        ("IRON", "I")  # , ("IRON", "II"), ("IRON", "III"), ("IRON", "IV"),
        # ("BRONZE", "I"), ("BRONZE", "II"), ("BRONZE", "III"), ("BRONZE", "IV")
    ]

    conn = sqlite3.connect("summoners.db")
    create_summoners_table(conn)

    requests_made = 1
    for tier, division in elo_divisions:
        page = 1
        while True:
            try:
                current_time = datetime.datetime.now()
                print(f"Requisição {requests_made} iniciada: {current_time}")

                names = await fetch_summoner_names(league, tier, division, "RANKED_SOLO_5x5", page)
                if not names:
                    break

                for summoner_name in names:
                    print(summoner_name)
                    summoner_info = fetch_summoner_info(summoner, summoner_name)
                    print(summoner_info)
                    if summoner_info:
                        insert_summoner_info(conn, summoner_info)

                print(f"Requisição {requests_made} finalizada: {current_time}")
                requests_made += 1
                page += 1

            except Exception as e:
                print(f"An error occurred: {e}")
                quit()

    conn.close()


if __name__ == "__main__":
    asyncio.run(main())
