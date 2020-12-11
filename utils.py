from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup

LEADERBOARD_URL = 'https://adventofcode.com/2020/leaderboard/private/view/144312.json'


def convert_unix_to_datetime(unix_time: int) -> str:
    now_dt = datetime.utcfromtimestamp(unix_time)
    pretty_date = now_dt.strftime("%c")
    return pretty_date


def get_leaderboard_data(url: str) -> dict:
    leaderboard = requests.get(url)
    soup = BeautifulSoup(leaderboard.text, 'html.parser')
    print(soup.prettify())


def parse_leaderboard(data):
    data = json.loads(data)
    parsed_data = {}
    for a in data['members']:
        results = data['members'][a]
        parsed_data[results['name']] = []
        completion_stats = results['completion_day_level']
        for day, timestamps in completion_stats.items():
            element = {}
            times = []
            for id, time in timestamps.items():
                times.append(convert_unix_to_datetime(int(time['get_star_ts'])))
            element[day] = times
            parsed_data[results['name']].append(element)
    print(parsed_data)


if __name__ == "__main__":
    pass
    # formatted_leaderboard = parse_leaderboard(data)
    # formatted_json = json.dumps(formatted_leaderboard)
    # with open('formatted_leadboard.json', 'w') as output:
    #     output.write(formatted_json)
