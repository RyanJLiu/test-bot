from apscheduler.schedulers.blocking import BlockingScheduler
import scheduling

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def scheduled_job():
    scheduling.mind()

sched.start()
