import json
from datetime import datetime
from urllib.request import urlopen


FETCH_URL = "https://www.bizportal.co.il/forex/quote/ajaxrequests/paperdatagraphjson?"
DICT_PAPER_NAME = 'paperName'
DICT_POINTS = 'points'
DICT_DATE = 'D_p'
TODAY = datetime.weekday(datetime.today())
FRI = 4
SAT = 5


def fetch_paper_data(paper_id=''):
    period = 'yearly'  # Period must be set to: 5Years, yearly or daily
    url = FETCH_URL + f"period={period}&paperID={paper_id}"

    with urlopen(url) as response:
        source = response.read()
        temp_dict = json.loads(source)

    if TODAY != FRI and TODAY != SAT:
        date_today = datetime.today().strftime('%d/%m/%Y')
        today = fetch_daily_data(date_today, paper_id)
        temp_dict.get(DICT_POINTS).insert(0, today)

    return temp_dict.get(DICT_POINTS), temp_dict.get(DICT_PAPER_NAME)


def fetch_daily_data(date_today='00/00/0000', paper_id=''):
    period = 'daily'
    url = FETCH_URL + f"period={period}&paperID={paper_id}"

    with urlopen(url) as response:
        source = response.read()
        temp_dict = json.loads(source)

        # Initializes today's points with latest trading value
        today = temp_dict.get(DICT_POINTS)[-1]
        today.update({DICT_DATE: date_today})

    return today