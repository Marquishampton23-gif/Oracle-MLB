class DNAEngine:

    def analyze(self, player):

        def value(*columns, default=0):
            for column in columns:
                if column in player:
                    try:
                        return float(player[column])
                    except:
                        pass
            return default

        exit_velocity = value(
            "avg_hit_speed",
            "avg_hit_speed_mph",
            "exit_velocity_avg"
        )

        barrel_rate = value(
            "brl_percent",
            "barrel_batted_rate"
        )

        hard_hit = value(
            "hard_hit_percent",
            "hardhit_percent"
        )

        launch_angle = value(
            "launch_angle_avg"
        )

        bat_speed = value(
            "avg_bat_speed"
        )

        sweet_spot = value(
            "sweet_spot_percent"
        )

        dna_score = (
            exit_velocity * .25 +
            barrel_rate * .20 +
            hard_hit * .20 +
            launch_angle * .15 +
            bat_speed * .10 +
            sweet_spot * .10
        )

        return {
            "DNA Score": round(dna_score,2),
            "Exit Velocity": exit_velocity,
            "Barrel %": barrel_rate,
            "Hard Hit %": hard_hit,
            "Launch Angle": launch_angle,
            "Bat Speed": bat_speed,
            "Sweet Spot %": sweet_spot
        }