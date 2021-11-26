from datetime import date
import calendar


def print_current_date():
    """
    Print the current date with this format: {day}/{month}/{year} and the weekday.
    :return: none
    """
    dt = date.today()
    print("{}/{}/{}".format(dt.day, dt.month, dt.year) + " and the current day is " + dt.strftime("%A"))


def print_calendar(year: int = date.today().year, month: int = date.today().month):
    """
    Print a calendar of the especified month and year or the current ones if you do not write any number.
    :param year: current year or especified year
    :param month: current month or especified month
    :return: none
    """
    c = calendar.TextCalendar(calendar.MONDAY)
    print(c.formatmonth(year, month))
