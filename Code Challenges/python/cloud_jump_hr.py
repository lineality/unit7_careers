# 2020.04.27-28

# sample input
# c = [0, 0, 1, 0, 0, 1, 0]
# c = [0, 0, 0, 1, 0, 0]
# print(len(c))

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/

import math
import os
import random
import re
import sys

# (user)problem:
# The user has a list of 0's and 1's they have to navigate a path through.
# but the user does not know (the user needs to know):
# the number of steps in the shortest path (not the path itself) through list.
# rules etc:
# the user can jump over one-next-item (advance 2), or not jump (advance 1),
# the user can only travel on zeros, not 1's (must jump over 1)
#
# solution(product):
# ~traverse through the list of numbers, using
# a progress_marker and
# as the index in the list: list[marker]
# Only 2 conditions (plus exit):
# If the next-next number is a zero, jump. else, move ahead one. (until end)
# record how many clouds you touch, finally:
# return that 'how many clouds touched' number


def jumpingOnClouds(c):

    # variables
    cloud_touch_counter = 0  # ~step counter
    this_cloud = 0  # where you are

    # ~iterate through list of "clouds"
    # checking what the next.next cloud is:
    # there are only 2 choices (not including exit):
    #  if the next next spot is zero: jump there
    #  if not, but the next spot exists: jump there
    #  (if no more clouds: exit)
    while this_cloud < len(c):

        # option 1:2, look ahead 2, go ahead 2
        if this_cloud < (len(c) - 2) and c[this_cloud + 2] == 0:
            this_cloud += 2

        # option 2:2, go ahead 1
        elif this_cloud < (len(c) - 1):
            this_cloud += 1

        else:  # exit: if this is the last cloud
            break

        cloud_touch_counter += 1

    return cloud_touch_counter


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()
