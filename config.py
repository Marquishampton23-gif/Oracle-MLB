"""
Oracle MLB Intelligence Engine
Configuration File
"""

from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).parent

# Database
DATABASE_PATH = ROOT_DIR / "database" / "oracle.db"

# Data folders
DATA_FOLDER = ROOT_DIR / "data"
REPORT_FOLDER = ROOT_DIR / "reports"

# Oracle Version
APP_NAME = "Oracle MLB Intelligence Engine"
VERSION = "0.1.0 Alpha"

# Default scoring weights (these will become configurable)
WEIGHTS = {
    "pitch_arsenal": 0.12,
    "exit_velocity": 0.12,
    "swing_path": 0.10,
    "swing_timing": 0.10,
    "bat_speed": 0.10,
    "launch_angle": 0.08,
    "pitch_movement": 0.08,
    "zone_match": 0.12,
    "weather": 0.08,
    "park_factor": 0.05,
    "recent_form": 0.05,
}
