import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def newton_raphson(fx, x0):
	x = Symbol('x')
	f_x = diff(fx, x)
	h = eval(str(fx),{"x": x0}) / eval(str(f_x),{"x": x0})
	xlist = np.array([])
	ylist = np.array([])
	while abs(h) >= 0.0001:
		h = eval(str(fx),{"x": x0}) / eval(str(f_x),{"x": x0})
		xn = x0 - h
		yn = eval(str(fx),{"x": xn})
		xlist = np.append(xlist, xn)
		ylist = np.append(ylist, yn)
		x0 = xn
    
	x0 = round(x0, 6)
	print(f"The root of equation is {x0}")
	print(xlist)
	print(ylist)
	plt.rcParams["figure.figsize"] = (15, 10)
	plt.plot(xlist, ylist, marker = 'o')
	font1 = {'family':'fantasy','color':'blue','size':20}
	plt.xlabel("Xn")
	plt.ylabel("f(Xn)")
	plt.title("Newton Rapshon Method", fontdict= font1)

	plt.show()
  
def main():
	x = Symbol('x')
	fx = input("input your equation : ")
	x0 = float(input("Initial approximation:"))
	newton_raphson(fx, x0)
  
main()
