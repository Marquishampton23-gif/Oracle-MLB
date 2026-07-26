import pandas as pd


class DNAEngine:

    def score(self, player):

        score = 0

        if player.get("avg_hit_speed", 0) >= 95:
            score += 20

        if player.get("max_hit_speed", 0) >= 110:
            score += 15

        if player.get("brl_percent", 0) >= 12:
            score += 20

        if player.get("hard_hit_percent", 0) >= 45:
            score += 15

        if player.get("launch_angle", 15) >= 12:
            score += 10

        if player.get("launch_angle", 15) <= 28:
            score += 10

        if player.get("sweet_spot_percent", 0) >= 35:
            score += 10

        return min(score, 100)