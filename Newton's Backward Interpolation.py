import numpy as np
import matplotlib.pyplot as plt
import math

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
		check = int(input("Do you want add more values?(yes: 1 / no: 0): "))

  	return x, y

def differences(y):
	diff = np.empty([len(y)-1, len(y)-1])
	for j in range(len(y)-1):
		for i in range(len(y)-1-j):
		  if j == 0:
			diff[i][j] = y[i+1] - y[i]
		  else:
			diff[i][j] = diff[i+1][j-1] - diff[i][j-1]
	return diff

def print_diff_table(x,y, diff):
	print("\n Backward Differnce Table")
	print("---------------------------------------------------------------------------------------")
	print("x\t\ty", end = "\t\t")
  	for i in range(len(y)-1):
    	print(f"Δ{i+1}y", end = "\t\t")
  	print("\n")
  	print("---------------------------------------------------------------------------------------")
  	for m in range(len(y)):
    	print("{:.6f}".format(x[m]),"\t","{:.6f}".format(y[m]), end = "\t")
    	for n in range(len(y)-1-m):
      		print("{:.6f}".format(diff[m][n]), end = "\t")
    	print("\n")
  	print("---------------------------------------------------------------------------------------")
  
def calculation(x, y, x_in, h, diff):
  	y_out = y[len(y)-1]
  	for i in range(len(y)-1):
    	u = 1
    	for n in range(i+1):
      		u = u * (((x_in - x[len(y)-1])/h) + n)
    	y_out = y_out + (u * diff[len(y)-2-i][i]) / math.factorial(i+1) 
  	return y_out

def plot(x, y, x_in, y_out):
	plt.rcParams["figure.figsize"] = (15, 10)
	plt.plot(x, y, marker = 'o')
	font1 = {'family':'monospace','color':'blue','size':30}
	plt.xlabel("Xn")
	plt.ylabel("f(Xn)")
	plt.title("Newton's Backward Interpolation", fontdict= font1)
	plt.annotate(f"f({x_in}) =  {y_out:.6f}", (x_in, y_out))
	plt.show()
  
def main():
	print("Newton's Backward Interpolation")
	x, y = taking_input()
	h = float(input("Enter the common difference between x-values: "))
	diff = differences(y)
	print_diff_table(x,y,diff)
	x_in = float(input("Enter the x-value for which you want the y-value: "))
	y_out = calculation(x,y,x_in,h,diff)
	print(f"The y-value of {x_in} = {y_out:.6f}")
	x = np.sort(np.append(x, x_in))
	y = np.sort(np.append(y, y_out))
	plot(x, y, x_in, y_out)
  
main()
