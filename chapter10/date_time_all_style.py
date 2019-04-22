import calendar
import datetime
import time

year = time.strftime("%Y", time.localtime())
month = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
hour = time.strftime("%H", time.localtime())
minute = time.strftime("%M", time.localtime())
second = time.strftime("%S", time.localtime())


def today():
    """
    get today,date format="YYYY-MM-DD"
    :return:
    """
    return datetime.date.today()


def today_str():
    """
    get date string, date format="YYYYMMDD"
    :return:
    """
    return year + month + day


def date_time():
    """
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def date_time_str():
    """
    get datetime string
    date format="YYYYMMDDHHMMSS"
    :return:
    """
    return year + month + day + hour + minute + second


def get_day_of_day(n=0):
    """
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    :param n:
    :return:
    """
    if n < 0:
        n = abs(n)
        return datetime.date.today() - datetime.timedelta(days=n)
    else:
        return datetime.date.today() + datetime.timedelta(days=n)


def get_days_of_month(year_v, mon_v):
    """
    get days of month
    :param year_v:
    :param mon_v:
    :return:
    """
    return calendar.monthrange(year_v, mon_v)[1]


def get_first_day_month(n=0):
    """
    get the first day of month from today
    n is how many months
    :param n:
    :return:
    """
    y, m, d = get_year_and_month(n)
    d = "01"
    arr = (y, m, d)
    return "-".join("%s" % i for i in arr)


def get_year_and_month(n=0):
    """
    get the year,month,days from today
    befor or after n months
    :param n:
    :return:
    """
    this_year = int(year)
    this_mon = int(month)
    total_mon = this_mon + n
    if n >= 0:
        if total_mon <= 12:
            days = str(get_days_of_month(this_year, total_mon))
            total_mon = add_zero(total_mon)
            return year, total_mon, days
        else:
            i = total_mon // 12
            j = total_mon % 12
            if j == 0:
                i -= 1
                j = 12
            this_year += i
            days = str(get_days_of_month(this_year, j))
            j = add_zero(j)
            return str(this_year), str(j), days
    else:
        if 0 < total_mon < 12:
            days = str(get_days_of_month(this_year, total_mon))
            total_mon = add_zero(total_mon)
            return year, total_mon, days
        else:
            i = total_mon // 12
            j = total_mon % 12
            if j == 0:
                i -= 1
                j = 12
            this_year += i
            days = str(get_days_of_month(this_year, j))
            j = add_zero(j)
            return str(this_year), str(j), days


def add_zero(n):
    """
    add 0 before 0-9
    return 01-09
    :param n:
    :return:
    """
    nabs = abs(int(n))
    if nabs < 10:
        return "0" + str(nabs)
    else:
        return nabs


def get_today_month(n=0):
    """
    获取当前日期前后N月的日期
    if n>0, 获取当前日期前N月的日期
    if n<0, 获取当前日期后N月的日期
    date format = "YYYY-MM-DD"
    :param n:
    :return:
    """
    y, m, d = get_year_and_month(n)
    arr = (y, m, d)
    if int(day) < int(d):
        arr = (y, m, day)
    return "-".join("%s" % i for i in arr)


def main():
    print(f'today is:{today()}')
    print(f'today is:{today_str()}')
    print(f'the date time is:{date_time()}')
    print(f'data time is:{date_time_str()}')
    print(f'2 days after today is:{get_day_of_day(2)}')
    print(f'2 days before today is:{get_day_of_day(-2)}')
    print(f'2 months after today is:{get_today_month(2)}')
    print(f'2 months before today is:{get_today_month(-2)}')
    print(f'2 months after this month is:{get_first_day_month(2)}')
    print(f'2 months before this month is:{get_first_day_month(-2)}')


if __name__ == "__main__":
    main()
