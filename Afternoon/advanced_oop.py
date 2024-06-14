# Day 4 presentation

# Advanced OOP Concepts

# • Encapsulation and data hiding
# • Magic methods and operator overloading
# • Composition vs. inheritance

# Ssentongo Henry Atanus (Encapsulation And Data Hiding)
class Plant:
    __location="Kampala"
    __height=35
    __name="mangoTree"


    def location(self):
        return self.__location

obj=Plant()
print(obj.__location)

class Animal:
    def __init__(self,color):
       self.__color=color
    @property
    def colored(self):
        return self.__color 
      
    @colored.setter
    def colored(self,value):
        self.color=value
polly= Animal("yellow") 
print(polly.colored)      
polly.colored="Brown"
print(polly.colored)  

class Food:
    def __init__(self,name,price) :
        self.__name=name
        self.__price=price
    def get_name(self):
        return self.__name    
    def set_name(self,jk):
           self.__name=jk


f1= Food("Rice",12000) 
print(f1.get_name())
#print(f1.price)
f1.set_name('Banana')
print(f1.get_name())
      
    




# Kisembo Rodgers Bangirana (Magic Methods) 

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__ for unambiguous representation of the object
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # __str__ for readable string representation of the object
    def __str__(self):
        return f"({self.x}, {self.y})"

    # __add__ for adding two vectors
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # __sub__ for subtracting two vectors
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y * other.y)
        return NotImplemented

    # __mul__ for scalar multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x + scalar, self.y - scalar)
        return NotImplemented

    # __rmul__ for scalar multiplication (when the scalar is on the left)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # __eq__ for equality comparison
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # __len__ to get the "length" of the vector (number of components)
    def __len__(self):
        return 2  # A 2D vector always has 2 components

# Examples of using the Vector class and its magic methods
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# __repr__ and __str__
print(repr(v1))  # Output: Vector(2, 3)
print(str(v1))   # Output: (2, 3)

# __add__
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# __sub__
v4 = v2 - v1
print(v4)  # Output: (2, 2)

# __mul__ and __rmul__
v5 = v1 * 3
print(v5)  # Output: (6, 9)
v6 = 2 * v2
print(v6)  # Output: (8, 10)

# __eq__
print(v1 == Vector(2, 3))  # Output: True
print(v1 == v2)            # Output: False

# __len__
print(len(v1))  # Output: 2





# David Hope Kavuma (Operator Overloading)

# You can overload operators by defining special methods in your class, such as:

# __add__ for the + operator
# __sub__ for the - operator
# __mul__ for the * operator
# __truediv__ for the / operator
# And many others


# #EXAMPLE 1A (WITH OPERATOR OVERLOADING)
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

# #EXAMPLE 1B (WITHOUT OPERATOR OVERLOADING)
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






# Olowo Omondi Philly (Composition Vs Inheritance)
# Inheritance is used where a class wants to derive the nature of parent class and then modify 
# or extend the functionality of it. 
# Inheritance will extend the functionality with extra features allows overriding of methods, 

# but in the case of Composition, we can only use that class we can not modify or extend the 
# functionality of it. It will not provide extra features. Thus, when one needs to use the 
# class as it without any modification, the composition is recommended and when one needs to 
# change the behavior of the method in another class, then inheritance is recommended.

# Inheritance models an is-a relationship
# parent class 
class Region: 

	def m1(self): 
		print('We are in the central region') 

# child class inheriting parent class 
class District(Region): 

	# child class constructor 
	def __init__(self): 
		print('Child Class object created') 

	# child class method 
	def m2(self): 
		print('We are in Kampala District') 


# creating object of child class 
obj = District() 

# calling parent class m1() method 
obj.m1() 

# calling child class m2() method 
obj.m2() 



# Composition
# Composition in classes is done by the Has-A Relation
# Example Class A can have or contain an object in another class B



class Parent: 
	def __init__(self): 
		print('Parent class object created...') 

	def m1(self): 
		print('Parent class m1() method executed...') 


class Child: 
	def __init__(self): 

		# creating object of parent class 
		self.obj1 = Parent() 
		print('Child class object also created...') 

	def m2(self): 
		print('Child class m2() method executed...') 
		# calling m1() method of parent class 
		self.obj1.m1() 


# creating object of child class 
obj2 = Child() 

# calling m2() method of child class 
obj2.m2() 
