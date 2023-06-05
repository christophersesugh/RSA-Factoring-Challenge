import math
from pollard import pollard_strassen

def factorize(number):
    """Function to factorize numbers"""
    if number <= 1:
        print("Number must be > 1")
    r =  pollard_strassen(number)
    print(r)
    #for i in range(2, math.isqrt(number) + 1):
     #   if number % i == 0:
      #      print("{:d}={:d}*{:d}".format(number, number//i, i))
       #     break
