"""
Oracle Opportunity Engine
Version 1.0
"""


class OpportunityEngine:

    def __init__(self):
        self.name = "Oracle Opportunity Engine"

    def analyze(
        self,
        lineup_spot,
        park_factor,
        weather_score,
        bullpen_score,
        game_script,
    ):

        opportunity_score = (
            lineup_spot * 0.25
            + park_factor * 0.25
            + weather_score * 0.20
            + bullpen_score * 0.15
            + game_script * 0.15
        )

        return {
            "Opportunity Score": round(opportunity_score, 2),
            "Status": "Complete",
        }


if __name__ == "__main__":

    engine = OpportunityEngine()

    print(
        engine.analyze(
            95,
            90,
            88,
            84,
            92,
        )
    )