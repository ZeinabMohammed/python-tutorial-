month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 30]
def is_leap(year):
    """return True for leap year , false for nin-leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)
def days_in_month(year, month):
    """return nomber of dayes in that months in that year"""
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print (days_in_month(2017, 2))
