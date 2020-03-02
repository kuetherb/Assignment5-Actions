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
