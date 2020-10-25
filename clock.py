from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    print('This job is run every 100 minutes.')

sched.start()