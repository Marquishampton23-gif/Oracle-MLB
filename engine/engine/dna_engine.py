"""
Oracle DNA Engine
Version 2.0
"""

import pandas as pd


class DNAEngine:

    def __init__(self):
        self.name = "Oracle DNA Engine"

    def analyze(self, player):

        def value(column, default=50):
            try:
                return float(player.get(column, default))
            except:
                return default

        exit_velocity = value("exit_velocity")
        barrel_rate = value("barrel_rate")
        hard_hit_rate = value("hard_hit_rate")
        launch_angle = value("launch_angle")
        bat_speed = value("bat_speed")
        sweet_spot = value("sweet_spot")
        fly_ball_rate = value("fly_ball_rate")

        score = (
            exit_velocity * 0.20 +
            barrel_rate * 0.25 +
            hard_hit_rate * 0.20 +
            launch_angle * 0.10 +
            bat_speed * 0.10 +
            sweet_spot * 0.05 +
            fly_ball_rate * 0.10
        )

        return {
            "DNA Score": round(score, 2),
            "Exit Velocity": exit_velocity,
            "Barrel Rate": barrel_rate,
            "Hard Hit": hard_hit_rate,
            "Launch Angle": launch_angle,
            "Bat Speed": bat_speed,
            "Sweet Spot": sweet_spot,
            "Fly Ball": fly_ball_rate
        }