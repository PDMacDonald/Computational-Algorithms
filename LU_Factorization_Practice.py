# LU Factorization 
# MAT4990-101
# @author Preston MacDonald
# @version 01-19-18

import scipy
import scipy.linalg


# Row oriented factorization
#
# @param lowerTri
#       Lower triangle matrix of A
# @param b
#       B vector
# @return xVector (Y)
def LFactor(lowerTri, b):
  
  DIMENSIONS = len(lowerTri)
  
  matrixL = lowerTri
  xVector = [0 for i in range(DIMENSIONS)]
  bVector = b
  
  #X sub 1 
  xVector[0] = bVector[0] / matrixL[0][0]
  
  #X sub 2 to X sub n
  for i in range(1, DIMENSIONS):
    
    summ = 0
    
    for j in range (0, i):
      summ += matrixL[i][j] * xVector[j]
    
    xVector[i] = (bVector[i] - summ) / matrixL[i][i]
  
  return xVector
  


# backwards column oriented factorization
#
# @param upperTri
#       upper triangle matrix of A
# @param yMatrix
#       Y matrix given by LFactor
def UFactor(upperTri, yMatrix):
  
  DIMENSIONS = len(upperTri)
  matrixU = upperTri
  xMatrix = yMatrix

  
  
  for j in range(DIMENSIONS - 1, -1, -1):
    
    xMatrix[j] = xMatrix[j] / matrixU[j][j]
    
    for i in range(j - 1, -1, -1):
      
      xMatrix[i] = xMatrix[i] - matrixU[i][j] * xMatrix[j]
      
   
  
  
  
  print("Output:\n")
  for i in range(DIMENSIONS):
    print("[", xMatrix[i], "]\n")
  return xMatrix[i]



#
# INPUT for both problems 1 and two
#
#


AOne = [[ 4, -1, -1, 0], \
     [-1,  4,  0,-1], \
     [-1,  0,  4,-1], \
     [ 0, -1, -1, 4] \
    ]

bVecOne = [40, 30, 30, 20]

ATwo =  [[4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,0,0,-1,4,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [-1,0,0,0,0,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0], \
        [0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0], \
        [0,0,0,0,-1,0,0,0,-1,4,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0], \
        [0,0,0,0,0,-1,0,0,0,0,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0], \
        [0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0,0], \
        [0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0,0], \
        [0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0,0,0,0], \
        [0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,0,0,0,0,-1,0,0,0,0,0], \
        [0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,4,-1,0,0,0,-1,0,0,0,0], \
        [0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0,0,-1,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,0,0,0,0,-1], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,4,-1,0,0,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1,0], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4,-1], \
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,-1,4], \
        ]
        
bVecTwo = [40, 30, 30, 30, 30, 10, 0, 0, 0 ,0, 10, 0, 0, 0 ,0, 10, 0, 0, 0 ,0, 30, 20, 20, 20, 20]


#Solving Problem 1
P, L, U = scipy.linalg.lu(AOne, False, False, True)

Y = LFactor(L, bVecOne)

print("Problem #1 Solution")
UFactor(U, Y)


#Solving Problem 2
P, L, U = scipy.linalg.lu(ATwo, False, False, True)

Y = LFactor(L, bVecTwo)

print("\n\nProblem #2 Solution")
UFactor(U, Y)

















