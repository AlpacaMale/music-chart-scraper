# Rank Tracker

## 개요

멜론, 벅스, 지니의 음원 차트 100위 이내의 랭킹을 수집하고, 하루 전의 랭킹과 비교한다.

## 목차

- [To-Do List](#to-do-list)
- [패키지 구조](#패키지-구조)
- [사용 모듈](#사용-모듈)
- [실행 방법](#실행-방법)

## To-Do List

- [x] **melon scraper**: 웹 스크래핑 로직 구현
- [x] **bugs scraper**: 웹 스크래핑 로직 구현
- [x] **genie scraper**: 웹 스크래핑 로직 구현
- [x] **refactor scraper code**: 스크래핑 코드 함수화, 클래스화, 모듈화
- [x] **export rank data**: 스크래핑한 데이터를 csv 파일로 export 하는 로직 구현
- [x] **rank tracker**: 어제의 랭크와 비교해서 오르고 내린 만큼을 표현하는 로직 구현
- [x] **export rank track data**: 랭크를 추적한 데이터를 csv 파일로 export 하는 로직 구현

## 패키지 구조

```
├── 📁 data / export path for data
├── 📁 rank_data / export path for rank-tracking data
├── main.py / main entry of python program
├── scraper.py / web scraper logic
├── ranktracker.py / rank track logic
├── requirements.txt / package dependency
├── README.md
```

## 사용 모듈

- **Beautifulsoup**: HTML 구문을 파싱하여 Python 자료구조로 변환해준다.
- **Requests**: HTTP 요청을 간편하게 보내고 응답을 처리해준다.
- **Datetime**: 날짜와 시간 관련 기능을 제공하며, 날짜 형식 변환, 차이 계산 등 다양한 작업을 처리한다.
- **Pandas**: 데이터를 읽고, 쓰고, 가공하는 다양한 기능을 처리한다.

## 실행 방법

1. **Clone repository**

```
git clone https://github.com/AlpacaMale/music-chart-scraper
```

2. **Install dependency**

```
pip install -r requirements.txt
```

3. **Run main.py**

```
python main.py
```
