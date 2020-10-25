from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    print('This job is run every 100 minutes.')
    res = requests.get('https://bk000-wedding.herokuapp.com/')
    print(res.text)

sched.start()