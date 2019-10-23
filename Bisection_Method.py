from math import exp
from math import pi
from math import tan
from math import sin

#author Preston MacDonald
#last Edit: 11-01-2017
#Mat 2310-101 Bisection Homework Python Portion

# Problem number 3
# Procedure to implement the bisection method.
# 
# @param f
#       Externally defined function.
# @param a
#       left end point.
# @param b
#       right end point.
# @param tol
#       tol is the bound on the absolute error.
# @return an approximation of the root between the given end points.
def bisect(f, a, b, tol):
  
  #variables
  n = 0
  maxIterations = 100 #max number of iterations that can occur
  newA = a
  newB = b
  fa = f(a)
  fb = f(b)
  
  if (fa * fb >= 0):
    print("ERROR, function at a and b must have different signs.")
    print("f(a) =", fa)
    print("f(b) =", fb)
    print("The function at", a, "and", b, "have the same signs.")
    
    return
  
  for n in range(maxIterations):
    
    c = .5 * (newB + newA)
    fc = f(c)
    
    #For debugging purposes
    print(newA, "...", newB, "...", c, "...", fa, "...", fb, "...", fc, "iterations", n)
    
    error = newB - newA
    
    if (abs(error) <= tol or fc == 0):
       print("The approximate solution is %6f which was found in %i iterations." % (((newB + newA)/2), n))
       
       return
    
    if(fa * fc < 0):
      newB = c
      fb = fc
    else:
      newA = c
      fa = fc

  print("The function did not converge to the root in,", maxIterations, "iterations.")
  
  return


# Test function for Problem #3
# Function is (x^2) - e^(-x)
#
# @param x
#     variable to evaluate function at.
def testOne(x):
  return pow(x, 2) - exp(-x)

  
# Test function for Problem #3
# Function is (x^3) + 3 * x^2
#
# @param x
#     variable to evaluate function at.
def testTwo(x):
  return pow(x, 3) + (3 * pow(x, 2))
  
# Test function for Problem #3
# Function is x^3
#
# @param x
#     variable to evaluate function at.
def testThree(x):
  return pow(x, 3)

print("\nBisection Test Cases")

print("\n\nTest #1")
print("f(x) = (x^2) - e^(-x), a = 0, a = 1, tolerance = 0.5, Actual value = 0.703")
print("output:")
bisect(testOne, 0, 1, .05)

print("\n\nTest #2")
print("f(x) = (x^2) - e^(-x), a = 1, a = 5, tolerance = .5*(10**(-6)), Actual value = DNE")
print("output:")
bisect(testOne, 1, 5, 1*(10**(-6)))

print("\n\nTest #3")
print("f(x) = (x^3) + 3 * x^2, a = -2, a = -4, tolerance = .5*(10**(-6)), Actual value = -3")
print("output:")
bisect(testTwo, -4, -2, 1*(10**(-6)))

print("\n\nTest #4")
print("f(x) = (x^3), a = -5, a = 5, tolerance = .5*(10**(-6)), Actual value = 0")
print("output:")
bisect(testThree, -2, 3, 1*(10**(-6)))


# Problem #4 exercise 17 on pages 125.

def probNumFour(x):
  wOne = 9
  wTwo = 7
  angle = 2.18166
  
  return wOne * (1/tan(pi - angle - x)) * (1/sin(pi - angle - x)) - wTwo * (1/tan(pi - angle - x)) * (1/sin(pi - angle - x))

print("\n\n\nProblem Number 4 Exercise 17 on page 125")
print("output:")
bisect(probNumFour, 2, 3, 1*(10**(-6)))


# Problem #6
def probNumSix(x):

  return ((4 * sin(x)) / (3 * x)) - 1

print("\n\n\nProblem Number 6")
print("output:")

bisect(probNumSix, .000001, pi/2, 1*(10**(-9)))










