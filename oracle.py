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
        self.database = PlayerDatabase(datasets).build()

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
            dna["DNA Score"] * 0.30 +
            matchup["Matchup Score"] * 0.25 +
            opportunity["Opportunity Score"] * 0.15 +
            heat["Heat Score"] * 0.15 +
            sleeper["Sleeper Score"] * 0.15
        )

        return {
            "Player": player.get("player_name", "Unknown"),
            "Oracle Score": round(oracle_score, 2),
            "DNA": dna,
            "Matchup": matchup,
            "Opportunity": opportunity,
            "Heat": heat,
            "Sleeper": sleeper,
        }

    def analyze_all(self):

        results = []

        for _, player in self.database.iterrows():
            results.append(self.analyze_player(player.to_dict()))

        results.sort(
            key=lambda x: x["Oracle Score"],
            reverse=True
        )

        return results