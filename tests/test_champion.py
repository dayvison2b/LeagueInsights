import unittest
from Champion.Champion import Champion


class TestChampion(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_api_key"
        self.champion = Champion(api_key=self.api_key)

    def test_get_all_champions(self):
        champions = self.champion.get_all_champions()
        self.assertIsInstance(champions, dict)
        self.assertTrue(champions)

    def test_get_champion(self):
        champion_name = "Ashe"
        champion_info = self.champion.get_champion(champion_name)
        self.assertIsInstance(champion_info, dict)
        self.assertTrue(champion_info)
        self.assertEqual(champion_info["id"], champion_name)

    def test_get_champion_skins(self):
        champion_name = "Ahri"
        skins = self.champion.get_champion_skins(champion_name)
        self.assertIsInstance(skins, list)

    def test_get_champion_info(self):
        champion_name = "Lux"
        info = self.champion.get_champion_info(champion_name)
        self.assertIsInstance(info, dict)

    def test_get_champion_stats(self):
        champion_name = "Garen"
        stats = self.champion.get_champion_stats(champion_name)
        self.assertIsInstance(stats, dict)

    def test_get_champion_spells(self):
        champion_name = "Yasuo"
        spells = self.champion.get_champion_spells(champion_name)
        self.assertIsInstance(spells, list)

    def test_get_champion_lore(self):
        champion_name = "Zed"
        lore = self.champion.get_champion_lore(champion_name)
        self.assertIsInstance(lore, str)

    def test_get_champion_tips(self):
        champion_name = "Annie"
        tips = self.champion.get_champion_tips(champion_name)
        self.assertIsInstance(tips, list)

    def test_get_champion_tags(self):
        champion_name = "Malphite"
        tags = self.champion.get_champion_tags(champion_name)
        self.assertIsInstance(tags, list)

    def test_get_champion_passive(self):
        champion_name = "Jinx"
        passive = self.champion.get_champion_passive(champion_name)
        self.assertIsInstance(passive, dict)

    def test_format_champion_name(self):
        self.assertEqual(self.champion._format_champion_name("ahri"), "Ahri")
        self.assertEqual(self.champion._format_champion_name("zed"), "Zed")
        self.assertEqual(self.champion._format_champion_name("GARen"), "Garen")


if __name__ == "__main__":
    unittest.main(verbosity=2)
