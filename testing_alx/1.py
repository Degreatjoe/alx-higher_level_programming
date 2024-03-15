# Importing functions from calculator_1.py
import calculator_1

# Defining variables a and b
a = 10
b = 5

# Calling functions from calculator_1.py with arguments a and b
result_sum = calculator_1.add(a, b)
result_diff = calculator_1.sub(a, b)
result_prod = calculator_1.mul(a, b)
result_quot = calculator_1.div(a, b)

# Printing results
print("Sum:", result_sum)
print("Difference:", result_diff)
print("Product:", result_prod)
print("Quotient:", result_quot)
