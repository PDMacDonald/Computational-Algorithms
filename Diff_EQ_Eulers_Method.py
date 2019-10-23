from math import exp
from math import pi
from math import tan
from math import sin
from math import cos

#author Preston MacDonald
#last Edit: 11-17-2017
#Mat 2310-101 Diff EQ Homework Python Portion

# Problem number 2
# Procedure to implement Eulers method to approximate the value of the solution for a
# differential equation.
# @param f
#       Externally defined function.
# @param a
#       left end point.
# @param b
#       right end point.
# @param xa
#       initial value
# @param n
#       Steps
# @return an approximation of the solution of the given differential equation.
def eule(f, a, b, xa, n):
  
  h = (b - a) / n
  t = a
  x = xa
  
  for i in range(n):
    x = x + h * f(t, x)
    t = t + h
  
  print("The approximate value of the solution at x =", b, "is", x)
  return
  
# MY OWN Test function for Problem #2
# Function is 1 + x^2 + t^3
#
# @param x
#     variable to evaluate function at.
def testOne(t, x):
  return 1 + x**2 + t**3
  
# Test case 3A
def test3A(t, x):
  return x
# Test case 3B
def test3B(t, x):
  return t + sin(x)
# Test case 3C
def test3C(t, x):
  return 0.001 * x * (900 - x)

print("\nEuler's Method Test Cases")

print("\n\nTest #1 MY OWN TEST From book")
print("x' = 1 + x^2 + t^3, a = 1, b = 2, xa = -4 n = 100")
print("Should equal =", 4.23585)
print("output:")
eule(testOne, 1, 2, -4, 100)

print("-----------------------------------------")


print("\n\nTest 3A")
print("x' = x, a = 0, b = 1, xa = 1, n = 1 ")
print("output:")
eule(test3A, 0, 1, 1, 1)

print("\n\nTest 3A with 2 steps")
print("x' = x, a = 0, b = 1, xa = 1, n = 2 ")
print("output:")
eule(test3A, 0, 1, 1, 2)

print("-----------------------------------------")

  
print("\n\nTest 3B")
print("x' = t + sin(x), a = 0, b = 1, xa = 1, n = 5")
print("output:")
eule(test3B, 0, 1, 1, 5)

print("Now with n = 25")
eule(test3B, 0, 1, 1, 25)

print("Now with n = 125")
eule(test3B, 0, 1, 1, 125)

print("Now with n = 625")
eule(test3B, 0, 1, 1, 625)

print("-----------------------------------------")

print("\n\nTest 3C")
print("x' = 0.001x(900 - x), a = 0, b = 12, xa = 200, n = 100")
print("output:")
eule(test3C, 0, 12, 200, 100)

print("-----------------------------------------")


# Problem number 4
# Procedure to implement Taylor series method of order 2 to approximate the value of 
# the solution for a equation.
# @param f
#       Externally defined function.
# @param a
#       left end point.
# @param b
#       right end point.
# @param xa
#       initial value
# @param n
#       Steps
# @return an approximation of the solution of the given differential equation.
def tay2de(f, fp, a, b, xa, n):

  h = (b - a) / n
  t = a
  x = xa
  
  for i in range(n):
    x = x + h * f(t, x) + (h**2 / 2) * fp(t, x)
    t = a + (i + 1) * h
  
  print("The approximate value of the solution at x =", b, "is", x)
  return

# Test case 5A
def test5A(t, x):
  return x
def test5AP(t, x):
  return x

# Test case 5B
def test5B(t, x):
  return t + sin(x)
def test5BP(t, x):
  return 1 + cos(x) * (t + sin(x))

# Test case 5C
def test5C(t, x):
  return 0.001 * x * (900 - x)
def test5CP(t, x):
  return (0.9 - 0.002 * x) * (0.001 * x * (900 - x))

print("\nTay2de Method Test Cases")

print("\n\nTest case 5A")
print("x' = x, xp = x, a = 0, b = 1, xa = 1, n = 1")
print("output:")
tay2de(test5A, test5AP, 0, 1, 1, 1)

print("\nTay2de Method Test Cases")

print("\n\nTest case 5A case 2")
print("x' = x, xp = x, a = 0, b = 1, xa = 1, n = 1")
print("output:")
tay2de(test5A, test5AP, 0, 1, 1, 2)

print("-----------------------------------------")

  
print("\n\nTest 5B")
print("x' = t + sin(x), xp = 1 + cos(x)(t + sin(x)), a = 0, b = 1, xa = 1, n = 5")
print("output:")
tay2de(test5B, test5BP, 0, 1, 1, 5)

print("Now with n = 25")
tay2de(test5B, test5BP, 0, 1, 1, 25)

print("Now with n = 125")
tay2de(test5B, test5BP, 0, 1, 1, 125)

print("Now with n = 625")
tay2de(test5B, test5BP, 0, 1, 1, 625)

print("-----------------------------------------")


print("\n\nTest 5C")
print("x' = 0.001x(900 - x), xp = (0.9 - 0.002x)x', a = 0, b = 12, xa = 200, n = 100")
print("output:")
tay2de(test5C, test5CP, 0, 12, 200, 100)








