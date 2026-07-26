"""
Oracle Matchup Engine
Version 1.0
"""


class MatchupEngine:

    def __init__(self):
        self.name = "Oracle Matchup Engine"

    def analyze(
        self,
        hitter,
        pitcher,
        pitch_match_score,
        zone_match_score,
        platoon_score,
        arsenal_score,
        movement_score,
    ):

        matchup_score = (
            pitch_match_score * 0.30
            + zone_match_score * 0.25
            + platoon_score * 0.20
            + arsenal_score * 0.15
            + movement_score * 0.10
        )

        return {
            "Hitter": hitter,
            "Pitcher": pitcher,
            "Matchup Score": round(matchup_score, 2),
            "Status": "Complete",
        }


if __name__ == "__main__":

    engine = MatchupEngine()

    print(
        engine.analyze(
            "Aaron Judge",
            "Tarik Skubal",
            94,
            91,
            88,
            90,
            86,
        )
    )