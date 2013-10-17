# Name: Stephen Rancourt
# Login: ranste07
#Collaborators : Cody, Alexei

fib1 = 0
fib2 = 1
fib3 = 1
n = 7
i = n
add = 0
total = 0
series = 'fibonacci'

if series == 'fibonacci':
    if n == 0: print 0
    elif n == 1: print 1
    else: 
        for n in range (0, (n-1)):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        print (fib3)

elif series == 'sum':
    while (i > 0):
        add = (3 * i)
        i = i - 1
        total = total + add
    print total

else:
    print "Invalid String"
