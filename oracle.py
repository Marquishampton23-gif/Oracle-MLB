"""
Oracle Engine
"""

from database.master_loader import MasterLoader
from database.player_database import PlayerDatabase

from engine.dna_engine import DNAEngine
from engine.matchup_engine import MatchupEngine
from engine.opportunity_engine import OpportunityEngine
from engine.heat_check_engine import HeatCheckEngine
from engine.sleeper_engine import SleeperEngine


class Oracle:

    def __init__(self):

        # Load all datasets
        loader = MasterLoader()
        datasets = loader.load_all()

        # Build Master Player Database
        self.database = PlayerDatabase(datasets)

        # Load Engines
        self.dna = DNAEngine()
        self.matchup = MatchupEngine()
        self.opportunity = OpportunityEngine()
        self.heat = HeatCheckEngine()
        self.sleeper = SleeperEngine()

    def analyze_player(self, player):

        dna = self.dna.analyze(player)
        matchup = self.matchup.analyze(player)
        opportunity = self.opportunity.analyze(player)
        heat = self.heat.analyze(player)
        sleeper = self.sleeper.analyze(player)

        oracle_score = (
            dna["score"] +
            matchup["score"] +
            opportunity["score"] +
            heat["score"] +
            sleeper["score"]
        ) / 5

        return {
            "Player": player,
            "Oracle Score": round(oracle_score, 2),
            "Tier": "A"
        }

    def analyze_all(self):

        players = self.database.players

        results = []

        for player in players:
            results.append(self.analyze_player(player))

        return results