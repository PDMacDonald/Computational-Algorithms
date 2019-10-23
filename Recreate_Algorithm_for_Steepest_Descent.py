
# @author Preston MacDonald
# @version 03-27-2018
#
# Algorithm for Steepest Descent

import numpy.linalg as linalg
import numpy as np


# An algorithm for finding nearest local minimum of a function
# which presuspposes that the gradient of the function can be 
# computed. The method steepest descent, also called the 
# gradient descent method, starts at a given initial point
# and as many times as needed, moves from x to the next x by
# minimizing along the line extending from point x in the
# direction of gradient f(x), the local downhill gradient.
# Using Description given at:
#http://mathworld.wolfram.com/MethodofSteepestDescent.html
#
# @param mA
#     A matrix A
# @param b
#     TODO: this b is the b in ax = b
# @param iX
#     A initial X
# @param tol
#     A tolerance to compare the 2nd norm of residual with.
def SteepDes(mA, b, iX, maxI, tol):
  #initialize Variables
  r = b - np.matmul(mA, iX)
  print("TROUBLESHOOT")
  print(b)
  print(iX)
  print(r)
  i = 0
  alpha = 0
  newX = iX
  
  
  while (linalg.norm(r, 2) > tol):
    
    i = i + 1
    # Variable to hold repeated calculation for efficiency.
    u = np.matmul(mA, r)
    alpha = (np.matmul(np.transpose(r), r)) / (np.matmul(np.transpose(r), u))
    newX = newX + alpha[0,0] * r
    r = r - np.dot(alpha[0,0], u)
    
    if (i >= maxI):
      break
    
  print("Alpha: ")
  print(alpha[0,0])
  print("Total iterations: ", i)
  print("The ending residual: ")
  print(r)
  print("The new X after steepest Descent Algorithm:")
  print(newX)





# Code to create a sample problem to run Steepest Descent
#ignore error???
A = np.random.rand(5,5)
X = np.random.rand(5,1)
print("\n*****Randomly generated matrix*****\n ")
print(A)

#make matrix symmetric
symA = np.dot(A, np.transpose(A))

print("\n*****Symmetric Random Matrix:*****\n ")
print(symA)

#check for Positive Definite
try:
  print("\n*****Cholesky Decomposition:*****\n")
  print("Matrix A =")
  print(linalg.cholesky(symA))
  print("\nReady to run Steepest Desecent Algorithm.\n\n")
except:
  print("Random matrix is not Symmetric Positive definite")
  print("Could not use algorithm for steepest descent on the")
  print("generated matrix.")

print("\n running steepest descent on matrix A......")
B = np.matmul(symA, X)
print("B MATRIX: ")
print(B)
iX = np.zeros((5,1))
SteepDes(symA, B, iX, 10000, .0000000001)

print("The actual X matrix:")
print(X)



















