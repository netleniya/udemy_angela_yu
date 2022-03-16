import random


def is_leap(year):
    """Determine if given year is a leap year"""
    return True if (not year % 4 and year % 100) or (not year % 400) else False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


def main():
    test_years = [1900, 1908, 1988, 2000, 2004]

    for year in test_years:
        print(days_in_month(year, month=random.randint(1, 12)))


if __name__ == "__main__":
    main()
