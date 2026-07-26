import os
import glob
import pandas as pd


class MasterLoader:
    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        self.player_data = None

    def load_all(self):
        csv_files = glob.glob(os.path.join(self.data_folder, "*.csv"))

        merged = None

        for file in csv_files:
            try:
                df = pd.read_csv(file)

                # Find MLBAM Player ID automatically
                player_id = None
                for col in df.columns:
                    if "player_id" in col.lower() or "mlbam" in col.lower():
                        player_id = col
                        break

                if player_id is None:
                    continue

                if merged is None:
                    merged = df
                else:
                    merged = merged.merge(
                        df,
                        on=player_id,
                        how="outer",
                        suffixes=("", "_dup")
                    )

            except Exception as e:
                print(f"Skipped {file}: {e}")

        self.player_data = merged
        return merged

    def get_player(self, player_id):
        if self.player_data is None:
            self.load_all()

        return self.player_data[
            self.player_data.iloc[:, 0] == player_id
        ]