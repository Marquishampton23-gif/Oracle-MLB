class ScoringEngine:

    def rank_players(self, results):

        results = sorted(
            results,
            key=lambda x: x["Oracle Score"],
            reverse=True
        )

        for player in results:

            score = player["Oracle Score"]

            if score >= 90:
                player["Tier"] = "Tier S"

            elif score >= 85:
                player["Tier"] = "Tier A"

            elif score >= 80:
                player["Tier"] = "Tier B"

            elif score >= 75:
                player["Tier"] = "Sleeper"

            else:
                player["Tier"] = "Deep Sleeper"

        return results