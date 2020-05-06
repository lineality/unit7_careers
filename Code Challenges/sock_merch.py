# 2020.04.25 ?
import math
import os
import random
import re
import sys

# (user)problem: we know the color of each sock
# but we do not know (need to know)
# how many matching pairs there are

# solution(product):
# use [].count(i)
# to get the number of appearances
# if that number is mod%2=0
# add that number to the pair list
# if not, add that number -i
# ignore n

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    number_of_matching_pairs = 0

    # make a list of colors
    color_list = set(ar)
    print(color_list)

    # iterate though list of colors, and find out how many occurances
    for color in color_list:
        occurences = ar.count(color)
        if occurences % 2 == 0:
            print("if", occurences)
            number_of_matching_pairs += occurences / 2
        else:
            number_of_matching_pairs += (occurences - 1) / 2
            print("else", occurences)
    return int(number_of_matching_pairs)


sockMerchant(0, [10, 20, 20, 10, 10, 30, 50, 10, 20])
