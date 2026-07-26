import pandas as pd


class PlayerDatabase:

    def __init__(self, datasets):
        self.datasets = datasets

    def build(self):

        merged = None

        for name, df in self.datasets.items():

            # Use player_id if available
            if "player_id" in df.columns:

                if merged is None:
                    merged = df

                else:
                    merged = merged.merge(
                        df,
                        on="player_id",
                        how="outer",
                        suffixes=("", "_dup")
                    )

            # Fall back to player_name
            elif "player_name" in df.columns:

                if merged is None:
                    merged = df

                else:
                    merged = merged.merge(
                        df,
                        on="player_name",
                        how="outer",
                        suffixes=("", "_dup")
                    )

        return merged