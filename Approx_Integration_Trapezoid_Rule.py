from math import exp
from math import pi
from math import tan
from math import sin

#author Preston MacDonald
#last Edit: 11-09-2017
#Mat 2310-101 Trapezoid Homework Python Portion

# Problem number 2
# Procedure to implement the Composite Trapezoid rule method.
# 
# @param f
#       Externally defined function.
# @param a
#       left end point.
# @param b
#       right end point.
# @param n
#       number of subintervals
# @return an approximation of integrating a given f(x) over a interval a to b.
def trap(f, a, b, n):
  
  if(b <= a):
    print("ERROR, Your b end point must be greater than a. ")
    print("Your b input =", b, "Your a input =", a)
    return
  if(n <= 0):
    print("ERROR, subintervals must be a value greater than 0.")
    print("Your n input =", n)
    return
  
  deltaX = (b - a) / n
  summ = f(a) + f(b)
  
  for i in range(1, n):
    summ = summ + (2 * f(a + (i * deltaX)))
  
  summ = summ * deltaX / 2
  
  print("The approximate integral with", n, "subintervals is", summ)
  return
  
# Test function for Problem #2
# Function is 1/x^2
#
# @param x
#     variable to evaluate function at.
def testOne(x):
  return 1 / pow(x, 2)
  
# Test function for Problem #2
# Function is e^(-x^2)
#
# @param x
#     variable to evaluate function at.
def testTwo(x):
  return exp(-pow(x, 2))
  

print("\nTrapezoid Test Cases")

print("\n\nTest #1")
print("f(x) = 1/x^2, a = 1, b = 2, n = 2")
print("output:")
trap(testOne, 1, 2, 2)

print("\n\nTest #2")
print("f(x) = e^(-x^2), a = 0, b = 1, n = 60")
print("Book approximate value: 0.74681")
print("output:")
trap(testTwo, 0, 1, 60)

print("\n\nError Test #1")
print("f(x) = 1/x^2, a = 3, b = 2, n = 2")
print("output:")
trap(testOne, 3, 2, 2)
  
print("\n\nError Test #2")
print("f(x) = 1/x^2, a = 1, b = 2, n = 0")
print("output:")
trap(testOne, 1, 2, 0)


# Problem number 3
# Test trap() function on exercise #12 pg 214 with n = 10, 100, 1000
# Function is sin(x)
#
# @param x
#     variable to evaluate function at.
def probThree(x):
  return sin(x)
print("\n\n\n---------------------------------------------------")
print("\n\n\nProblem #3 Exercise 12 pg 214")
print("Exact value = 0.956449142415")

print("\n\nTest #1")
print("f(x) = sin(x), a = -1, b = 2, n = 10")
print("output:")
trap(probThree, -1, 2, 10)
print("Absolute Error:", (0.956449142415 - 0.9492649906850621))

print("\n\nTest #2")
print("f(x) = sin(x), a = -1, b = 2, n = 100")
print("output:")
trap(probThree, -1, 2, 100)  
print("Absolute Error:", (0.956449142415 - 0.9563774076535726))
  
print("\n\nTest #3")
print("f(x) = sin(x), a = -1, b = 2, n = 1000")
print("output:")
trap(probThree, -1, 2, 1000)  
print("Absolute Error:", (0.956449142415 - 0.9564484250783174))

#These computations proves that the error in the trapezoid rule is O(h^2).
# This is proven by examining the ratios of errors between 2 consecutive error values.
# 0.007184142414999983 / 7.214241499997609 = 99.5827824034
# So the ratio is approximentaly 100 which is predicted by O(h^2).


print("\n\n\n---------------------------------------------------")
print("\n\n\nProblem #4 Question 3 PG 216")

# Problem number 4
# Test trap() function on exercise #3 pg 216
# Function is 1/(1+x^2)
#
# @param x
#     variable to evaluate function at.
def probFour(x):
  return 4 / (1 + pow(x, 2))
  

print("\n\nApproximate PI")
print("f(x) = 4 / (1 + pow(x, 2)) , a = 0, b = 1, n = 81650")
print("output:")
print("Actual PI =", pi)
trap(probFour, 0, 1, 81650)



print("\n\n\n---------------------------------------------------")
print("\n\n\nProblem #5 Question 4 PG 216")

# Problem number 5
# Test trap() function on exercise #4 pg 216 with n = 100
# Function is sin(x/x)
#
# @param x
#     variable to evaluate function at.
def probFive(x):
  if(x == 0):
    return 1
    
  return sin(x/x)

#print("\n\nTest #1")
#print("f(x) = sin(x/x), a = 0, b = 0.8, n = 100")
#print("output:")
#trap(probFive, 0, 0.8, 100)

#Since f(x) = sin(x/x), when we attempt to find f(x_0) we have a illegal action of dividing by 0.
#The function f(x) will always be equal to sin(1) The function is therefore, only unedifined when x = 0
#Otherwise you will always have a x/x which will always result to 1.
  
print("\n\nTest Piecewise")
print("f(x) = sin(x/x), a = 0, b = 0.8, n = 100")
print("output:")
trap(probFive, 0, 0.8, 100)
  
  
  
  
  
  