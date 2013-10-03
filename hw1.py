# Name: Stephen Rancourt
# Evergreen Login: ranste07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available
import hw1_test

###
### Problem 1
###

print "Problem 1 solution follows:"

p = 1
q = -5.86
r = 8.5408

rootOne = (-q + math.sqrt(q ** 2 - 4 * p * r))/ 2 * p

rootTwo = (-q - math.sqrt(q ** 2 - 4 * p * r))/ 2 * p

print rootOne

print rootTwo

###
### Problem 2
###

print "Problem 2 solution follows:"

print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f

###
### Problem 3
###

print "Problem 3 solution follows:"

a = hw1_test.a
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

print ((a and b) or (not c) and not (d or e or f))

###
### Collaboration
###

# Rel as collaborator for importing on problem 2
