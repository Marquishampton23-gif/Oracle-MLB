"""
Oracle Engine
"""

from database.master_loader import MasterLoader
from database.player_database import PlayerDatabase

from engine.engine.dna_engine import DNAEngine
from engine.engine.matchup_engine import MatchupEngine
from engine.engine.opportunity_engine import OpportunityEngine
from engine.engine.heat_check_engine import HeatCheckEngine


class Oracle:

    def __init__(self):

        # Load all datasets
        loader = MasterLoader()
        datasets = loader.load_all()

        # Build Master Player Database
        self.database = PlayerDatabase(datasets)
        self.merged_data = self.database.build()

        # Load Engines
        self.dna = DNAEngine()
        self.matchup = MatchupEngine()
        self.opportunity = OpportunityEngine()
        self.heat = HeatCheckEngine()

    def analyze_player(self, player):

        dna = self.dna.analyze(player)
        matchup = self.matchup.analyze(player)
        opportunity = self.opportunity.analyze(player)
        heat = self.heat.analyze(player)

        oracle_score = (
            dna["DNA Score"] +
            matchup["Matchup Score"] +
            opportunity["Opportunity Score"] +
            heat["Heat Score"]
        ) / 4

        return {
            "Player": player.get("player_name") or player.get("player_id", "Unknown"),
            "Oracle Score": round(oracle_score, 2),
            "Tier": "A"
        }

    def analyze_all(self):

        if self.merged_data is None or len(self.merged_data) == 0:
            return []

        results = []

        for idx, row in self.merged_data.iterrows():
            player_dict = row.to_dict()
            results.append(self.analyze_player(player_dict))

        return results
