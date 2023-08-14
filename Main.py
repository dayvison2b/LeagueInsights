from Summoner.Summoner import Summoner

# Example usage:
api_key = "RGAPI-13e95eec-482a-4e24-9555-4fc94bcf68b8"
summoner = Summoner(api_key, summoner_name="Perseüs")
summoner._get_summoner_info()
print(summoner._summoner_info)