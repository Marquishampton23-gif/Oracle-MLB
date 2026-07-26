"""
Oracle Base Set
Version 1.0
"""


class BaseSet:

    # DNA Engine
    DNA_WEIGHTS = {
        "exit_velocity": 0.20,
        "barrel_rate": 0.25,
        "hard_hit_rate": 0.20,
        "launch_angle": 0.10,
        "bat_speed": 0.10,
        "sweet_spot": 0.05,
        "fly_ball_rate": 0.10,
    }

    # Matchup Engine
    MATCHUP_WEIGHTS = {
        "pitch_match": 0.30,
        "zone_match": 0.25,
        "platoon": 0.20,
        "arsenal": 0.15,
        "movement": 0.10,
    }

    # Opportunity Engine
    OPPORTUNITY_WEIGHTS = {
        "lineup": 0.25,
        "park": 0.25,
        "weather": 0.20,
        "bullpen": 0.15,
        "game_script": 0.15,
    }

    # Final Oracle score
    CONFIDENCE_WEIGHTS = {
        "dna": 0.40,
        "matchup": 0.35,
        "opportunity": 0.25,
    }

    TIERS = {
        "Tier S": 90,
        "Tier A": 85,
        "Tier B": 80,
        "Sleeper": 0,
    }