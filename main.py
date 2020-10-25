def add(*argv):
  sum = 0 
  for arg in argv:
    sum += arg
  return sum

def main():
  add(67, 86, 86, 90, 39) 
  return 0
  
if __name__ == "__main__":
  main()
