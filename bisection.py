
def f1(x):
    return x**3+2*x**2-3*x-1


def Bisection(a,b,f,n):
    if f(a)*f(b)>0:
        return ("Invalid interval")
    else:
        for i in range(n):
            
            print(i+1,' iteration')
            m=(a+b)/2
            print('a=',a,'b=',b,'m=',m)
            if f(m)==0:
                return m
            elif f(m)*f(a)<0:
                b=m
            else:
                a=m
            
        return m
            
print('Ans=',(Bisection(-10,10,f1,5)))
