def truncation_error(trvl, apprxvl):
  trncn_err = abs(trvl - apprxvl)
  return trncn_err

def absolute_error(trvl, apprxvl):
  abslt_err = abs(trvl - apprxvl)
  return abslt_err
  
def relative_error(trvl, apprxvl):
  rltv_err = absolute_error(trvl, apprxvl) / trvl
  return rltv_err
  
def relative_percentage_error(trvl, apprxvl):
  rltv_prcntg_err = relative_error(trvl, apprxvl) * 100
  return rltv_prcntg_err
  
def main():
  True_value = float(input("Enter the true value: "))
  Approx_value = float(input("Enter the approximate value: "))
  acc = int(input("How much accuracy do you want in decimal places: "))
  trncn = round(truncation_error(True_value, Approx_value), acc)
  abslt = round(absolute_error(True_value, Approx_value), acc)
  rltv = round(relative_error(True_value, Approx_value), acc)
  rltv_per = round(relative_percentage_error(True_value, Approx_value), acc)

  print(f"The truncation error is {trncn}")
  print(f"The absolute error is {abslt}")
  print(f"The relative error is {rltv}")
  print(f"The relative percentage error is {rltv_per}")
  
main()
