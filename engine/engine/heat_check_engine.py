"""
Oracle Heat Check Engine
Version 1.0
"""

class HeatCheckEngine:

    def __init__(self):
        self.name = "Oracle Heat Check Engine"

    def analyze(self, player):

        def value(column, default=50):
            try:
                return float(player.get(column, default))
            except:
                return default

        recent_home_runs = value("recent_home_runs")
        recent_barrel_rate = value("recent_barrel_rate")
        recent_hard_hit_rate = value("recent_hard_hit_rate")
        recent_exit_velocity = value("recent_exit_velocity")
        recent_launch_angle = value("recent_launch_angle")

        score = (
            recent_home_runs * 0.30 +
            recent_barrel_rate * 0.25 +
            recent_hard_hit_rate * 0.20 +
            recent_exit_velocity * 0.15 +
            recent_launch_angle * 0.10
        )

        return {
            "Heat Score": round(score, 2),
            "Recent HR": recent_home_runs,
            "Recent Barrel %": recent_barrel_rate,
            "Recent Hard Hit %": recent_hard_hit_rate,
            "Recent Exit Velocity": recent_exit_velocity,
            "Recent Launch Angle": recent_launch_angle
        }