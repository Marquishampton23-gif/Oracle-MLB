"""
Oracle Matchup Engine
Version 2.0
"""


class MatchupEngine:

    def __init__(self):
        self.name = "Oracle Matchup Engine"

    def analyze(self, player):

        def value(column, default=50):
            try:
                return float(player.get(column, default))
            except:
                return default

        pitch_match = value("pitch_match_score")
        zone_match = value("zone_match_score")
        platoon = value("platoon_score")
        arsenal = value("arsenal_score")
        movement = value("movement_score")

        score = (
            pitch_match * 0.30 +
            zone_match * 0.25 +
            platoon * 0.20 +
            arsenal * 0.15 +
            movement * 0.10
        )

        return {
            "Matchup Score": round(score, 2),
            "Pitch Match": pitch_match,
            "Zone Match": zone_match,
            "Platoon": platoon,
            "Arsenal": arsenal,
            "Movement": movement
        }