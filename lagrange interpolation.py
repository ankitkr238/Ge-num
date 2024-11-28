#Lagrange Interpolation

def L(X,Y,x):
    sum=0
    for i in range(len(X)):
        t=1
        for j in range(len(X)):
            if i==j:
                continue
            t*=(x-X[j])/(X[i]-X[j])
        sum+=t*Y[i]
    return sum

X,Y=[-5,-3,2,3,5,9],[25,9,4,9,25,81]

print('x=7 y=',L(X,Y,7))
print('x=2.5 y=',L(X,Y,2.5))
