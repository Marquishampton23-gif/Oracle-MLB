"""
Oracle Scoring Engine
Version 1.0
"""

from base_set import BaseSet


class ScoringEngine:

    def __init__(self):
        self.base = BaseSet()

    def weighted_score(self, values, weights):

        total = 0

        for key in values:

            if key in weights:
                total += values[key] * weights[key]

        return round(total, 2)


if __name__ == "__main__":

    engine = ScoringEngine()

    dna = {
        "exit_velocity": 95,
        "barrel_rate": 92,
        "hard_hit_rate": 90,
        "launch_angle": 84,
        "bat_speed": 93,
        "sweet_spot": 86,
        "fly_ball_rate": 88,
    }

    print(
        engine.weighted_score(
            dna,
            BaseSet.DNA_WEIGHTS,
        )
    )