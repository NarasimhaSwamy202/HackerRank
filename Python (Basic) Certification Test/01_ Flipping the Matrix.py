# HackerRank
# HackerRank Python (Basic) Certification Test : Question and Answers :
# -------------------------------------------------------------------------------------------------------
# Question 1: Python — Maximize sum of N X N upper left sub-matrix from given 2N X 2N matrix.
# Given a 2N x 2N matrix of integers. You are allowed to reverse any row or column any number of times and in any order. The task is to calculate the maximum sum of the upper-left N X N submatrix i.e the sum of elements of the submatrix from (0, 0) to (N – 1, N – 1).

# Python3 program to find the maximum value 
# of top N/2 x N/2 matrix using row and 
# column reverse operations 

def maxSum(mat): 
    R = len(mat)         #Rows
    C = len(mat[0])      #Columns
    Sum = 0
    for i in range(0, R // 2): 
        for j in range(0, C // 2): 
  
            r1, r2 = i, R - i - 1
            c1, c2 = j, C - j - 1

            Sum += max(max(mat[r1][c1], mat[r1][c2]), 
                       max(mat[r2][c1], mat[r2][c2])) 
  
    return Sum
  
  
# Driver Code 
if __name__ == "__main__": 
  
    R = C = 4
    mat = [[112, 42, 83, 119], 
           [56, 125, 56, 49], 
           [15, 78, 101, 43], 
           [62, 98, 114, 108]] 
  
    print(maxSum(mat))
