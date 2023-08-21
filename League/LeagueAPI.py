from RiotAPIService import RiotAPIService
from CustomExceptions import NotFoundError
from typing import Dict, Any, List, Union


class LeagueAPI(RiotAPIService):
    def __init__(self, api_key: str, region: str = "br1"):
        super().__init__(api_key, region)

    def get_league_entries(self, tier: str, division: str, queue: str, page: int = 1):
        endpoint = f"league/v4/entries/{queue}/{tier}/{division}"
        params: Dict[str, Any] = {"api_key": self._api_key, "page": page}
        return self._make_request(endpoint, params)
