from RiotAPIService import RiotAPIService


class LeagueAPI(RiotAPIService):
    ENDPOINTS = {
        "entries": "league/v4/entries/{queue}/{tier}/{division}",
        "entries_by_summoner": "league/v4/entries/by-summoner/{summoner_id}",
        "challenger_league": "league/v4/challengerleagues/by-queue/{queue}",
        "grandmaster_league": "league/v4/grandmasterleagues/by-queue/{queue}",
        "master_league": "league/v4/masterleagues/by-queue/{queue}",
    }

    def __init__(self, api_key: str, region: str = "br1"):
        super().__init__(api_key, region)

    def fetch_league_entries(self, tier: str, division: str, queue: str, page: int = 1):
        endpoint = self.ENDPOINTS["entries"].format(queue=queue, tier=tier, division=division)
        params = {"api_key": self._api_key, "page": page}
        return self._make_request(endpoint, params)

    def fetch_entries_by_summoner(self, summoner_id):
        endpoint = self.ENDPOINTS["entries_by_summoner"].format(summoner_id=summoner_id)
        params = {"api_key": self._api_key}
        return self._make_request(endpoint, params)

    def _fetch_league(self, queue: str, league_type: str):
        endpoint = self.ENDPOINTS[league_type].format(queue=queue)
        params = {"api_key": self._api_key}
        return self._make_request(endpoint, params)

    def fetch_challenger_league(self, queue: str):
        return self._fetch_league(queue, "challenger_league")

    def fetch_grandmaster_league(self, queue: str):
        return self._fetch_league(queue, "grandmaster_league")

    def fetch_master_league(self, queue: str):
        return self._fetch_league(queue, "master_league")
