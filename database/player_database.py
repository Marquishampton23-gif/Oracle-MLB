import pandas as pd


class PlayerDatabase:

    def __init__(self, datasets):
        self.datasets = datasets

    def build(self):

        merged = None

        for name, df in self.datasets.items():

            if df.empty:
                continue

            # Remove duplicate columns inside each dataframe
            df = df.loc[:, ~df.columns.duplicated()]

            if "player_id" in df.columns:

                if merged is None:
                    merged = df

                else:

                    # Remove *_dup columns before merging again
                    merged = merged.loc[
                        :,
                        ~merged.columns.str.endswith("_dup")
                    ]

                    merged = merged.merge(
                        df,
                        on="player_id",
                        how="outer",
                        suffixes=("", "_dup")
                    )

            elif "player_name" in df.columns:

                if merged is None:
                    merged = df

                else:

                    merged = merged.loc[
                        :,
                        ~merged.columns.str.endswith("_dup")
                    ]

                    merged = merged.merge(
                        df,
                        on="player_name",
                        how="outer",
                        suffixes=("", "_dup")
                    )

        if merged is not None:
            merged = merged.loc[
                :,
                ~merged.columns.str.endswith("_dup")
            ]

        return merged