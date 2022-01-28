import time
from threading import Thread

import schedule
import notifypy

from date_time_funcs import getTimeDifference
from fightcenter_parse import *


class Manager:
    upcoming_cards = []
    recent_cards = []
    thread = None
    stop_flag = False

    def __init__(self):
        self.thread = Thread(target=self.check_schedule, daemon=True).start()

    def check_schedule(self):
        schedule.every().day.at("08:00").do(self.job)
        while not self.stop_flag:
            schedule.run_pending()
            time.sleep(60)

    def kill_thread(self):
        self.stop_flag = True

    def update_cards(self):
        ret = []
        self.recent_cards = self.upcoming_cards
        self.upcoming_cards = parse()

        for card in self.recent_cards:
            if card in self.upcoming_cards:
                ret.append(card)

        self.recent_cards = ret

    def send_notifications(self):

        for card in self.upcoming_cards:

            # If card is starting within a day, send a notification
            if getTimeDifference(card.dt_local).total_seconds() < 86400:
                notification = Notify()
                notification.title = card.headline()
                notification.message = card.dateAndTime()
                notification.icon = 'logo.png'
                notification.send()

    def job(self):
        self.update_cards()
        self.send_notifications()
