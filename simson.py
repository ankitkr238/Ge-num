#SImpsons 1/3 
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:  # Simpson's rule requires n to be even
        n += 1
    
    h = (b - a) / n
    total = f(a) + f(b)

    print(f"{'i':<5}{'x_i':<10}{'f(x_i)':<10}")
    for i in range(1, n):
        x_i = a + i * h
        f_x_i = f(x_i)
        
        if i % 2 == 0:
            total += 2 * f_x_i
        else:
            total += 4 * f_x_i
            
        print(f"{i:<5}{x_i:<10.4f}{f_x_i:<10.4f}")
    
    total *= h / 3
    return total

# Parameters for Simpson's rule
a = 0  # Lower limit
b = 1  # Upper limit
n = 10  # Number of intervals (must be even)
def function(x):
    return x ** 2  # Example: f(x) = x^2

result_simpsons = simpsons_rule(function, a, b, n)
print(f"\nSimpson's Rule Result: {result_simpsons:.4f}")

###SImpsons 3/8
##def simpsons_rule(f, a, b, n):
##    if n % 2 == 1:  # Simpson's rule requires n to be even
##        n += 1
##    
##    h = (b - a) / n
##    total = f(a) + f(b)
##
##    print(f"{'i':<5}{'x_i':<10}{'f(x_i)':<10}")
##    for i in range(1, n):
##        x_i = a + i * h
##        f_x_i = f(x_i)
##        
##        if i % 3 == 0:
##            total += 2 * f_x_i
##        else:
##            total += 3 * f_x_i
##            
##        print(f"{i:<5}{x_i:<10.4f}{f_x_i:<10.4f}")
##    
##    total *= 3*h/8
##    return total
##
### Parameters for Simpson's rule
##a = 0  # Lower limit
##b = 1  # Upper limit
##n = 10  # Number of intervals (must be even)
##def function(x):
##    return x ** 2  # Example: f(x) = x^2
##
##result_simpsons = simpsons_rule(function, a, b, n)
##print(f"\nSimpson's Rule Result: {result_simpsons:.4f}")
