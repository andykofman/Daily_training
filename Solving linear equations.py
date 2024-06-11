# -*- coding: utf-8 -*-
"""
Solving linear equations using forward and backward subs

Created on Sun Jun  9 02:58:53 2024

@author: Lenovo
"""

import numpy as np

#check for valid input
def check_if_square (matrix_A, Matrix_B):
    if matrix_A.shape[0] != matrix_A[1]:
        raise ValueError ("invalid input. Matrix has to be square")
        
    if matrix_A[0] != Matrix_B[0]:
        raise ValueError("Dimensions has to be compatible")
    


"""
 Decompose matrix  A into the product of a: 
    lower triangular matrix  L
    and an upper triangular matrix U

"""

def LU_decompose (A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    
    
    for i in range (n):
        
        L[i][i] = 1             #set diagonal of elment L = 1
        for j in range (i, n):
            
            
            # Calculate the sum of the Upper matrix
            sum_u = sum(L[i][k] * U [k][j] for k in range (i))
            U[i][j] = A[i][j] - sum_u
            
            
            # Calculate the sum of the Lower matrix
        for j in range (i+1, n):
            sum_l = sum(L[i][k] * U [k][j] for k in range (i))
            L[i][j] = (A[i][j]- sum_l)/ U[i][i]
            
    return L, U


        
        
#forward substitution

def forward_subs(L, B):
    n = len(B)
    Y= np.zeros(n)
    for i in range (n):
        Y[i] = (B[i] - sum (L[i][j] * Y[i] for j in range (i))) / L[i][i]
        
    return Y


def back_Subs (U, Y):
    n = len(Y)
    x = np.zeros(n)
    
    for i in reversed(range(n)):
        x[i] = (Y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
        
    return x


def solve(A, B):
    L, U = LU_decompose(A)
    Y = forward_subs(L, B)
    x = back_Subs(U, Y)
    
    return x


def get_user_input():
    
    n =int (input("Enter the size of the matrix n*n"))
    A = []
    
    for i in range(n):
       row = list(map(float, input(f"Enter row {i+1} of the matrix (space-separated): ").strip().split()))
       A.append(row)
   
    B = list(map(float, input("Enter the right-hand side vector (space-separated): ").strip().split()))
   
    return np.array(A), np.array(B)


def main():
    A, B = get_user_input()
    X = solve(A, B)
    print("Solution:", X)

if __name__ == "__main__":
    main()