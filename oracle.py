"""
Oracle Engine
Version 0.2
"""

from database.master_loader import MasterLoader

from engine.dna_engine import DNAEngine
from engine.matchup_engine import MatchupEngine
from engine.opportunity_engine import OpportunityEngine
from engine.heat_check_engine import HeatCheckEngine
from engine.sleeper_engine import SleeperEngine


class Oracle:

    def __init__(self):

        # Load Master Database
        self.loader = MasterLoader()
        self.database = self.loader.load_all()

        # Load Oracle Engines
        self.dna = DNAEngine()
        self.matchup = MatchupEngine()
        self.opportunity = OpportunityEngine()
        self.heat = HeatCheckEngine()
        self.sleeper = SleeperEngine()

    def analyze(self, player):

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
            "Sleeper": sleeper
        }


if __name__ == "__main__":

    oracle = Oracle()

    if len(oracle.database) > 0:
        result = oracle.analyze(oracle.database.iloc[0].to_dict())
        print(result)