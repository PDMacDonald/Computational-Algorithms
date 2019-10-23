from math import exp

#author Preston MacDonald
#last Edit: 10-25-2017
#Mat 2310-101 Derivative Homework

# Problem number 1
# Procedure that approximates the derivative of a given function using the central difference quotient.
# Note: Output is an estimated value.
#
# @param f
#     function to be evaluated.
# @param x
#     Value of x to approximate the derivative at.
def deriv(f, x):
  
  tolerance = 1e-6
  h = 0.5
  preEst = 0;
  estimate = ( f((x + h)) - f((x - h)) ) / (2 * h);
  
  while(abs(estimate - preEst) > tolerance):
    preEst = estimate;
    h = h / 2
    estimate = ( f((x + h)) - f((x - h)) ) / (2 * h)
    
    # For troubleshooting
    # print("x= %6f h= %8f preEst= %8f estimate= %8f" % (x, h, preEst, estimate))


  print("The derivative at %6f is %6f." % (x, estimate))
  
  return
  
# Test function for Problem #1
# Function is e^x
# Derivative: e^x
#
# @param x
#     variable to evaluate function at.
def testOne(x):
  return exp(x)

# Test function for Problem #1
# Function is (x^3) + (x^2)
# Derivative: (3x^2) + (2x)
#
# @param x
#     variable to evaluate function at.
def testTwo(x):
  return pow(x, 3) + pow(x, 2)
  
# Test function for Problem #1
# Function is (x^2)(e^x)
# Derivative: (2x * e^x) + ((e^x)*(x^2))

# @param x
#     variable to evaluate function at.
def testThree(x):
  return pow(x, 2) * exp(x)

print("Problem #1\n")

print("test One: f(x) = e^x; x = 1; estimate should be approximently: 2.718281")
deriv(testOne, 1)

print("\ntest Two: f(x) = (x^3) + (x^2); x = -3.24; estimate should be approximently: 2153.8507")
deriv(testTwo, -27.13)

print("\ntest Three: f(x) = (x^2)(e^x); x = -1; estimate should be approximently: -0.367879441171")
deriv(testThree, -1)

















