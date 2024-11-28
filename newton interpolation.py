
def newton_interpolation(x, y, x_value):
    
    n = len(x)
    # Divided difference table
    divided_diff = []
    for i in range(n):
        divided_diff.append([])
        divided_diff[i].append(y[i])
        for j in range(1,n):
            divided_diff[i].append(0)
    print(y)
    print(divided_diff)
    # Fill the divided difference table
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x[i + j] - x[i])

    # Compute the interpolation polynomial at x_value
    result = divided_diff[0][0]
    product = 1.0
    for j in range(1, n):
        product *= (x_value - x[j - 1])
        result += divided_diff[0][j] * product

    return result

# Example usage
x_points = [19,39,59,79,99]
y_points = [41,103,168,218,235]
x_to_evaluate = 22

# Compute interpolated value
interpolated_value = newton_interpolation(x_points, y_points, x_to_evaluate)
print(f"Interpolated value at x = {x_to_evaluate}: {interpolated_value:.6f}")
