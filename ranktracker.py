import pandas as pd
import os
from datetime import date, timedelta

RANK_DATA_PATH = "./rank_data"


class RankTracker:
    def track(self, domain):
        # 어제의 랭크 데이터와 오늘의 랭크 데이터를 읽어서 DF형태로 저장한다.
        today_df = pd.read_csv(f"data/{date.today()}-{domain}.csv", encoding="utf-8")
        yesterday_df = pd.read_csv(
            f"data/{date.today()-timedelta(days=1)}-{domain}.csv", encoding="utf-8"
        )

        # 두 데이터 프레임을 머지
        merged_df = pd.merge(
            today_df,
            yesterday_df,
            on=["title", "artist", "album", "img_url"],
            how="outer",
            suffixes=("_today", "_yesterday"),
        )

        # 결측값 채우기, 타입변환
        merged_df = merged_df.fillna(101)
        merged_df["rank_today"] = merged_df["rank_today"].astype(int)
        merged_df["rank_yesterday"] = merged_df["rank_yesterday"].astype(int)

        # 어제 랭크와 오늘 랭크의 차를 계산해서 새로운 컬럼 생성(rank_change)
        merged_df["rank_change"] = merged_df["rank_yesterday"] - merged_df["rank_today"]
        merged_df = (
            merged_df.rename(columns={"rank_today": "rank"})
            .drop(columns="rank_yesterday")
            .set_index("rank")
        )

        # 컬럼의 순서를 바꾸기 위해 다시 대입해주었음 그리고 index(rank)를 기준으로 정렬
        merged_df = merged_df[
            ["rank_change", "title", "artist", "album", "img_url"]
        ].sort_index()

        # 100순위 밑으로 밀려난 데이터 제거
        merged_df = merged_df[merged_df.index <= 100]

        # rank_data 디렉토리가 없으면 rank_data 디렉토리 생성
        if not os.path.exists(RANK_DATA_PATH):
            os.makedirs(RANK_DATA_PATH)

        # 랭크 변화 데이터가 추가된 csv 파일을 export
        merged_df.to_csv(
            f"{RANK_DATA_PATH}/{date.today()}-{domain}.csv",
            index=True,
            encoding="utf-8",
        )
