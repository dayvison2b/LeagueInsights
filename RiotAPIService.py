from typing import Dict, Any

import requests


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

    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make a request to the Riot API.
        :param endpoint: API endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        url = f"{self._base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the response is not successful
        return response.json()

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
        params: dict[str, str] = {"api_key": self._api_key}
        return self._make_request(endpoint, params=params)
