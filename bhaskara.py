print("2 degree equation solver\n github.com/Daniib0y")
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
delta = b ** 2 - 4 * a * c
print("Delta: {}".format(delta))
raizdelta = delta ** 0.5
if raizdelta > 0:
    menosb = b - b - b
    x = (menosb + raizdelta)/(2*a)
    x2 = (menosb - raizdelta)/(2*a) 
    print("x1 = {} x2 = {}".format(x,x2))
else:
    print("Delta negative, delta is = {}".format(raizdelta))

# The 'if' ins't working and i dont know why
# 05/03/2020
