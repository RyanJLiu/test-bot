from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=2)
def scheduled_job():
    print('Time to sleep.')

sched.start()