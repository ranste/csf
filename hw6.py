# Name: Stephen Rancourt
# Evergreen Login: ranste07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 'pumpkin pie'
if n == 'apple pie':
    print "I like apple pie."
elif n == 'peach pie':
    print "I hate peach pie."
else:
    print "I don't mind other types of pie"


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

pies = ['apple','peach','blueberry','rhubarb','pumpkin','chocolate']
value = {'apple': 5, 'peach': 0, 'blueberry': 4, 'rhubarb': 1, 'pumpkin': 3, 'chocolate': 2}

print value

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

def valsearch(x, y):
    print x[y]

valsearch(value, 'blueberry')
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

for pie in pies:
    if value[pie] > 3:
        print ("This {} pie has a rating of {}." .format(pie, value[pie]))

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

morePies = ['key lime', 'lemon', 'mocha', 'Boston cream', 'mango', 'cherry', 'meat', 'sweet cream', 'strawberry', 'blackberry']
moreRatings = []

for i in range(10):
    moreRatings.append(i//2)

moreValues = {morePies[j]: moreRatings[j] for j in range(10)}

print moreValues
evenMorePies = pies + morePies
evenMoreValues = dict(value.items() + moreValues.items())
print evenMoreValues

for pie in evenMorePies:
    if evenMoreValues[pie] > 3:
        print ("This {} pie has a rating of {}." .format(pie, evenMoreValues[pie]))

###
### Collaboration - Got help from my brother on six and seven.
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
