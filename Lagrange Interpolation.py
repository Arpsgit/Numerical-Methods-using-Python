import numpy as np
import matplotlib.pyplot as plt

def taking_input():
  check = 1
  i = 0
  x = np.array([])
  y = np.array([])
  while check != 0:
    a = float(input(f"Enter x[{i}]: "))
    b = float(input(f"Enter y[{i}]: "))
    x = np.append(x, a)
    y = np.append(y, b)
    i = i + 1
    check = int(input("Do you want to add more values?(yes: 1 / no: 0): "))

  return x, y

def calculation(x, y, x_in):
  y_out = 0
  for m in range(len(x)):
    num_x = 1
    den_x = 1
    for i in range(len(x)):
      if m != i:
        num_x = num_x * (x_in - x[i])
    for n in range(len(x)):
      if m != n:
        den_x = den_x * (x[m]-x[n])
    frac_x = num_x / den_x
    y_out = y_out + (frac_x * y[m])
  return y_out

def plot(x, y, x_in, y_out):
  plt.rcParams["figure.figsize"] = (15, 10)
  plt.plot(x, y, marker = 'o')
  font1 = {'family':'monospace','color':'blue','size':30}
  plt.xlabel("Xn")
  plt.ylabel("f(Xn)")
  plt.title("Lagrange Interpolation", fontdict= font1)
  plt.annotate(f"f({x_in}) =  {y_out:.6f}", (x_in, y_out))
  plt.show()
  
def main():
  print("Lagrange Interpolation")
  x, y = taking_input()
  x_in = float(input("Enter the x-value for which you want the y-value: "))
  y_out = calculation(x, y, x_in)
  print(f"The y-value of {x_in} = {y_out:.6f}")
  x = np.sort(np.append(x, x_in))
  y = np.sort(np.append(y, y_out))
  plot(x, y, x_in, y_out)
  
main()
