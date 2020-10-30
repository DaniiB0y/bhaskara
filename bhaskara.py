
import math 

print("2 degree equation solver\n github.com/Daniib0y")	print("2 degree equation solver\n github.com/Daniib0y")
a = float(input('A: '))	a = float(input('A: '))
b = float(input('B: '))	b = float(input('B: '))
c = float(input('C: '))	c = float(input('C: '))

delta = b ** 2 - 4 * a * c	delta = b ** 2 - 4 * a * c
print("Delta: {}".format(delta))	print("Delta: {}".format(delta))
raizdelta = delta ** 0.5	
if raizdelta > 0:	if delta > 0:
    menosb = b - b - b	    raizdelta = math.sqrt(delta)
    x = (menosb + raizdelta)/(2*a)	    x = (-b + raizdelta)/(2*a)
    x2 = (menosb - raizdelta)/(2*a) 	    x2 = (-b - raizdelta)/(2*a) 
    print("x1 = {} x2 = {}".format(x,x2))	    print("x1 = {} \nx2 = {}".format(x,x2))
else:	else:
    print("Delta negative, delta is = {}".format(raizdelta))	    print("Delta negative, delta is = {}".format(delta))




# The 'if' ins't working and i dont know why	# The 'if' ins't working and i dont know why
# 05/03/2020	# 05/03/2020

# The 'if' is now working
# 24/03/2020
