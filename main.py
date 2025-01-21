from scraper import Scraper, MELON, BUGS, GENIE
from ranktracker import RankTracker


MELON_URL = "https://www.melon.com/chart/index.htm"
BUGS_URL = "https://music.bugs.co.kr/chart"
GENIE_URL = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250122&hh=04&rtm=Y&pg="

scraper = Scraper()
scraper.melon_scrape(MELON_URL)
scraper.bugs_scrape(BUGS_URL)
scraper.genie_scrape(GENIE_URL)


ranktracker = RankTracker()
ranktracker.track(MELON)
ranktracker.track(BUGS)
ranktracker.track(GENIE)
