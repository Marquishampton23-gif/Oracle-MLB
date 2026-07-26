"""
Oracle Engine
Version 0.1 Alpha
"""

from engine.dna_engine import DNAEngine
from engine.matchup_engine import MatchupEngine
from engine.opportunity_engine import OpportunityEngine
from engine.confidence_engine import ConfidenceEngine
from engine.statcast_engine import StatcastEngine


class Oracle:

    def __init__(self):
        self.statcast = StatcastEngine()
        self.dna = DNAEngine()
        self.matchup = MatchupEngine()
        self.opportunity = OpportunityEngine()
        self.confidence = ConfidenceEngine()

    def analyze(self, hitter, pitcher):

        return {
            "hitter": hitter,
            "pitcher": pitcher,
            "status": "Oracle Connected"
        }


if __name__ == "__main__":
    oracle = Oracle()

    print(
        oracle.analyze(
            "Aaron Judge",
            "Tarik Skubal"
        )
    )