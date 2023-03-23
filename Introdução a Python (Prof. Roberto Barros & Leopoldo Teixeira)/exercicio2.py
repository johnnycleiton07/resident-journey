from spatialmath import *
from math import pi

# R = SO2(-pi/2)
# print (R)

# R2 = SO2(90, unit='deg')
# print (R2)

# a = [1,0]

# a_1 = R * a
# print (a_1)

H1 = SE2(pi/2)
print (H1)

H2 = SE2(1,2)
print (H2)

H3 = H1 * H2
print (H3)

a = [1,0]

