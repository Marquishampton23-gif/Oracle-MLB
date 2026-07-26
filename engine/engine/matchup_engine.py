class MatchupEngine:

    def analyze(self, player):

        score = 0

        if player.get("Fastball_Run_Value", 0) > 0:
            score += 20

        if player.get("Slider_Run_Value", 0) > 0:
            score += 15

        if player.get("Curveball_Run_Value", 0) > 0:
            score += 10

        if player.get("Changeup_Run_Value", 0) > 0:
            score += 15

        if player.get("Sinker_Run_Value", 0) > 0:
            score += 10

        if player.get("Cutter_Run_Value", 0) > 0:
            score += 10

        if player.get("Splitter_Run_Value", 0) > 0:
            score += 10

        return {"Matchup Score": min(score, 100)}
