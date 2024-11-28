# Python Code to find approximation
# of a ordinary differential equation
# using euler method.

# Consider a differential equation
# dy / dx =(x + y + xy)
def func( x, y ):
	return (x + y + x * y)
	
# Function for euler formula
def euler( x0, y, h, x ):
	temp = -0

	# Iterating till the point at which we
	# need approximation
	while x0 < x:
		temp = y
		y = y + h * func(x0, y)
		x0 = x0 + h

	# Printing approximation
	print("Approximate solution at x = ", x, " is ", "%.6f"% y)
	
# Driver Code
# Initial Values
x0 = 0
y0 = 1
h = 0.025

# Value of x at which we need approximation
x = 0.1

euler(x0, y0, h, x)

### Python Code to find approximation
### of a ordinary differential equation
### using euler method.
##
### Consider a differential equation
### dy / dx =(x + y + xy)
##def func( x, y ):
##	return (x + y + x * y)
##	
### Function for euler formula
##def euler( x0, y, h, x ):
##	temp = -0
##
##	# Iterating till the point at which we
##	# need approximation
##	while x0 < x:
##		temp = y
##		y = y + h * func(x0, y)
##		x0 = x0 + h
##
##	# Printing approximation
##	print("Approximate solution at x = ", x, " is ", "%.6f"% y)
##	
### Driver Code
### Initial Values
##x0 = 0
##y0 = 1
##h = 0.025
##
### Value of x at which we need approximation
##x = 0.1
##
##euler(x0, y0, h, x)

###Ankit 8932
##
#Euler's Method
##'''dy/dx = -y with initial condition y(0)=1 '''
##
##'''Differential equation dy/dx=-y'''
##def dydx(y):
##    return -y
##
##def Eulers(x0,y0,h):
##    '''x0=initial x, y0=initial y, h= step value'''
##    for i in range(1,5):
##        x=x0+h
##        y=y0+h*(dydx(y0))
##        x0,y0=x,y
##        print('x'+str(i),'=',x,'y'+str(i),'=',y)
##        
##x0=eval(input("Enter initial x:"))
##y0=eval(input("Enter initial y:"))
##h=eval(input("Enter initial h:"))

##Eulers(x0,y0,h)

#Ankit 8932

##Modified Euler's Method
#
#'''dy/dx=x^2+y with initial condition y(0)=1'''
#
#'''Differential Equation x^2+y'''
#def dydx(x,y):
#    return x**2+y
#
#def Eulers(x0,y0,h):
#    '''x0=initial x, y0=initial y, h= step value'''
#    for i in range(1):
#        x=x0+h
#        y=y0+h*(dydx(x0,y0))
#        for j in range(1,3):
#            y=y0+h/2*(dydx(x0,y0)+dydx(x,y))
#            print('x'+str(i),'=',x,'y'+str(i)+str(j),'=',y)
#       x0,y0=x,y
#        
#x0=eval(input("Enter initial x:"))
#y0=eval(input("Enter initial y:"))
#h=eval(input("Enter initial h:"))
#Eulers(x0,y0,h)

