# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def seidel(a, x ,b):
	#Finding length of a(3)	 
	n = len(a)				 
	# for loop for 3 times as to calculate x, y , z
	for j in range(0, n):	 
		# temp variable d to store b[j]
		d = b[j]				 
		
		# to calculate respective xi, yi, zi
		for i in range(0, n):	 
			if(j != i):
				d-=a[j][i] * x[i]
		# updating the value of our solution	 
		x[j] = d / a[j][j]
	# returning our updated solution		 
	return x 

# int(input())input as number of variable to be solved			 
n = 2						
a = []						 
b = []	 
# initial solution depending on n(here n=3)					 
x = [0, 0]					 
a = [[16,3],[7,-11]]
b = [11,13]

#loop run for m times depending on m the error value
for i in range(0, 25):		 
	x = seidel(a, x, b)
	
print(x)					 
