from League.LeagueAPI import LeagueAPI


class League:
    def __init__(self, api_key: str, region: str = "br1"):
        self._api = LeagueAPI(api_key, region)

    def get_league_entries(self, tier: str, division: str, queue: str, page: int = 1):
        return self._api.fetch_league_entries(tier, division, queue, page)

    def get_league_entries_by_summoner(self, summoner_id: str):
        return self._api.fetch_entries_by_summoner(summoner_id)

    def get_challenger_league(self, queue: str):
        return self._api.fetch_challenger_league(queue)

    def get_grandmaster_league(self, queue: str):
        return self._api.fetch_grandmaster_league(queue)

    def get_master_league(self, queue: str):
        return self._api.fetch_master_league(queue)
