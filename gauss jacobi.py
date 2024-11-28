#Gauss Jacobi method


A=[[6,-2,1],[-2,7,2],[1,2,-5]]
B=[11,5,-1]
X0=[0,0,0]
X=X0
k=0
N=10
while k<N:
    for i in range(len(A)):
        sum=0  
        for j in range(len(A[i])):
            sum+=(A[i][j]*X0[j])
        X[i]=X[i]+(1/A[i][i])*(B[i]-sum)
    print(k+1,' iteration')
    print(X)
    k+=1
print(X)
