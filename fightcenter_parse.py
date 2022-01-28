import re

import pytz
import requests
from bs4 import BeautifulSoup

from card import Card
from date_time_funcs import *


def parse():
    url = 'https://www.tapology.com'
    r = requests.get("https://www.tapology.com/fightcenter?group=major&schedule=upcoming")
    soup = BeautifulSoup(r.text, 'html.parser')
    events = soup.findAll(class_='fcListing')
    all_cards = []

    for x in events:
        if len(all_cards) == 10:
            break

        promotion_time = x.find(class_='promotion').text
        promotion_time = ' '.join(promotion_time.split())

        day_idx = re.search('[^ ]*day', promotion_time).start()
        ampm_idx = re.search('[AP]M', promotion_time).end()
        date_time = promotion_time[day_idx:ampm_idx]
        date_time_details = date_time.split(',')
        date = date_time_details[1].strip()
        date_details = date.split(' ')
        month = date_details[0]
        month_num = convertMonth(month)
        day_num = date_details[1]
        day_str = date_time_details[0].strip()
        time = date_time_details[2].strip()
        promotion = promotion_time[0:day_idx].strip()
        promotion_details = promotion.split(' ')
        promotion = promotion_details[0]

        try:
            title = x.find(class_='billing').text
            link = x.find('a', href=True)
            idx = re.search('".*"', str(link))
            link = str(link)[idx.start() + 1:idx.end() - 1]
            link = url + link

        except:  # reached when cards don't have official name yet.
            continue

        dt_now = datetime.datetime.now()
        curr_year = dt_now.year
        curr_month = dt_now.month

        if month_num < curr_month:
            year = curr_year + 1
        else:
            year = curr_year

        time = convert24Hour(time)
        time = removeAMPM(time)

        time_details = time.split(':')
        hour = time_details[0]
        min = time_details[1]

        dt = datetime.datetime(year, month_num, int(day_num), int(hour), int(min), 0, 0)
        utc_tz = pytz.utc
        est_tz = pytz.timezone('US/Eastern')

        dt = est_tz.localize(dt)
        dt = dt.astimezone(utc_tz)
        new_card = Card(title, promotion, date, str(month_num), day_str, day_num,
                        time, dt, convertUTCtoLocal(dt), hour, min, link)
        all_cards.append(new_card)

    return all_cards
