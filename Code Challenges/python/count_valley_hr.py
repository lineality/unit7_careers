# 2020.04.27 ?

# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# (user)problem: we know the sequence of down and up steps
# we know starting and ending is sea-level
# we know mointain and valley are defined relative to sea level
# but we do not know (we need to know)
# how many vallys were crossed
# we can ignore n
# the path is string form
# path is up or down
#
# solution(product):
# co
# iterate through the path
# track the elevation_units
# track last value and this value
# every time you go from -1 to 0: increment vally_crossed

import math
import os
import random
import re
import sys

s = "UDDDUDUU"  # the path(steps?)

# Complete the countingValleys function below.
def countingValleys(n, s):
    # convert s to a list of individual steps
    s = list(s)

    # make valley_counter
    valley_counter = 0

    # make current_elevation tracker
    current_elevation = 0
    # make last_elevation tracker
    last_elevation = 0

    # iterate through path
    for step in s:
        # update elevation tracker: if "Up", increment
        if step == "U":
            current_elevation += 1
        else:  # if down "D", decriment
            current_elevation -= 1

        # update valley
        if last_elevation == -1 and current_elevation == 0:
            valley_counter += 1

        # update last_elevation tracker
        last_elevation = current_elevation

    return valley_counter


countingValleys(0, s)
