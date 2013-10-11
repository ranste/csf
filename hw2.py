# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

x = 0
c = 0
total = 0
while (x < 100):
    x = (x + 1)
    c = (c + 1)
    total = (total + c)
print total
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

nums = [ (1.0/2), (1.0/3), (1.0/4), (1.0/5), (1.0/6), (1.0/7), (1.0/8), (1.0/9), (1.0/10) ]
for num in nums:
    print num


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(0, 9):
    triangular = n * (n + 1) / 2
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n * (n + 1) / 2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

m = 10
factorial = 0
for i in range(0, 9):
    factorial = math.factorial(m)
print "Factorial:", factorial

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
factorialout = 0
while (numlines > 0):
    factorialout = math.factorial(numlines)
    print "Factorial of", numlines, ":", factorialout
    numlines = numlines - 1


###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numline = 10
reciprocals = 0
total = 1.0
while (numline > 0):
    reciprocals = (1.0 / math.factorial(numline))
    total = total + reciprocals
    numline = numline - 1
print total
###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
