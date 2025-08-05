def flippingMatrix(matrix):
 n=len(matrix)//2
 sum=0
 for i in range(n):
 for j in range (n):
            c=[matrix[i][j],matrix[i][-(j+1)],matrix[-(i+1)][j],matrix[
(i+1)][-(j+1)]]
            sum+=max(c)
            
    return sum 