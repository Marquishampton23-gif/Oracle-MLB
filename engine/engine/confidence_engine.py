"""
Oracle Confidence Engine
Version 1.0
"""


class ConfidenceEngine:

    def __init__(self):
        self.name = "Oracle Confidence Engine"

    def analyze(
        self,
        dna_score,
        matchup_score,
        opportunity_score,
    ):

        confidence = (
            dna_score * 0.40
            + matchup_score * 0.35
            + opportunity_score * 0.25
        )

        return {
            "Confidence Score": round(confidence, 2),
            "Tier": self.get_tier(confidence),
            "Status": "Complete",
        }

    def get_tier(self, score):

        if score >= 90:
            return "Tier S"

        if score >= 85:
            return "Tier A"

        if score >= 80:
            return "Tier B"

        return "Sleeper"


if __name__ == "__main__":

    engine = ConfidenceEngine()

    print(
        engine.analyze(
            92,
            89,
            87,
        )
    )