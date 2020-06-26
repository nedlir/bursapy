from datetime import datetime
from time import sleep
import signaler
from paper import Paper


DAY_IN_SECS = 86400
TODAY = datetime.weekday(datetime.today())
FRI = 4
SAT = 5
SIGNAL_TIME = 11
TIME_NOW = datetime.now().hour

portfolio = set()

portfolio.add(Paper('777037'))
portfolio.add(Paper('1123777'))
portfolio.add(Paper('1104249'))
portfolio.add(Paper('1157833'))
portfolio.add(Paper('103010'))
portfolio.add(Paper('1161264'))

while True:
    if TODAY != FRI and TODAY != SAT:
        if TIME_NOW == SIGNAL_TIME:
            for paper in portfolio:
                signaler.send_percentage_change(paper, 0.1, 'mail')
                signaler.send_percentage_change(paper, 0.1, 'wapp')
    sleep(DAY_IN_SECS)
