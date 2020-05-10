# (User) Problem:
# We know: hours and mintues
# We Need: seconds
# We Must: intput 2, return 1 number
#
# Solution (Product):
# translate hours into  hours_to_seconds
# translate minutes_to_seconds
# add and return the two translated


def convert(hours, minutes):
    hours_to_seconds = hours * 60 * 60
    minutes_to_seconds = minutes * 60
    return hours_to_seconds + minutes_to_seconds
