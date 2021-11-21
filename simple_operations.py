from datetime import date
import calendar


def fecha():
    dt = date.today()
    print("{}/{}/{}".format(dt.day, dt.month, dt.year) + " and the current day is " + dt.strftime("%A"))


def month_calendar():
    dt = date.today()
    calendario = calendar.TextCalendar(calendar.MONDAY)
    print(calendario.formatmonth(dt.year, dt.month))
