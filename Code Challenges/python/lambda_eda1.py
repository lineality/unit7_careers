# (User)Problem
# we know: functions exist
# we need: function must be lambda optimized
# we must: lambda functions must be call-able
#
# Solution(Product)
# convert functions to call-able lambas


add_2 = lambda x: x + 2

add_3 = lambda x: x + 3

add_5 = lambda x: x + 5

add_7 = lambda x: x + 7

add_11 = lambda x: x + 11

# original
# def add_2(x):
# 	return x + 2
#
# def add_3(x):
# 	return x + 3
#
# def add5(x):
# 	return x + 5
#
# def add_7(x):
# 	return x + 7
#
# def add_11(x):
# 	return x + 11

# code from coder named "haskell":
# for n in range(12):exec("add_%s=lambda x:x+%s"%(n,n))
