import math


def firstrun():
    return "success"


def circle_area(radius):
    area = (radius * radius)
    area = math.pi * area
    return area


def list(input):
    first_last = [input[0], input[-1]]
    return first_last


def days(date1, date2):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year1 = date1[2]
    month1 = date1[1]
    day1 = date1[0]
    total1 = (year1 * 365) + day1
    for i in range(0, month1 - 1):
        total1 += months[i]

    year2 = date2[2]
    month2 = date2[1]
    day2 = date2[0]
    total2 = (year2 * 365) + day2
    for i in range(0, month2 - 1):
        total2 += months[i]

    diff = total2 - total1
    return diff
