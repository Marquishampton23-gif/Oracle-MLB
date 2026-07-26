"""
Oracle DNA Engine
Version 1.0
"""


class DNAEngine:

    def __init__(self):
        self.name = "Oracle DNA Engine"

    def analyze(
        self,
        exit_velocity,
        barrel_rate,
        hard_hit_rate,
        launch_angle,
        bat_speed,
        sweet_spot,
        fly_ball_rate,
    ):

        score = (
            exit_velocity * 0.20
            + barrel_rate * 0.25
            + hard_hit_rate * 0.20
            + launch_angle * 0.10
            + bat_speed * 0.10
            + sweet_spot * 0.05
            + fly_ball_rate * 0.10
        )

        return {
            "DNA Score": round(score, 2),
            "Status": "Complete"
        }


if __name__ == "__main__":

    dna = DNAEngine()

    print(
        dna.analyze(
            95,
            90,
            88,
            82,
            91,
            84,
            87,
        )
    )