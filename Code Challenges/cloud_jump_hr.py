# 2020.04.27-28
# sample input
# c = [0, 0, 1, 0, 0, 1, 0]
# c = [0, 0, 0, 1, 0, 0]

import math
import os
import random
import re
import sys

# (user)problem: 
# The user has a list of 0's and 1's to navigate a path through.
# but the user does not know (the user needs to know) 
# the number of steps in the shortest path (not the path itself).
# the user can jump over one-next-number, or not jump,
# the user can only travel on zeros, not 1's.
#
# solution(product): 
# iterate through the list of numbers, using the index (recording that index)
# if the next-next number is a zero, jump. else, move ahead one.
# record what numbers you 'land' on.

def jumpingOnClouds(c):

    # record stops along path
    cloud_touch_counter = 0

    this_cloud = 0

    # ~iterate through list of clouds
    # checking what the next.next cloud is:
    # there are 2 choices (not including exit)
    while this_cloud < len(c):
        # print("\nstart", this_cloud, c[this_cloud])

        # option 1:2, go ahead 2
        if this_cloud < (len(c) - 2) and c[this_cloud+2] == 0:
            # print('option 1')
            this_cloud += 2

        # option 2:2, go ahead 1
        elif this_cloud < (len(c) - 1):
            # print('option 2')
            this_cloud += 1

        else:  # if this is the last cloud:
            # print("exits")
            break

        # print("counter", cloud_touch_counter)

        cloud_touch_counter += 1  # increment cloud_touch_counter
    # print(c)
    return cloud_touch_counter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

