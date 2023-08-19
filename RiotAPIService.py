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
                raise NotFoundError("Summoner not found.")
            else:
                raise http_error

    def _make_full_request(self, url: str, params: Dict[str, Any] = None):
        """
        Make a request to the Riot API with a complete URL.
        It is needed, because some requests require different urls.
        :param url: Complete URL including the endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response is not successful
            return response.json()
        except HTTPError as http_error:
            if http_error.response.status_code == 403:
                raise NotFoundError("Champion not found.")
            else:
                raise http_error

