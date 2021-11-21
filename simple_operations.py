from datetime import date
import calendar


def current_date():
    dt = date.today()
    print("{}/{}/{}".format(dt.day, dt.month, dt.year) + " and the current day is " + dt.strftime("%A"))


def month_calendar():
    dt = date.today()
    c = calendar.TextCalendar(calendar.MONDAY)
    print(c.formatyear(dt.year, 2, 1, 6, 4))
