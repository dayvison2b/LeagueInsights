import unittest
from RiotAPIService import RiotAPIService
from Summoner import Summoner
from CustomExceptions import NotFoundError
import json

with open('../config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']


class TestRiotPy(unittest.TestCase):
    def setUp(self) -> None:
        # Basic configs to all tests
        self.api_key = api_key
        self.riot_api = RiotAPIService(self.api_key)

    def test_summoner_exists(self):
        self.assertTrue(Summoner.Summoner.summoner_exists(self.api_key, "Perseüs", region="br1"))
        self.assertFalse(Summoner.Summoner.summoner_exists(self.api_key, "NonExistentSummonerTest2231", region="br1"))

    def test_summoner_info(self):
        summoner = Summoner.Summoner(self.api_key, "Perseüs", region="br1")
        self.assertTrue(summoner.summoner_info)
        self.assertEqual(summoner.summoner_name, "Perseüs")
        # SummonerNotFoundError test
        with self.assertRaises(NotFoundError):
            summoner = Summoner.Summoner(self.api_key, summoner_name="NonExistentSummonerTest2231")
            # summoner.summoner_name

    def test_get_match_history(self):
        summoner = Summoner.Summoner(self.api_key, "Perseüs", region="br1")
        self.assertTrue(summoner.summoner_info)
        match_history = summoner.get_match_history()
        self.assertIsInstance(match_history, list)


if __name__ == '__main__':
    unittest.main()
