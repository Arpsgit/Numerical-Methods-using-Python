from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def nr_method_two_var(fxy, gxy, x0, y0, rep):
  x = Symbol('x')
  y = Symbol('y')
  xplot = np.array([])
  yplot = np.array([])
  fx_y = diff(fxy, x)
  fxy_ = diff(fxy, y)
  gx_y = diff(gxy, x)
  gxy_ = diff(gxy, y)
  i = 0
  print("--------------------------------------")
  print("x-values \t\t y-values")
  print("--------------------------------------") 
  while i <= rep:
    xn = x0 - ((eval(str(gxy_), {"x": x0, "y": y0}) * eval(str(fxy), {"x": x0, "y": y0})) - (eval(str(fxy_), {"x": x0, "y": y0}) * eval(str(gxy), {"x": x0, "y": y0}))) / ((eval(str(fx_y), {"x": x0, "y": y0}) * eval(str(gxy_), {"x": x0, "y": y0})) - (eval(str(fxy_), {"x": x0, "y": y0}) * eval(str(gx_y), {"x": x0, "y": y0})))
    yn = y0 - (-(eval(str(gx_y), {"x": x0, "y": y0}) * eval(str(fxy), {"x": x0, "y": y0})) + (eval(str(fx_y), {"x": x0, "y": y0}) * eval(str(gxy), {"x": x0, "y": y0}))) / ((eval(str(fx_y), {"x": x0, "y": y0}) * eval(str(gxy_), {"x": x0, "y": y0})) - (eval(str(fxy_), {"x": x0, "y": y0}) * eval(str(gx_y), {"x": x0, "y": y0})))
    
    #print(f"  {round(xn, 6)}\t\t{round(yn, 6)}")
    print("{:.6f}".format(xn)+"\t\t"+"{:.6f}".format(yn))
    x0 = xn
    y0 = yn
    xplot = np.append(xplot, xn)
    yplot = np.append(yplot, yn)
    i = i + 1
  print("--------------------------------------")  
  plt.rcParams["figure.figsize"] = (15, 10)
  plt.plot(xplot, yplot, marker = '*')
  plt.show()
  
def main():
  x = Symbol('x')
  y = Symbol('y')
  fxy = input("input your equation : ")
  gxy = input("input your equation : ")
  x0 = float(input("Enter the value of x0: "))
  y0 = float(input("Enter the value of y0: "))
  rep = int(input("Enter the no. of repeataion: "))
  nr_method_two_var(fxy, gxy, x0, y0, rep)
  
main()
