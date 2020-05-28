# (User) Problem
# We know / We have: 3 number: win draw lose
# We need / We don't have: points for team
# We must: use: 3 points for win, 1 for draw, 0 for loss
# name of function must be: football_points
#
# Solution (Product)
# function with 3 inputs
def football_points(wins, draws, losses):
    return wins * 3 + draws


# alt: Lambda Version
#
# football_points = lambda x, y, z: x * 3 + y
