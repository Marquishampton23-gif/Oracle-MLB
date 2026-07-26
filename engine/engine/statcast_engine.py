"""
Oracle Statcast Engine
Version 1.0
"""


class StatcastEngine:

    def __init__(self):
        self.name = "Oracle Statcast Engine"

    def analyze(
        self,
        exit_velocity,
        barrel_rate,
        hard_hit_rate,
        launch_angle,
        bat_speed,
        sweet_spot,
        fly_ball_rate,
        pull_air_rate,
    ):

        score = (
            exit_velocity * 0.18
            + barrel_rate * 0.22
            + hard_hit_rate * 0.18
            + launch_angle * 0.10
            + bat_speed * 0.10
            + sweet_spot * 0.07
            + fly_ball_rate * 0.08
            + pull_air_rate * 0.07
        )

        return {
            "Exit Velocity": exit_velocity,
            "Barrel %": barrel_rate,
            "Hard Hit %": hard_hit_rate,
            "Launch Angle": launch_angle,
            "Bat Speed": bat_speed,
            "Sweet Spot %": sweet_spot,
            "Fly Ball %": fly_ball_rate,
            "Pull Air %": pull_air_rate,
            "Statcast Score": round(score, 2),
            "Status": "Complete",
        }


if __name__ == "__main__":

    engine = StatcastEngine()

    print(
        engine.analyze(
            95,
            91,
            90,
            84,
            92,
            86,
            88,
            85,
        )
    )