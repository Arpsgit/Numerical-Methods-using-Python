from sympy import Symbol

def secant_method(fx, a, b, itr):
  x = Symbol('x')
  if eval(str(fx),{"x": a}) * eval(str(fx),{"x": b}) < 0:
    for i in range(itr):
      c = (a * eval(str(fx),{"x": b}) - b * eval(str(fx),{"x": a})) / (eval(str(fx),{"x": b}) - eval(str(fx),{"x": a}))
      a = b
      b = c
    print("The root of the equation is " + "{:.6f}".format(c))
  else:
    print("Invalid interval")
    
def main():
  fx = input("Enter the equation: ")
  a = float(input("Enter your first approximation: "))
  b = float(input("Enter your second approximation: "))
  itr = int(input("Enter the desired no of iteration: "))
  secant_method(fx, a ,b, itr)
  
main()
