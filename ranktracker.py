import pandas as pd
from datetime import date, timedelta


class RankTracker:
    def track(self, domain):
        today_df = pd.read_csv(f"data/{date.today()}-{domain}.csv", encoding="utf-8")
        yesterday_df = pd.read_csv(
            f"data/{date.today()-timedelta(days=1)}-{domain}.csv", encoding="utf-8"
        )

        merged_df = pd.merge(
            today_df,
            yesterday_df,
            on=["title", "artist", "album", "img_url"],
            how="outer",
            suffixes=("_today", "_yesterday"),
        )
        merged_df = merged_df.fillna(101)
        merged_df["rank_today"] = merged_df["rank_today"].astype(int)
        merged_df["rank_yesterday"] = merged_df["rank_yesterday"].astype(int)
        merged_df["rank_change"] = merged_df["rank_yesterday"] - merged_df["rank_today"]
        merged_df = (
            merged_df.rename(columns={"rank_today": "rank"})
            .drop(columns="rank_yesterday")
            .set_index("rank")
        )
        merged_df = merged_df[
            ["rank_change", "title", "artist", "album", "img_url"]
        ].sort_index()
        merged_df = merged_df[merged_df.index <= 100]
        merged_df.to_csv(
            f"rank_data/{date.today()}-{domain}", index=True, encoding="utf-8"
        )
