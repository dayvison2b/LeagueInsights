import time
from typing import Dict, Any, List, Union
import requests
from CustomExceptions import *

class RiotAPIService:
    RATE_LIMITS = {
        "requests_per_second": 9,
        "requests_per_two_minutes": 50
    }
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
        self._request_count_seconds_limit = 0
        self._request_count_minutes_limit = 0
        self._last_request_time = 0
        self._minute_limit = time.time()

    def _wait_if_rate_limit_exceeded(self):
        current_time = time.time()
        time_since_last_request = current_time - self._last_request_time

        if time_since_last_request < 1:  # 1 second
            if self._request_count_seconds_limit >= self.RATE_LIMITS["requests_per_second"]:
                time_to_wait = 1 - time_since_last_request
                time.sleep(time_to_wait)
                self._request_count_seconds_limit = 0
            else:
                self._request_count_seconds_limit = 0

        if current_time - self._minute_limit < 100:  # 100 seconds
            if self._request_count_minutes_limit >= self.RATE_LIMITS["requests_per_two_minutes"]:
                time_to_wait = 100 - (current_time - self._minute_limit)
                time.sleep(time_to_wait)
                self._request_count_minutes_limit = 0
                self._minute_limit = time.time()

        if current_time - self._minute_limit > 100 or self._request_count_minutes_limit > self.RATE_LIMITS["requests_per_two_minutes"]:
            self._minute_limit = time.time()
            self._request_count_minutes_limit = 0

    def _make_request(self, endpoint: str, params: Dict[str, Any] = None):
        """
        Make a request to the Riot API.
        :param endpoint: API endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        self._wait_if_rate_limit_exceeded()

        url = f"{self._base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            self._request_count_seconds_limit += 1
            self._request_count_minutes_limit += 1
            self._last_request_time = time.time()
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
        self._wait_if_rate_limit_exceeded()

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response is not successful
            self._request_count_seconds_limit += 1
            self._request_count_minutes_limit += 1
            self._last_request_time = time.time()
            return response.json()
        except HTTPError as http_error:
            if http_error.response.status_code == 403:
                raise NotFoundError("Champion not found.")
            else:
                raise http_error
