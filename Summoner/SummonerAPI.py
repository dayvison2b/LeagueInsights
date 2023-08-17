from RiotAPIService import RiotAPIService
from CustomExceptions import SummonerNotFoundError
from typing import Dict, Any, List, Union


class SummonerAPI(RiotAPIService):
    def __init__(self, api_key: str, region: str = "br1"):
        super().__init__(api_key, region)

    def get_summoner_by_name(self, summoner_name: str) -> Dict[str, Any]:
        """
        Get summoner information by summoner name.
        :param summoner_name: The summoner's name.
        :return: Summoner information.
        """
        endpoint = f"summoner/v4/summoners/by-name/{summoner_name}"
        params: Dict[str, Any] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)

    def get_summoner_by_account_id(self, account_id: str) -> Dict[str, Any]:
        """
        Get summoner information by account ID.
        :param account_id: The summoner's account ID.
        :return: Summoner information.
        """
        endpoint = f"summoner/v4/summoners/by-account/{account_id}"
        params: Dict[str, Any] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)

    def get_summoner_by_summoner_id(self, summoner_id: str) -> Dict[str, Any]:
        """
        Get summoner information by summoner ID.
        :param summoner_id: The summoner's ID.
        :return: Summoner information.
        """
        endpoint = f"summoner/v4/summoners/{summoner_id}"
        params: dict[str, Any] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)

    def get_current_match(self, summoner_id) -> Dict:
        endpoint = f"spectator/v4/active-games/by-summoner/{summoner_id}"
        params: dict[str, Any] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)

    def get_masteries(self, summoner_id) -> dict[str, Any]:
        endpoint = f"champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
        params: dict[str, Any] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)

    def get_match_ids_by_puuid(self, puuid: str, start: int = 0, count: int = 20) -> List[str]:
        endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"

        url = f"https://americas.api.riotgames.com{endpoint}"
        params: dict[str, Union[int, str]] = {
            "api_key": self._api_key,
            "start": start,
            "count": count
        }
        return self._make_full_request(url, params=params)

    def get_match_details_by_id(self, match_id: str):
        endpoint = f"/lol/match/v5/matches/{match_id}"
        url = f"https://americas.api.riotgames.com{endpoint}"
        params: dict[str, Any] = {"api_key": self._api_key}
        return self._make_full_request(url, params=params)
