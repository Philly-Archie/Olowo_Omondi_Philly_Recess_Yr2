# You can overload operators by defining special methods in your class, such as:

# __add__ for the + operator
# __sub__ for the - operator
# __mul__ for the * operator
# __truediv__ for the / operator
# And many others


#EXAMPLE 1A (WITH OPERATOR OVERLOADING)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2  # uses the __add__ method
print(v3.x)  # prints 6
print(v3.y)  # prints 8

#EXAMPLE 1B (WITHOUT OPERATOR OVERLOADING)
class Vector1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, scalar):
        return Vector1(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create a vector
vec = Vector1(3, 4)

# Scale the vector using a method call
scaled_vec = vec.scale(2)

# Print the result
print(scaled_vec)  # Output: (6, 8)

#EXAMPLE 2A (WITH OPERATOR OVERLOADING)
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Create complex numbers
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)

# Add complex numbers using + operator
result = num1 + num2

# Print the result
print(result)  # Output: 4 + 9i

#EXAMPLE 2B (WITHOUT OPERATOR OVERLOADING)
class ComplexNumber1:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return ComplexNumber1(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Create complex numbers
num1 = ComplexNumber1(3, 2)
num2 = ComplexNumber1(1, 7)

# Add complex numbers using a method call
result = num1.add(num2)

# Print the result
print(result)  # Output: 4 + 9i

