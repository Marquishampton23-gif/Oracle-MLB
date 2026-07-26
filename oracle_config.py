"""
Oracle Configuration
"""

from pathlib import Path


ROOT = Path(__file__).parent

DATASETS = ROOT / "datasets"

DATABASE = ROOT / "database"

REPORTS = ROOT / "reports"

MODELS = ROOT / "models"


CSV_FILES = {
    "statcast": "statcast_hitters.csv",
    "hr_matchups": "hr_matchups.csv",
    "pitch_mix": "team_vs_pitch_mix.csv",
    "pitcher_weak_spots": "pitcher_weak_spots.csv",
    "pitch_arsenal": "pitcher_arsenal.csv",
}