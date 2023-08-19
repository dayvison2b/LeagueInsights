from Champion.ChampionAPI import ChampionAPI
from typing import Optional, List, Dict, Any


class Champion:
    def __init__(self, api_key: str, region: str = "br1"):
        self._api_key = api_key
        self._region = region
        self._champion_info = None
        self._champions_list = None
        self._champion_api = ChampionAPI(self._api_key, region)

    def _format_champion_name(self, champion_name: str) -> str:
        formatted_name = champion_name.title()
        return formatted_name

    def _get_champion_info(self, champion_name: str) -> Dict[str, Any]:
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._champion_api.get_champion(formatted_champion_name)[formatted_champion_name]


    def _get_champion_data(self, champion_name: str) -> Dict[str, Any]:
        if not hasattr(self, "_champion_info") or self._champion_info is None:
            self._champion_info = self._get_champion_info(champion_name)
        return self._champion_info


    def get_all_champions(self) -> Dict[str, Any]:
        if not hasattr(self, "_champions_list") or self._champions_list is None:
            self._champions_list = self._champion_api.get_champions()
        return self._champions_list

    def get_champion(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self._get_champion_data(champion_name=formatted_champion_name)


    def get_champion_skins(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("skins")

    def get_champion_info(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("info")

    def get_champion_stats(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("stats")

    def get_champion_spells(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("spells")

    def get_champion_lore(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("lore")

    def get_champion_tips(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("allytips")

    def get_champion_tags(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("tags")

    def get_champion_passive(self, champion_name: str):
        formatted_champion_name = self._format_champion_name(champion_name)
        return self.get_champion(formatted_champion_name)[formatted_champion_name].get("passive")