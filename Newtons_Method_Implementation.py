#!/usr/bin/env python3
#shabang


"""
main.py: 3 programming problems.

MAT 4310
Homework Assignment #3
Last Modified: 2-23-2019
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonad"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Completed"


#imports
import math

#Python Question #1

#Implementation of a basic Newton's method.
# f is the function
# fp is the derivative of f.
# x0 is the initial guess
# TOL is the stopping  tolerance
# N is the maximum iterations allowed.
def Newt(f, fp, x0, TOL):
    
    x_old = x0
    N = 1

    while(True):

        der_fx = fp(x_old)

        if( abs(der_fx) < 1e-15):
            print("The derivative at an iterate with value", x_old, "is zero.")
            break

        x_new = x_old - (f(x_old) / der_fx)

        if(abs(x_new - x_old) < TOL):
            print("Starting at", x0, ", the solution to the equation is", x_new, "in", N, "iterations.")
            break
        elif( abs(x_new) > 1e10):
            print("The iterates tend to infinity.")
            break
        elif( N >= 20):
            print("The solution wasn't found in 20 iterations.")
            break

        x_old = x_new
        N += 1

print("\nPython Q1 Test Case #1")

#Test case #1
def Func(x):
    return x**3 - 25

def FuncDer(x):
    return 3*x**2

Newt(Func, FuncDer, 2, 1e-7)

print("\nPython Q1 Test Case #2")
#Test case #2
def Func2(x):
    return x**2 + 1

def FuncDer2(x):
    return 2*x

Newt(Func2, FuncDer2, 5, 1e-7)

print("\nPython Q1 Test Case #3")
#Test case #3
def Func3(x):
    return math.atan(x)

def FuncDer3(x):
    return 1 / ((x**2) + 1)

Newt(Func3, FuncDer3, 5, 1e-7)







#Python Question #2
print("\n\nPython Question #2 - Parachutist")

def vfunc(x):
    return ((9.8 * x) / 15) * (1 - math.e**((-15/x)*9)) - 35

def vfuncP(x):
    return 0.65333 * (-math.e**(-135 / x) - (135 * math.e**(-135/x) / x) + 1)

Newt(vfunc, vfuncP, 5, 1e-7)




#Python Question #3
#(x^2-4)^2 - 3
print("\n\nPython Question #3 - Aproximating the value of the sqrt")

def q3Func(x):
    return ((x**2) - 4)**2 - 3

def q3FuncP(x):
    return 4*x * (x**2 - 4)

Newt(q3Func, q3FuncP, 5, 1e-7)