from apscheduler.schedulers.blocking import BlockingScheduler
import scheduling

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=30)
def scheduled_job():
    url = "https://test-bot-first.herokuapp.com/"
    conn = urllib.request.urlopen(url)

@sched.scheduled_job('interval', minutes=5)
def scheduled_job():
    scheduling.med_mind()

sched.start()
