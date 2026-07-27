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
        
        print(self.merged_data.columns.tolist())
print(self.merged_data[["player_id", "player_name"]].head(10))
raise SystemExit

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


if __name__ == "__main__":
    print("=" * 70)
    print("ORACLE MLB HOME RUN ENGINE")
    print("=" * 70)

    try:
        oracle = Oracle()

        print(f"\nLoaded {len(oracle.merged_data)} players.")

        results = oracle.analyze_all()

        if not results:
            print("No players were analyzed.")
            raise SystemExit

        results = sorted(
            results,
            key=lambda player: player.get("Oracle Score", 0),
            reverse=True
        )

        print("\nTOP 25 HOME RUN BOARD")
        print("-" * 70)
        
for rank, player in enumerate(results[:25], start=1):

    name = (
        player.get("player_name")
        or player.get("Player Name")
        or player.get("full_name")
        or player.get("Name")
        or player.get("name")
        or player.get("Player")
        or "Unknown"
    )

    team = (
        player.get("team")
        or player.get("Team")
        or ""
    )

    score = player.get("Oracle Score", 0)
    tier = player.get("Tier", "-")

    if team:
        print(
            f"{rank:2}. {name} ({team})    "
            f"Score: {score}    "
            f"Tier: {tier}"
        )
    else:
        print(
            f"{rank:2}. {name}    "
            f"Score: {score}    "
            f"Tier: {tier}"
        )

print("\nDone.")