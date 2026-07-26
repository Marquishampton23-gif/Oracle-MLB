"""
Oracle Opportunity Engine
Version 2.0
"""


class OpportunityEngine:

    def __init__(self):
        self.name = "Oracle Opportunity Engine"

    def analyze(self, player):

        def value(column, default=50):
            try:
                return float(player.get(column, default))
            except:
                return default

        lineup_spot = value("lineup_spot")
        park_factor = value("park_factor")
        weather = value("weather_score")
        bullpen = value("bullpen_score")
        positioning = value("positioning_score")

        score = (
            lineup_spot * 0.30 +
            park_factor * 0.25 +
            weather * 0.15 +
            bullpen * 0.15 +
            positioning * 0.15
        )

        return {
            "Opportunity Score": round(score, 2),
            "Lineup": lineup_spot,
            "Park": park_factor,
            "Weather": weather,
            "Bullpen": bullpen,
            "Positioning": positioning
        }