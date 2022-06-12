from sympy import Symbol

def regula_falsi(fx, a, b):
  x = Symbol('x')
  for i in range(1000):
    c = (a * eval(str(fx),{"x": b}) - b * eval(str(fx),{"x": a})) / (eval(str(fx),{"x": b}) - eval(str(fx),{"x": a}))
    if eval(str(fx),{"x": c}) == 0:
      break
    elif eval(str(fx),{"x": c}) * eval(str(fx),{"x": a}) < 0:
      b = c
    else:
      a = c
  print("The root of the equation is " + "{:.6f}".format(c))      
  
def main():
  fx = input("Enter the equation: ")
  a = float(input("Enter your first approximation: "))
  b = float(input("Enter your second approximation: "))
  regula_falsi(fx, a ,b)
  
main()
