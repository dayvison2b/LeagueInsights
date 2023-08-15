from typing import Dict, Any, List, Union

import requests
from CustomExceptions import *


class RiotAPIService:
    """
    This class is a module and all classes that need to request from Riot API will instantiate it.
    """

    SUPPORTED_REGIONS = ["br1", "eun1", "euw1", "kr"]

    def __init__(self, api_key: str, region: str = "br1") -> None:
        """
        Initialize RiotAPIService with API key and region.
        :param api_key: Your Riot Games API key.
        :param region: Region for API calls. Default is "br1".
        """
        self._api_key = api_key
        if region not in self.SUPPORTED_REGIONS:
            raise ValueError(f"Unsupported region '{region}'. Supported regions: {', '.join(self.SUPPORTED_REGIONS)}")
        self._region = region
        self._base_url = f"https://{self._region}.api.riotgames.com/lol"

    def _make_request(self, endpoint: str, params: Dict[str, Any] = None):
        """
        Make a request to the Riot API.
        :param endpoint: API endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        url = f"{self._base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise SummonerNotFoundError("Summoner not found.")
            else:
                raise http_error

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

    def _make_full_request(self, url: str, params: Dict[str, Any] = None):
        """
        Make a request to the Riot API with a complete URL.
        :param url: Complete URL including the endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the response is not successful
        return response.json()

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
