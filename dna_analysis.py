# Name: Stephen Rancourt
# Evergreen Login: ranste07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
total_count1 = 0
total_count2 = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
g_count = 0
t_count = 0
c_count = 0
sum_count = 0
seq_length = 0
at_over_gc = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G,
    if bp == 'G':
        # increment the count of g
        g_count = g_count + 1
    # next, if the bp is an c,
    elif bp == 'C':
        # increment the count of c
        c_count = c_count + 1
    # next, if the bp is an a,
    elif bp == 'A':
        # increment the count of a
        a_count = a_count + 1
    # next, if the bp is an t,
    elif bp == 'T':
        # increment the count of t
        t_count = t_count + 1
        
# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count2 = total_count2 + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count1 = total_count1 + 1

    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1

sum_count = g_count + a_count + c_count + t_count
seq_length = len(seq)

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
at_over_gc = float(at_count) / float(gc_count)

#check gc_content
if (gc_content > 0.6):
    print 'high GC content'
elif (gc_content < 0.4):
    print 'low GC content'
else:
    print 'moderate GC content'

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G-content:', g_count
print 'C-content:', c_count
print 'A-content:', a_count
print 'T-content:', t_count
print 'Sum count:', sum_count
print 'Total count:', total_count
print 'Seq length:', seq_length
print 'AT/GC:', at_over_gc