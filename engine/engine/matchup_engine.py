"""
Oracle Pitch Attack Engine
"""

class MatchupEngine:

    def analyze(self, player):

        def value(*columns, default=0):
            for column in columns:
                if column in player:
                    try:
                        return float(player[column])
                    except:
                        pass
            return default

        # Hitter production vs pitch types
        fastball = value(
            "fastball_run_value",
            "fastball_xwoba",
            "fastball_slug"
        )

        breaking = value(
            "breaking_run_value",
            "breaking_xwoba",
            "breaking_slug"
        )

        offspeed = value(
            "offspeed_run_value",
            "offspeed_xwoba",
            "offspeed_slug"
        )

        # Pitch quality
        movement = value(
            "horizontal_break",
            "induced_vertical_break"
        )

        spin = value(
            "spin_rate",
            "active_spin"
        )

        matchup_score = (
            fastball * 0.30 +
            breaking * 0.25 +
            offspeed * 0.20 +
            movement * 0.15 +
            spin * 0.10
        )

        return {
            "Matchup Score": round(matchup_score, 2),
            "Fastball": fastball,
            "Breaking": breaking,
            "Offspeed": offspeed,
            "Movement": movement,
            "Spin": spin
        }