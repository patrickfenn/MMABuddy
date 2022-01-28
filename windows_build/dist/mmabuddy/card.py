from date_time_funcs import *


class Card:
    title = promotion = date = month = day_str = day_num = time = hour = \
        min = dt_utc = dt_local = link = None

    def __init__(self, t, p, d, m, ds, dn, ti, dt, dt_l, h, mi, l):
        self.title = t
        self.promotion = p
        self.date = d
        self.month = m
        self.day_str = ds
        self.day_num = dn
        self.dt_utc = dt
        self.dt_local = dt_l
        self.time = ti
        self.hour = h
        self.min = mi
        self.link = l

    def __str__(self):
        return self.headline() + '\n' + self.dateAndTime() + '\n' + self.countDown()

    def __eq__(self, other):
        if self.title == other.title:
            return True
        else:
            return False

    def countDown(self):
        dif = getTimeDifference(self.dt_local)
        time_unit = timeUnit(dif.total_seconds())
        return time_unit.__str__()

    def headline(self):
        return self.promotion + ' - ' + self.title

    def dateAndTime(self):
        return self.day_str + ', ' + self.date + ' @ ' + \
               self.dt_local.time().strftime('%I:%M %p') + ' ' + self.dt_local.utcnow().astimezone().tzinfo.__str__()
