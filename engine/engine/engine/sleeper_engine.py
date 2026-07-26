"""
Oracle Sleeper Engine
Version 1.0
"""

class SleeperEngine:

    def __init__(self):
        self.name = "Oracle Sleeper Engine"

    def analyze(self, player):

        def value(column, default=50):
            try:
                return float(player.get(column, default))
            except:
                return default

        power_upside = value("power_upside")
        ownership = value("ownership_score")
        lineup_value = value("lineup_value")
        hidden_power = value("hidden_power")
        consistency = value("consistency_score")

        score = (
            power_upside * 0.30 +
            ownership * 0.20 +
            lineup_value * 0.20 +
            hidden_power * 0.20 +
            consistency * 0.10
        )

        return {
            "Sleeper Score": round(score, 2),
            "Power Upside": power_upside,
            "Ownership": ownership,
            "Lineup Value": lineup_value,
            "Hidden Power": hidden_power,
            "Consistency": consistency
        }