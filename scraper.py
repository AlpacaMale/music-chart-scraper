import requests
import csv
import os
from bs4 import BeautifulSoup
from datetime import date

MELON = "melon"
BUGS = "bugs"
GENIE = "genie"
DATA_PATH = "./data"


class Scraper:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        self.music_ranks = []

    def melon_scrape(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        musics = soup.select("tbody > tr")
        for music in musics:
            rank = music.select_one(".rank").text
            title = music.select_one(".rank01 > span > a").text
            artist = music.select_one(".rank02 > a").text
            album = music.select_one(".rank03 > a").text
            img_url = music.select_one("img")["src"]
            music_data = self.to_dict(rank, title, artist, album, img_url)
            self.music_ranks.append(music_data)
        self.to_csv(MELON)

    def bugs_scrape(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        musics = soup.select(".trackList > tbody > tr")
        for music in musics:
            rank = music.select_one(".ranking > strong").text
            title = music.select_one(".title").text.strip()
            artist = music.select_one("td > .artist > a").text
            album = music.select_one("td > .album").text
            img_url = music.select_one("img")["src"]
            music_data = self.to_dict(rank, title, artist, album, img_url)
            self.music_ranks.append(music_data)
        self.to_csv(BUGS)

    def genie_scrape(self, url):
        for page in (1, 2):
            response = requests.get(f"{url}{page}", headers=self.headers)
            soup = BeautifulSoup(response.content, "html.parser")
            musics = soup.select("tbody > .list")
            for music in musics:
                rank = music.select_one(".number").text.split()[0]
                title = music.select_one(".info > .title").text.strip()
                artist = music.select_one(".info > .artist").text
                album = music.select_one(".info > .albumtitle").text
                img_url = music.select_one("img")["src"]
                music_data = self.to_dict(rank, title, artist, album, img_url)
                self.music_ranks.append(music_data)
        self.to_csv(GENIE)

    def to_dict(self, rank, title, artist, album, img_url):
        return {
            "rank": rank,
            "title": title,
            "artist": artist,
            "album": album,
            "img_url": img_url,
        }

    def to_csv(self, file_name):
        # rank_data 디렉토리가 없으면 rank_data 디렉토리 생성
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        with open(
            f"{DATA_PATH}/{date.today()}-{file_name}.csv", "a", encoding="utf-8"
        ) as file:
            fieldnames = ["rank", "title", "artist", "album", "img_url"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # 헤더 작성
            writer.writerows(self.music_ranks)  # 데이터 작성
            self.music_ranks = []

        # file.write("rank,title,artist,album,img_url\n")
        # for music_rank in music_ranks:
        #     line = [str(string) for string in music_rank.values()]
        #     file.write(",".join(line) + "\n")
