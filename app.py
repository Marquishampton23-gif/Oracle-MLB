from oracle import Oracle
from scoring_engine import ScoringEngine


def main():

    oracle = Oracle()

    print("\nRunning Oracle...\n")

    results = oracle.analyze_all()

    rankings = ScoringEngine().rank_players(results)

    print("===== ORACLE HOME RUN BOARD =====\n")

    for i, player in enumerate(rankings[:25], start=1):

        print(
            f"{i}. {player['Player']} | "
            f"{player['Oracle Score']} | "
            f"{player['Tier']}"
        )


if __name__ == "__main__":
    main()