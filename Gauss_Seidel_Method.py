

import numpy as np

def gaussy(A, b, n):
    
    l = np.arange(n)
    s = np.zeros(n)
    

    #Find the Scale vector
    for i in range(n):

        smax = 0

        for j in range(n):

            if abs(A[i,j]) > smax:
                smax = abs(A[i,j])

            s[i] = smax


    #obtain ratios
    for k in range(0,n):

        rmax = 0
        j = 0

        for i in range(k, n):
            ratio = abs(A[l[i], k] / s[l[i]])

            if ratio > rmax:
                rmax = ratio
                j = i


        #swap
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

    #Calculate Multipliers
        for i in range(k+1, n):
            x_multiplier = A[l[i], k] / A[l[k], k]

            A[l[i], k] = x_multiplier
            

            for j in range(k+1, n):
                A[l[i],j] = A[l[i],j] - x_multiplier * A[l[k], j]


    #Update array b
    for k in range(n):
        for i in range(k+1, n):
            b[l[i]] = b[l[i]] - A[l[i],k] * b[l[k]]

    #Solve
    x = np.zeros(n)

    x[n-1] = b[l[n-1]] / A[l[n-1],n-1]

  

    for i in range(n-2, -1, -1):
        summ = b[l[i]]
        
        for j in range(i+1, n):
            summ -= A[l[i],j] * x[j]
        
        x[i] = summ / A[l[i], i]



    print("The solution vector is", x)
    return x


#Example a for problem #1
matrix_a = np.array([[3.0, -13.0, 9.0,  3.0],
                     [-6.0, 4.0, 1.0, -18.0],
                     [6.0, -2.0, 2.0,   4.0],
                     [12.0, -8.0, 6.0, 10.0]])

matrix_b = np.array([-19.0, -34.0, 16.0, 26.0])

n = 4

print("Example a for problem #1")
gaussy(matrix_a, matrix_b, n)
print("\n")




#Example #2
a = np.array([[2, 4, -2], [1, 3, 4], [5, 2, 0]], float)
n = 3
b = np.array([6, -1, 2], float)

print("Example b for problem #1")
gaussy(a, b, n)
print("\n")



a = np.array([[(1/2), (1/3), (1/4), (1/5), (1/6)], 
              [(1/3), (1/4), (1/5), (1/6), (1/7)],
              [(1/4), (1/5), (1/6), (1/7), (1/8)], 
              [(1/5), (1/6), (1/7), (1/8), (1/9)], 
              [(1/6), (1/7), (1/8), (1/9), (1/10)]], float)
c = np.copy(a)
b = np.array([.882, .744, .618, .521, .447], float)
d = np.copy(b)
n = 5


print("Example c for problem #1")
x = gaussy(a, b, n)

t = c.dot(x)
print("The residual vector is", d-t)
print("\n\n")

#The approximations appears to be very close.



def GaussSeidel(A, b, x, N, tol):
    eps = .5 * (10 ** (-4))
    kmax = 100


    for k in range(kmax):
        y = np.copy(x)
        
        for i in range(0, N):
            summ = b[i]
            diag = A[i, i]

            if abs(diag) < tol:
                print("Diagonal element is too small!")
                return

            for j in range(0, i):
                summ -= A[i, j] * x[j]

            for j in range(i+1, N):
                summ -= A[i, j] * x[j]
    
            x[i] = summ / diag

        t = np.linalg.norm((x-y), ord = 1)

        if t < eps:
            print("It took", k, "iterations for the Gauss Seidel method to converge to the vector", x, ".")
            return

    print("After", kmax, "iterations, no convergence was found.")
    print("Output:", x)
    
    return


#Part A for Question #2
a = np.array([[3, 1], [2, 6]], float)
b = np.array([5, 9], float)
x = np.array([1, 1], float)
N = 2
tol = 10 ** -10

print("Part A question #2")
GaussSeidel(a, b, x, N, tol)
print("\n")

#Part B for Question #2
a = np.array([[(1/2), (1/3), (1/4), (1/5), (1/6)],
              [(1/3), (1/4), (1/5), (1/6), (1/7)], 
              [(1/4), (1/5), (1/6), (1/7), (1/8)], 
              [(1/5), (1/6), (1/7), (1/8), (1/9)], 
              [(1/6), (1/7), (1/8), (1/9), (1/10)]], float)
b = np.array([.882, .744, .618, .521, .447], float)
x = np.array([1, 1, 1, 1, 1], float)
N = 5
tol = 10 ** -5

print("Part B question #2")
GaussSeidel(a, b, x, N, tol)
print("\n")

#With the initial vector of all 1's, it seems that the run goes over the maximum allowed iterations indicating that there was no convergence found. Comparing the output to our Gaussy procedure, we can see that the approximated solutions are no where near each other.


#Changing initial vector for second run.
x = np.array([-2.52, 5.04, 2.52, 7.56, -10.08], float)

GaussSeidel(a, b, x, N, tol)


# After changing the initial vector, we get an immediate solution.

#1
#The residual vector was better then mine.

#2
#My answer was truncated compared to the Maple answer. The same goes for the second initial vector. I believe the Gauss Seidel should have converged immediately in this case.

#3
#The condition number was very high, which indicates that there exists a large amount of error with the chosen matrix and vector. Specifically, this indicates that the presence of error in the previous questions are great.
