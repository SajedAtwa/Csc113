import math

def mathematical_exp(x,z):
     m = ((1/(1-x))/(z+x)**(1/(math.e)))**(1/(math.e))
     return m

x = 0.2
z = 10
d = mathematical_exp(x,z)
print(d)