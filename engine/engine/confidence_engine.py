class ConfidenceEngine:

    def calculate(
        self,
        dna,
        matchup,
        opportunity,
        heat,
        sleeper
    ):

        score = (
            dna * 0.35 +
            matchup * 0.25 +
            opportunity * 0.15 +
            heat * 0.15 +
            sleeper * 0.10
        )

        return round(score, 2)