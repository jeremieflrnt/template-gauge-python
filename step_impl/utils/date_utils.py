import locale

from datetime import datetime
from datetime import timedelta


class DateUtils(object):
    TODAY = datetime.today()


def print_date(date):
    return date.strftime("%d/%m/%Y")


def print_month_full_name(date):
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    return date.strftime("%B")


def get_today():
    return print_date(DateUtils.TODAY)


def get_today_add_days(days):
    days_delta = timedelta(days=days)
    return print_date(DateUtils.TODAY + days_delta)


def get_date_add_days_from_date_dd_mm_yyyy(date_dd_mm_yyyy, days):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    days_delta = timedelta(days=days)
    return print_date(given_date + days_delta)


def get_date_add_days_from_date_yyyy_mm_dd(date_yyyy_mm_dd, days):
    given_date = convert_yyyy_mm_dd_to_dd_mm_yyyy(date_yyyy_mm_dd)
    days_delta = timedelta(days=days)
    return print_date(given_date + days_delta)


def get_today_add_months(months):
    days_delta = timedelta(months=months)
    return print_date(DateUtils.TODAY + days_delta)


def get_date_add_months_from_date_dd_mm_yyyy(date_dd_mm_yyyy, months):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    months_delta = timedelta(months=months)
    return print_date(given_date + months_delta)


def get_date_add_months_from_date_yyyy_mm_dd(date_yyyy_mm_dd, months):
    given_date = convert_yyyy_mm_dd_to_dd_mm_yyyy(date_yyyy_mm_dd)
    months_delta = timedelta(months=months)
    return print_date(given_date + months_delta)


def get_today_add_years(years):
    days_delta = timedelta(years=years)
    return print_date(DateUtils.TODAY + days_delta)


def get_date_add_years_from_date_dd_mm_yyyy(date_dd_mm_yyyy, years):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    years_delta = timedelta(years=years)
    return print_date(given_date + years_delta)


def get_date_add_years_from_date_yyyy_mm_dd(date_yyyy_mm_dd, years):
    given_date = convert_yyyy_mm_dd_to_dd_mm_yyyy(date_yyyy_mm_dd)
    years_delta = timedelta(years=years)
    return print_date(given_date + years_delta)


def get_today_add_day_no_we(days_sup_0):
    current_date = datetime.today()
    days_to_add = days_sup_0
    while days_to_add >= 0:
        current_date += timedelta(days=1)
        if current_date.isoweekday() >= 6:  # saturday = 6, sunday = 7
            continue
        days_to_add -= 1
    return print_date(current_date)


def get_day(date_dd_mm_yyyy):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    return given_date.day


def get_month(date_dd_mm_yyyy):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    return given_date.month


def get_month_full_name(date_dd_mm_yyyy):
    given_date = datetime.strptime(date_dd_mm_yyyy, "%d/%m/%Y")
    return print_month_full_name(given_date)


def convert_yyyy_mm_dd_to_dd_mm_yyyy(date_yyyy_mm_dd):
    given_date = datetime.strptime(date_yyyy_mm_dd, "%Y/%m/%d")
    return print_date(given_date)


def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
