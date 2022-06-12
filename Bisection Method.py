import matplotlib.pyplot as plt
from sympy import Symbol


def bisection_method(fx, a0, b0, itr):
  count = 0
  print("-------------------------------------------------------------------------")
  print("count\t\tan\t\tbn\t\txn\t\tf(xn)")
  print("-------------------------------------------------------------------------")
  while True:
    x = Symbol('x')
    ai = eval(str(fx),{"x": a0})
    bi = eval(str(fx),{"x": b0})
    
    xn = (a0 + b0) / 2
    xi = eval(str(fx),{"x": xn})
    
    print(str(count) +"\t   "+"{:.6f}".format(a0)+"\t   "+"{:.6f}".format(b0)+"\t   "+"{:.6f}".format(xn)+"\t   "+"{:.6f}".format(xi))
    if xi < 0:
      if ai < 0:
        a0 = xn
      elif bi < 0:
        b0 = xn
    elif xi > 0:
      if ai > 0:
        a0 = xn
      elif bi > 0:
        b0 = xn
    count = count + 1
    if count > itr:
      break
  print("-------------------------------------------------------------------------")

  
def main():
  fx = input("Enter the equation: ")
  a0 = float(input("Enter the lower bound of the interval: "))
  b0 = float(input("Enter the upper bound of the interval: "))
  itr = int(input("How many times you want to iterate: "))
  bisection_method(fx, a0, b0, itr)

main()
