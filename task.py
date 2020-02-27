def firstrun():
    return "success"


def calcArea(r):
    return r * 3.14 * r


def listEnds(input):
    result = [input[0], input[len(input) - 1]]
    return result


def diffDates(date1, date2):
    return (date2-date1).days
