from typing import Optional, Union, List
from RiotAPIService import RiotAPIService  # Import RiotAPIService module


class Summoner:
    def __init__(self, api_key: str, summoner_name: Optional[str] = None, account_id: Optional[str] = None,
                 summoner_id: Optional[str] = None, region: str = "br1") -> None:
        self._api_key = api_key
        self._summoner_name = summoner_name
        self._account_id = account_id
        self._summoner_id = summoner_id
        self._region = region
        self._summoner_info = None  # To store summoner info
        self._riot_api = RiotAPIService(api_key, region)  # Initialize RiotAPIService instance

    @property
    def account_id(self) -> str:
        return self._get_summoner_info()["accountId"]

    @property
    def summoner_id(self) -> str:
        return self._get_summoner_info()["id"]

    @property
    def summoner_name(self) -> str:
        return self._get_summoner_info()["name"]

    @property
    def summoner_level(self) -> int:
        return self._get_summoner_info().get("summonerLevel", 0)

    @property
    def summoner_info(self) -> int:
        return self._get_summoner_info()

    def _get_summoner_info(self):
        if not self._summoner_info:
            if self._account_id:
                self._summoner_info = self._riot_api.get_summoner_by_account_id(self._account_id)
            elif self._summoner_id:
                self._summoner_info = self._riot_api.get_summoner_by_summoner_id(self._summoner_id)
            elif self._summoner_name:
                self._summoner_info = self._riot_api.get_summoner_by_name(self._summoner_name)
            else:
                raise ValueError("No summoner information provided.")
        return self._summoner_info

    def exists(self) -> bool:
        summoner_info = self._get_summoner_info()
        return summoner_info is not None
