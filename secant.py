# Secant Method for finding roots

def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        # Calculate the function values
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            print("Division by zero encountered.")
            return None

        # Secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Check if the result is within the tolerance level
        if abs(x2 - x1) < tol:
            print(f"Root found after {i+1} iterations: {x2}")
            return x2
        
        # Update guesses
        x0, x1 = x1, x2

    print("Max iterations reached. Solution may not have converged.")
    return x2


def func(x):
     return x**2 - 4*x +2
x0 = 4
x1 = 3
root = secant_method(func, x0, x1)
print(f"Estimated root: {root}")
