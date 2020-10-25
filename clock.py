from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    print('This job is run every 100 minutes.')
    res = request.get('https://bk000-wedding.herokuapp.com/')
    print(res.text)

sched.start()