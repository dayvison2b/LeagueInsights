from Champion.ChampionAPI import ChampionAPI
from typing import Optional, List, Dict, Any

class Champion:
    """
    A class for interacting with the Riot API to retrieve information about champions.
    """
    def __init__(self, api_key: str, region: str = "br1"):
        """
        Initialize the Champion instance with the API key and region.

        :param api_key: Your Riot Games API key.
        :param region: Region for API calls. Default is "br1".
        """
        self._api_key = api_key
        self._region = region
        self._champion_info = None
        self._champions_list = None
        self._champion_api = ChampionAPI(self._api_key, region)

    def _format_champion_name(self, champion_name: str) -> str:
        """
        Format the champion name by capitalizing each word.

        :param champion_name: The original champion name.
        :return: Formatted champion name.
        """
        formatted_name = champion_name.title()
        return formatted_name

    def _get_champion_data(self, champion_name: str) -> Dict[str, Any]:
        """
        Get data for the specified champion.

        :param champion_name: The name of the champion.
        :return: Dictionary containing champion data.
        """
        if not hasattr(self, "_champion_info") or self._champion_info is None:
            formatted_champion_name = self._format_champion_name(champion_name)
            self._champion_info = self._champion_api.get_champion(formatted_champion_name)[formatted_champion_name]
        return self._champion_info

    def get_all_champions(self) -> Dict[str, Any]:
        """
        Get information about all champions.

        :return: A dictionary containing information about all champions.
        """
        if not hasattr(self, "_champions_list") or self._champions_list is None:
            self._champions_list = self._champion_api.get_champions()
        return self._champions_list

    def get_champion(self, champion_name: str):
        """
        Get information about a champion.

        :return: A dictionary containing information about the champion.
        """
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(champion_name=formatted_champion_name)

    def get_champion_skins(self, champion_name: str) -> List[Dict[str, Any]]:
        """
        Get information about the skins of a specific champion.

        :param champion_name: The name of the champion.
        :return: List of dictionaries containing skin information.
        """
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("skins")

    def get_champion_info(self, champion_name: str) -> Dict[str, Any]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("info")

    def get_champion_stats(self, champion_name: str) -> Dict[str, Any]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("stats")

    def get_champion_spells(self, champion_name: str) -> Dict[str, Any]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("spells")

    def get_champion_lore(self, champion_name: str) -> str:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("lore")

    def get_champion_tips(self, champion_name: str) -> List[str]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("allytips")

    def get_champion_tags(self, champion_name: str) -> List[str]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("tags")

    def get_champion_passive(self, champion_name: str) -> Dict[str, Any]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(formatted_champion_name).get("passive")
