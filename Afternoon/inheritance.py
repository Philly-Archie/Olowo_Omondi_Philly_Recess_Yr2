# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class:
class MyClass:
  x = 5

p1 = MyClass()# this is an object of the class
print(p1.x)

# The self-parameter
# The self-parameter refers to the current instance of the class and accesses the class variables. We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.

# _ _init_ _ method
# In order to make an instance of a class in Python, a specific function called __init__ is called. Although it is used to set the object's attributes, it is often referred to as a constructor.

# The self-argument is the only one required by the __init__ method. This argument refers to the newly generated instance of the class. To initialise the values of each attribute associated with the objects, you can declare extra arguments in the __init__ method.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Advantages of Inheritance and Polymorphism
# Inheritance:
# It permits code to be reused and avoids code duplication.
# It permits for the creation of hierarchical classifications.
# It permits for extensibility, as new subclasses can be made.
# It permits for less demanding support and debugging.
# Polymorphism:
# It permits for the execution of dynamic dispatch and the implementation of interfaces.
# It reduces the number of lines of code and makes it simpler to maintain.
# It permits for the execution of more generic algorithms.
# It permits the execution of more adaptable programs.

# Disadvantages of Inheritance and Polymorphism
# Inheritance:
# Tight coupling: Inheritance makes a firmly coupled relationship among classes, making it troublesome to adjust existing code without breaking other program parts.
# Increased complexity: Inheritance can increment the complexity of a program, as increasing classes are included to back the inheritance hierarchy.
# Overuse: Inheritance ought to be utilized sparingly because it can lead to overcomplicated designs and implementations that are troublesome to keep up with.
# Polymorphism:
# Trouble investigating: Polymorphism can make it challenging to investigate code because it can be hard to track the stream of execution when the same code is executing in several ways.
# Execution issues: Polymorphism can lead to execution issues, as the framework must check each object's sort to decide which strategy to execute.
# Superfluous complexity: Polymorphism can too lead to pointless complexity in the event that it is utilized when a less complex approach would suffice.

# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Types of Inheritance in Python

# Single inheritance: A derived class inherits from one base class.
# Multiple inheritance: A derived class inherits from multiple base classes.
# Multilevel inheritance: A derived class inherits from a base class that inherits from another base class.
# Hierarchical inheritance: Multiple derived classes inherit from the same base class.
# Hybrid inheritance: A combination of two or more of the above inheritance types.\

# Python program to show single inheritance
 
class a:
	def __init__(self):
			self.name = n
class b(a):
	def __init__(self):
			self.roll = roll

# Python code to show the working of multiple inheritance      
class B1(object):
    def __init__(self):
        self.str1 = "Python1"
        print("B1 initialized")
  
class B2(object):
    def __init__(self):
        self.str2 = "Python2"        
        print("B2 initialized")
  
class Derived(B1, B2):
    def __init__(self):
        super().__init__()  # This calls the __init__ method of B1 due to Method Resolution Order (MRO)
        B2.__init__(self)   # Explicitly calling the __init__ method of B2
        print("Derived initialized")

# Create an instance of Derived to see the inheritance in action
d = Derived()

# Check the attributes
print(d.str1)
print(d.str2)

        
        

# Python program to show multilevel inheritance
 
# The base class
class grandma:
	def __init__(self, grandmaname):
		self.grandmaname = grandmaname
 
# Middle class
class mother(grandma):
	def __init__(self, mothername, grandmaname):
		self.mothername = mothername
 
		# invoke a constructor of grandma class
		grandma.__init__(self, grandmaname)
 
# last class
class son(mother):
	def __init__(self,sonname, mothername, grandmaname):
		self.sonname = sonname
 
		# invoke a constructor of mother class
		father.__init__(self, mothername, grandmaname)
 
	def print_name(self):
		print('Grandma name :', self.grandmaname)
		print("Mother name :", self.mothername)
		print("Son name :", self.sonname)
  

#Python program to show hierarchical inheritance
 
# The base class
class parent:
      def funA(self):
          print("This function is in the parent class.")
 
# Derived class one
class child_one(parent):
      def funB(self):
          print("This function is in class child_one.")
 
# Derived class two
class child_two(parent):
      def funC(self):
          print("This function is in class child_two.")
          
          

class a:
	def funcA(self):
		print("Hello, you are now in class A")
class b(a):
	def funcB(self):
		print("Hello, you are now in class B")
class c(a):
	def funcC(self):
		print("Hello, you are now in class C")
class d(c,a):
	def funcD(self):
	    print("Hello, you are now in class D")
 
ref = d()
ref.funcD()
ref.funcC()
ref.funcA()


# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(self.fname, self.lname)
        
x = Person("Arinda", "Tarasisio")
x.print_name()

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass # Use the pass keyword when you do not want to add any other properties or methods to the class.

x1 = Student("Tahia", "Becka") # Now the Student class has the same properties and methods as the Person class.
x1.print_name()

# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# class Student(Person):
#   def __init__(self, fname, lname):
# x2 = Student("mike", "ppp")
# x2.print_name # this will cause an error because the derived class nolonger has the properties of the base class

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.print_name()

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
    
y =Student("Vanessa", "Aijuka")
y.print_name()

# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

# Add methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x = Student("Arinda", "Asiimwe", 2019)
x.welcome()

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
#Which brings us to Polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# Polymorphism in Python allows objects of different classes to be treated as objects of a common superclass. 

# It is implemented through method overriding and interfaces.

# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.

class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
    

# Polymorphism with Functions, Functions can take objects of different classes that implement the same method.
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

# Polymorphism with Inheritance Using polymorphism with class inheritance, you can call overridden methods from the base class references.
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

animals = [Dog(), Cat()]

for animal in animals:
    animal_sound(animal)
    
    
# Polymorphism with Abstract Base Class, Using the abc module to define an abstract base class and implementing polymorphism.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())



# Polymorphism with Duck Typing Python's dynamic nature allows for a more flexible form of polymorphism known as duck typing, where the type of an object is determined by its behavior (methods and properties) rather than its class
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

class Bird:
    def sound(self):
        return "Chirp"

# Polymorphism in action
def make_sound(animal):
    print(animal.sound())

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    make_sound(animal)



# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
    
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


#  If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  
# Child classes inherits the properties and methods from the parent class.

# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism we can execute the same method for all classes.