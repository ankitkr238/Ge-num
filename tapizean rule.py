def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    
    print(f"{'i':<5}{'x_i':<10}{'f(x_i)':<10}")
    for i in range(1, n):
        x_i = a + i * h
        f_x_i = f(x_i)
        total += f_x_i
        print(f"{i:<5}{x_i:<10.4f}{f_x_i:<10.4f}")
    
    total *= h
    return total

# Example function to integrate
def function(x):
    return x ** 2  # Example: f(x) = x^2

# Parameters for the trapezoidal rule
a = 0  # Lower limit
b = 1  # Upper limit
n = 10  # Number of intervals

result_trapezoidal = trapezoidal_rule(function, a, b, n)
print(f"\nTrapezoidal Rule Result: {result_trapezoidal:.4f}")
