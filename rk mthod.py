###Runge Kutta method second order
##'''dy/dx = y-x with initial condition y(0)=2 '''
##
##'''Differential equation dy/dx=y-x'''
##def dydx(x,y):
##    return y-x
##
##def RK2(x0,y0,h):
##    '''x0=initial x, y0=initial y, h= step value'''
##    
##    for i in range(1,5):
##        x=x0+h
##        
##        k1=h*dydx(x0,y0)
##        k2=h*dydx(x0+h,y0+k1)
##        
##        y=y0+0.5*(k1+k2)
##        print('x'+str(i),'=',x,'y'+str(i),'=',y)
##        
##        x0,y0=x,y
##        
##x0=eval(input("Enter initial x:"))
##y0=eval(input("Enter initial y:"))
##h=eval(input("Enter initial h:"))
##
##RK2(x0,y0,h)

##Ankit 8932

Runge-Kutte of Fourth Order
'''dy/dx=3x+y/2 with initial condition y(0)=1'''

'''Differential Equation dy/dx=3x+y/2'''
def dydx(x,y):
    return 3*x+y/2

def RK4(x0,y0,h):
    '''x0=initial x, y0=initial y, h= step value'''

    for i in range(1,6):
        x=x0+h
        
        k1=h*dydx(x0,y0)
        k2=h*dydx(x0+h/2,y0+k1/2)
        k3=h*dydx(x0+h/2,y0+k2/2)
        k4=h*dydx(x0+h,y0+k3)
        
        y=y0+(k1+2*k2+2*k3+k4)/6
        print('x'+str(i),'=',x,'y'+str(i),'=',y)

        x0,y0=x,y
        
x0=eval(input("Enter initial x:"))
y0=eval(input("Enter initial y:"))
h=eval(input("Enter initial h:"))

RK4(x0,y0,h)

