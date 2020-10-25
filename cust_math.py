class MyMath:
  def add(*argv):
    sum = 0 
    for arg in argv:
      sum += arg
    return sum

  def sub(*argv):
    res = 0 
    for arg in argv:
      res -= arg
    return res 

   def mul(*argv):
    res = 1
    for arg in argv:
      res *= arg
    return res 

   def div(f_arg, *argv):
    for arg in argv:
      f_arg /= arg
    return f_arg
    
def main():
   print("\n\tError: Cannot use this module as a main script.")
  
if __name__ == "__main__":
  main()
