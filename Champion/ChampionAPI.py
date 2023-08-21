from RiotAPIService import RiotAPIService
from CustomExceptions import NotFoundError
from typing import Dict, Any, List, Union


class ChampionAPI(RiotAPIService):
    """
    This class provides methods for interacting with the Riot API to retrieve information about champions.
    """

    REGION_LANGUAGE_MAPPING = {
        "br1": "pt_BR",
        "eun1": "en_US",
        "euw1": "en_GB",
        "kr": "ko_KR"
    }
    def __init__(self, api_key: str, region: str = "br1"):

        """
        Initialize ChampionAPI with API key and region.

        :param api_key: Your Riot Games API key.
        :param region: Region for API calls. Default is "br1".
        """

        super().__init__(api_key, region)
        self.base_url = "https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}"
        self.version = "11.16.1"  # Current version may vary
        self.language = self.REGION_LANGUAGE_MAPPING.get(region, "en_US")  # Use en_US as default

    def get_champions(self) -> Dict[str, Any]:
        """
        Get information about all champions.
        :return: A dictionary containing information about all champions.
        """
        endpoint = f"{self.base_url}/champion.json".format(version=self.version, language=self.language)
        response = self._make_full_request(endpoint)
        return response.get("data", {})

    def get_champion(self, champion_name) -> Dict[str, Any]:
        """
        Get information about all champions.
        :return: A dictionary containing information about all champions.
        """
        endpoint = f"{self.base_url}/champion/{champion_name}.json".format(version=self.version, language=self.language)
        response = self._make_full_request(endpoint)
        return response.get("data", {})

