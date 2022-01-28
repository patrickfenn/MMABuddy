import datetime
from time import strptime

from dateutil import tz


class timeUnit:
    days = hours = minutes = seconds = total_seconds = None

    def __init__(self, total_sec):
        self.total_seconds = total_sec
        self.days = divmod(total_sec, 86400)  # Get days (without [0]!)
        self.hours = divmod(self.days[1], 3600)  # Use remainder of days to calc hours
        self.minutes = divmod(self.hours[1], 60)  # Use remainder of hours to calc minutes
        self.seconds = divmod(self.minutes[1], 1)  # Use remainder of minutes to calc seconds

    def __str__(self):
        return "%d days, %d hours, and %d minutes" % (
            self.days[0], self.hours[0], self.minutes[0])


def convertMonth(month_str):
    return strptime(month_str[0:3], '%b').tm_mon


def convert24Hour(time12):
    time_details = time12.split(':')
    hour_num = int(time_details[0])
    if 'PM' in time12:
        if hour_num == 12:
            time_details[0] = '00'
        elif hour_num + 12 > 24:
            hour_num = hour_num + 12 - 24
            time_details[0] = str(hour_num)
        else:
            hour_num += 12
            time_details[0] = str(hour_num)

    return time_details[0] + ':' + time_details[1]


def convert12Hour(time24):
    time_details = time24.split(':')
    hour_num = int(time_details[0])

    if hour_num > 12:
        hour_num -= 12
        return '0' + str(hour_num) + ':' + time_details[1] + ' PM'
    else:
        return time_details[0] + ':' + time_details[1] + ' AM'


def removeAMPM(time_am_pm):
    time_details = time_am_pm.split(' ')
    return time_details[0]


def convertUTC(time_in_est):
    time_details = time_in_est.split(':')
    hour_num = int(time_details[0])

    if 'AM' in time_in_est:
        new_hour = hour_num + 5
        if hour_num + 5 > 12:
            time_details[1].replace('AM', 'PM')
            time_details[0] = str(new_hour - 12)
        elif hour_num + 5 == 12:
            time_details[1].replace('AM', 'PM')
            time_details[0] = str(new_hour)
        else:
            time_details[0] = str(new_hour)

    elif 'PM' in time_in_est:
        new_hour = hour_num + 5
        if hour_num + 5 > 12:
            time_details[1].replace('PM', 'AM')
            time_details[0] = str(new_hour - 12)
        elif hour_num + 5 == 12:
            time_details[1].replace('PM', 'AM')
            time_details[0] = str(new_hour)
        else:
            time_details[0] = str(new_hour)

    return time_details[0] + ':' + time_details[1]


def convertUTCtoLocal(dt_utc):
    local_tz = tz.tzlocal()
    local_time = dt_utc.astimezone(local_tz)
    return local_time


def getTimeDifference(dt):
    local = datetime.datetime.now()
    local = local.replace(tzinfo=tz.tzlocal())
    dif = dt - local
    return dif
