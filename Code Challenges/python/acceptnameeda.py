# (User) Problem
# We know: a name input, a welcome message
# We need (we don't yet have):
# output with the two together
# a function called 'func'
# We must: string input and output
#
# Solution (Product)
# use f-string to put the input into the outout

# fstrings not accepted for no known reason
# def func(name_input):
#     return f"Welcome {name_input}"


def func(name_input):
    return "Welcome " + name_input


# def func(name_input):
#     return f"Welcome {name_input}"


# Lambda version
# func = lambda name_input: f"Welcome {name_input}"
