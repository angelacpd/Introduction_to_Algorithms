# Comparison of running times
# For each function f .n/ and time t in the following table, determine the largest
# size n of a problem that can be solved in time t , assuming that the algorithm to
# solve the problem takes f .n/ microseconds.

import math


t = 0.000001    # microsecond
n1 = 10**6      # second
n2 = 60 * n1    # minute
n3 = 60 * n2    # hour
n4 = 24 * n3    # day
n5 = 30 * n4    # month of 30 days
n6 = 365 * n4   # year of 365 days
n7 = 100 * n6   # century
t1 = True
t2 = True
t3 = True
t4 = True
t5 = True
t6 = True
t7 = True

tsum = 0
stop = n7
n = 1
while n <= stop:
    fun = math.log(n, 2)
    tsum += fun
    if tsum >= n1 and t1:
        print("For t = 1 sec, n = {} and lg(n) = {}".format(n, fun))
        t1 = False
    if tsum >= n2 and t2:
        print("For t = 1 min, n = {} and lg(n) = {}".format(n, fun))
        t2 = False
    if tsum >= n3 and t3:
        print("For t = 1 hour, n = {} and lg(n) = {}".format(n, fun))
        t3 = False
    if tsum >= n4 and t4:
        print("For t = 1 day, n = {} and lg(n) = {}".format(n, fun))
        t4 = False
    if tsum >= n5 and t5:
        print("For t = 1 month, n = {} and lg(n) = {}".format(n, fun))
        t5 = False
    if tsum >= n6 and t6:
        print("For t = 1 year, n = {} and lg(n) = {}".format(n, fun))
        t6 = False
    if tsum >= n7 and t7:
        print("For t = 1 century, n = {} and lg(n) = {}".format(n, fun))
        t7 = False
        break
    n += 1

fun2 = math.sqrt(n)
fun3 = n
fun4 = n*math.log(n, 2)
fun5 = math.pow(n, 2)
fun6 = math.pow(n, 3)

try:
    fun7 = math.pow(2, n)
except OverflowError as error:
    print("OverflowError: Result of an arithmetic operation is too large to be represented.")
    print("n = {}".format(n))

try:
    fun8 = math.factorial(n)
except OverflowError as error:
    print("OverflowError: Result of an arithmetic operation is too large to be represented.")
    print("n = {}".format(n))
