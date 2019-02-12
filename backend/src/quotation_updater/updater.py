from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from quotation_updater import quotation_api


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(quotation_api.update_quotations, 'interval', hours=1)
    scheduler.start()
