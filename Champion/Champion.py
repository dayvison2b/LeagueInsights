from Champion.ChampionAPI import ChampionAPI
from typing import Optional, List, Dict, Any


class Champion:
    def __init__(self, api_key: str, champion_name: str = None, champion_id: int = None, region: str = "br1"):
        self._api_key = api_key
        self._champion_name = champion_name
        self._champion_id = champion_id
        self._region = region
        self._champion_info = None
        self._champions_list = None
        self._champion_api = ChampionAPI(self._api_key, region)

    def get_champions_list(self) -> Dict[str, Any]:
        if not self._champions_list:
            self._champions_list = self._champion_api.get_champions()
        return self._champions_list

    def get_champion(self, champion_name: str):
        if not self._champion_info:
            self._champion_info = self._champion_api.get_champion(champion_name=champion_name)
        return self._champion_info
